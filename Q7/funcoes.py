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


