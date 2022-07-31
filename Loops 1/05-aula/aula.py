from cgi import print_arguments
from pickle import APPEND
from pickletools import uint1


def approved_alunes():
    # TODO: use o dicionário abaixo para criar uma função que retorne a quantidade de alunes aprovados
    # Considere que a média é 70
    # Dica: use laço de repetição e condicionais
    alunes = {'Tulio':80,
              'Laercio':20,
              'Ana':50,
              'Rafaela':90,
              'Fernando':91,
              'Jones':10}
    nomes = alunes.keys()
    nomes = list(nomes)
    u = 0
    for i in nomes:
        if alunes[i] >= 70:
            u = u + 1
    return u




def approved_alunes_names():
    # TODO: use o dicionário abaixo para criar uma função que retorne a quantidade de alunes aprovados
    # Considere que a média é 70
    # Dica: use laço de repetição e condicionais
    alunes = {'Tulio':80,
              'Laercio':20,
              'Ana':50,
              'Rafaela':90,
              'Fernando':91,
              'Jones':10}
    nomes=alunes.keys()
    nomes=list(nomes)
    alunes1=[]
    u=0
    for i in nomes:
        if alunes[i]>=70:
            alunes1.append(i)
    return alunes1



def count_letters(string):
    # TODO: crie uma função que conte quantas vezes cada letra aparece na string e
    # retorne um dicionário com a letra como chave e a quantidade como valor
    # Exemplo: string = 'textooo' deve retornar {'e':1, 't':2, 'x':1, 'o':3}
    # Dica: use laço de repetição, condicionais e seus conhecimentos sobre dicionários
    my_dict={}
    lista= set(list(string))
    for v in lista:
        my_dict[v]= string.lower().count(v)
    return(my_dict)

