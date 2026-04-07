#Questão 1

lista = [4, 8, 6, 2]

def s(lista):
    soma = sum(lista)
    leitura = len(lista)
    media = soma/leitura
    return media

print(s(lista))

#Questão 2

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

print(fatorial(5))

#Questão 3
entrada = "ola mundo cruel estou aqui"
 

def espacos(a): 
    j=1
    for i in entrada: 
        if i == " ":
            j += 1
    return j
print(espacos(entrada))

#Questão 5

lista = [3, 7, 2, 9, 5]
def j(a):
    maior = max(lista)
    w = -9999999
    for i in lista: 
        if i < maior and i > w:
            w = i
    return w 
print(j(lista))

#Questão 6

numero = 1234
soma = sum(int(digito) for digito in str(numero))
print(soma)



