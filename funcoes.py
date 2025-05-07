import random
from collections import Counter

def rolar_dados(quantidade_dados: int) -> list[int]:
    resultados = []
    for _ in range(quantidade_dados):
        resultado_dado = random.randint(1, 6)
        resultados.append(resultado_dado)
    return resultados

def guardar_dado(dados_rolados: list[int], dados_no_estoque: list[int], indice_dado_para_guardar: int) -> list[list[int]]:
    dado_a_ser_guardado = dados_rolados.pop(indice_dado_para_guardar)
    dados_no_estoque.append(dado_a_ser_guardado)
    return [dados_rolados, dados_no_estoque]

def remover_dado(dados_rolados: list[int], dados_no_estoque: list[int], indice_dado_para_remover: int) -> list[list[int]]:
    dado_removido = dados_no_estoque.pop(indice_dado_para_remover)
    dados_rolados.append(dado_removido)
    return [dados_rolados, dados_no_estoque]

def calcula_pontos_regra_simples(dados_rolados: list[int]) -> dict[int, int]:
    pontos = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for dado in dados_rolados:
        if 1 <= dado <= 6:
            pontos[dado] += dado
    return pontos

def calcula_pontos_soma(dados):
    soma = 0
    for dado in dados:
        soma += dado
    return soma

def calcula_pontos_sequencia_baixa(dados_rolados: list[int]):
    if len(dados_rolados) < 4:
        return 0
    dados_ordenados = sorted(dados_rolados)
    dados_unicos = []
    for dado in dados_ordenados:
        if dado not in dados_unicos:
            dados_unicos.append(dado)
    if len(dados_unicos) < 4:
        return 0
    for i in range(len(dados_unicos) - 3):
        if (dados_unicos[i] + 1 == dados_unicos[i+1] and 
            dados_unicos[i+1] + 1 == dados_unicos[i+2] and 
            dados_unicos[i+2] + 1 == dados_unicos[i+3]):
            return 15
    return 0

def calcula_pontos_sequencia_alta(dados_rolados: list[int]):
    if len(dados_rolados) < 5:
        return 0
    dados_ordenados = sorted(dados_rolados)
    dados_unicos = []
    for dado in dados_ordenados:
        if dado not in dados_unicos:
            dados_unicos.append(dado)
    if len(dados_unicos) < 5:
        return 0
    for i in range(len(dados_unicos) - 4):
        if (dados_unicos[i] + 1 == dados_unicos[i+1] and 
            dados_unicos[i+1] + 1 == dados_unicos[i+2] and 
            dados_unicos[i+2] + 1 == dados_unicos[i+3] and
            dados_unicos[i+3] + 1 == dados_unicos[i+4]):
            return 30
    return 0

def calcula_pontos_full_house(dados_rolados: list[int]):
    if len(dados_rolados) < 5:
        return 0
    contagem = {}
    for dado in dados_rolados:
        if dado in contagem:
            contagem[dado] += 1
        else:
            contagem[dado] = 1
    tem_tres = False
    tem_dois = False
    soma_total = 0
    for valor, quantidade in contagem.items():
        if quantidade >= 3 and not tem_tres:
            tem_tres = True
            soma_total += valor * 3
        elif quantidade >= 2 and not tem_dois:
            tem_dois = True
            soma_total += valor * 2
    if tem_tres and tem_dois:
        return soma_total
    return 0

def calcula_pontos_quadra(dados):
    counts = Counter(dados)
    if any(v >= 4 for v in counts.values()):
        total = 0
        for value in dados:
            total += value
        return total
    return 0

def calcula_pontos_quina(dados):
    counts = Counter(dados)
    if any(v >= 5 for v in counts.values()):
        return 50
    return 0 

def calcula_pontos_regra_avancada(dados_rolados: list[int]):
    resultado = {
        'cinco_iguais': calcula_pontos_quina(dados_rolados),
        'full_house': calcula_pontos_full_house(dados_rolados),
        'quadra': calcula_pontos_quadra(dados_rolados),
        'sem_combinacao': calcula_pontos_soma(dados_rolados),
        'sequencia_alta': calcula_pontos_sequencia_alta(dados_rolados),
        'sequencia_baixa': calcula_pontos_sequencia_baixa(dados_rolados)
    }
    return resultado

def faz_jogada(dados: list[int], categoria: str, cartela_de_pontos: dict):
    pontos_simples = calcula_pontos_regra_simples(dados)
    pontos_avancados = calcula_pontos_regra_avancada(dados)
    if categoria in ['1', '2', '3', '4', '5', '6']:
        cartela_de_pontos['regra_simples'][int(categoria)] = pontos_simples[int(categoria)]
    else:
        cartela_de_pontos['regra_avancada'][categoria] = pontos_avancados[categoria]
    return cartela_de_pontos