from asyncio.sslproto import _DO_HANDSHAKE


def selecting_positive(list1, number):
    # TODO: a função deve retornar uma nova lista apenas com os valores maiores que o number
    # Exemplo: list1 = [10,20,30,40,50] e number = 20, a função deve retornar [30,40,50]
    # Dica: use laço de repetição e condicionais

    list2=[]
    i=0
    for i in range(len(list1)):
        if number<list1[i]:
            list2.append(list1[i])
    return (list2)




