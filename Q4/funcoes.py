def calcula_pontos_regra_simples(dados_rolados: list[int]) -> dict[int, int]:
    pontos = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for dado in dados_rolados:
        if 1 <= dado <= 6:
            pontos[dado] += dado
    return pontos