import random

def rolar_dados(quantidade_dados: int) -> list[int]:
    resultados = []
    for _ in range(quantidade_dados):
        resultado_dado = random.randint(1, 6)
        resultados.append(resultado_dado)
    return resultados
