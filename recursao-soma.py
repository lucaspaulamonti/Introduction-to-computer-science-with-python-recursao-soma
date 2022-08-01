# Utilize recursão para retornar a soma dos números de uma lista.
def soma_lista(lista):
    result=int()
    if len(lista)>0:
        result+=lista[0]
        del(lista[0])
        result+=soma_lista(lista)
    return result
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!