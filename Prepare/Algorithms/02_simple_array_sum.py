#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    # Calcula a soma dos elementos do array
    return sum(ar)

if __name__ == '__main__':
    # Lê o tamanho do array (não é utilizado no cálculo da soma)
    ar_count = int(input().strip())

    # Lê os elementos do array e os converte para uma lista de inteiros
    ar = list(map(int, input().rstrip().split()))

    # Chama a função para calcular a soma
    result = simpleArraySum(ar)

    # Escreve o resultado no arquivo output.txt
    with open('output.txt', 'w') as fptr:
        fptr.write(str(result) + '\n')

