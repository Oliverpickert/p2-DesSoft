def guardar_dado(dados_rolados: list[int], dados_no_estoque: list[int], indice_dado_para_guardar: int) -> list[list[int]]:
    dado_a_ser_guardado = dados_rolados.pop(indice_dado_para_guardar)
    dados_no_estoque.append(dado_a_ser_guardado)
    return [dados_rolados, dados_no_estoque]