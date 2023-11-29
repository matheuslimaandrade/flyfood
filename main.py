from itertools import permutations
from time import time


def ler_matriz(arquivo):
    with open(arquivo, 'r') as file:
        linhas = file.readlines()
    matriz = [linha.split() for linha in linhas]
    return matriz


def calcular_distancia(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def calcular_distancia_total(percurso):
    d = 0
    for i in range(1, len(percurso)):
        d += calcular_distancia(percurso[i - 1], percurso[i])
    return d


def encontrar_menor_trajeto(matriz):
    pontos_entrega = []
    ponto_origem = None

    for i, linha in enumerate(matriz):
        for j, ponto in enumerate(linha):
            if ponto != '0' and ponto != 'R':
                pontos_entrega.append(((i, j), ponto))
            elif ponto == 'R':
                ponto_origem = (i, j)

    menor_trajeto = None
    menor_distancia = float('inf')

    for permutacao in permutations(pontos_entrega):
        percurso = [ponto_origem] + [p[0] for p in permutacao] + [ponto_origem]
        distancia = calcular_distancia_total(percurso)

        if distancia < menor_distancia:
            menor_distancia = distancia
            menor_trajeto = percurso[1:-1]  

    return menor_trajeto


def main():
    arquivo = 'matriz_entregas.txt' 
    matriz = ler_matriz(arquivo)

    menor_trajeto = encontrar_menor_trajeto(matriz)

    print(f"Menor trajeto otimizado para entregas: {menor_trajeto}")


if __name__ == "__main__":
    main()
