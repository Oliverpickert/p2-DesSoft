from collections import Counter

def calcula_pontos_quadra(dados):
    counts = Counter(dados)
    if any(v >= 4 for v in counts.values()):
        total = 0
        for value in dados:
            total += value
        return total
    return 0