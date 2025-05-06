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




