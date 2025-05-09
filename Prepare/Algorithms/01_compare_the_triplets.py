#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts the following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Inicializa as pontuações de Alice e Bob
    alice_score = 0
    bob_score = 0
    
    # Laço para comparar as pontuações nas 3 categorias
    for i in range(3):
        if a[i] > b[i]:
            alice_score += 1
        elif a[i] < b[i]:
            bob_score += 1
    
    # Retorna as pontuações de Alice e Bob como uma lista
    return [alice_score, bob_score]

if __name__ == '__main__':
    # Recebe as entradas do usuário
    a = list(map(int, input().rstrip().split()))  # Pontuações de Alice
    b = list(map(int, input().rstrip().split()))  # Pontuações de Bob

    # Chama a função compareTriplets para calcular os pontos
    result = compareTriplets(a, b)

    # Salva o resultado no arquivo output.txt
    with open('output.txt', 'w') as fptr:
        fptr.write(' '.join(map(str, result)) + '\n')  # Escreve a saída no arquivo

