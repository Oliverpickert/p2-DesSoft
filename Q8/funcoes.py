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
