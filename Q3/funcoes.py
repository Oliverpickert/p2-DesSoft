def remover_dado(dados_rolados: list[int], dados_no_estoque: list[int], indice_dado_para_remover: int) -> list[list[int]]:

    dado_removido = dados_no_estoque.pop(indice_dado_para_remover)
    dados_rolados.append(dado_removido)
    return [dados_rolados, dados_no_estoque]
