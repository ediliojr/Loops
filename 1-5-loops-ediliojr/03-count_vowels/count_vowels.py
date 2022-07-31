def count_vowels(string):
    # TODO: a função deve retornar a quantidade de vogais em string
    # Dica: use loop for e condicionais
    # Exemplo: string = 'qualquer texto' deve retornar 6
    lista = ['a','e','i','o','u']
    t=0
    for v in lista:
        n= string.lower().count(v)
        t=n+t
    return t


