from sre_constants import RANGE
from tokenize import Number

def multiplication_table(number):
    # TODO: use o for para retorna uma lista com a tabuada do number selecionado pelo usuário
    # Exemplo: number = 3 deve retorna [3,6,9,12,15,18,21,24,27,30]
    lista=[]
    for n in range(10):
        if n<=10:
            lista.append(number*(n+1))
            n= n + 1
            print(lista)
    return lista

def other_multiplication_table(number):
    # TODO: use o while para retorna uma lista com a tabuada do number selecionado pelo usuário
    # Exemplo: number = 3 deve retorna [3,6,9,12,15,18,21,24,27,30]
    n=0
    lista=[]
    while n <=9 :
        lista.insert(n,number*(n+1))
        n= n + 1
    return lista


