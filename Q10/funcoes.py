from collections import Counter

def calcula_pontos_quina(dados):
    counts = Counter(dados)
    if any(v >= 5 for v in counts.values()):
        return 50
    return 0