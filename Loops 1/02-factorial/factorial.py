def factorial(number):
    # TODO: criar uma função que deve retornar o fatorial de number
    # Lembrando que o fatorial de um número natural n é calculado por n! = n*(n-1)*(n-2)*....*3*2*1
    # Exemplo: fatorial de 4 é calculado por 4! = 4*3*2*1
    # Dica: use laço de repetição


    for n in range(number-1):
        number=number*(n+1)
    return (number)

