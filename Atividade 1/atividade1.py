#Questão 1 - soma de elementos

entrada1 = [1,2,3,4]

x = sum(entrada1)

print(x)

#Questão 3 - Maior número

maiornum = [3,7,2,9,5]

maior = max(maiornum)

print(maior)

#Questão 5 - Soma dos pares

somadospares = [1,2,3,4,5,6]
pares=[]

for i in somadospares:
    if i%2==0:
        pares.append(i)
somadosparesx = sum(pares)

print(somadosparesx)

#Questão 7 - Inverter lista

listanormal = [1,2,3,4]

invertido = listanormal[::-1]

print(invertido)

#Questão 9 - Soma de positivos

listacompleta = [-1,2,-3,4,5]
positivos = []

for i in listacompleta:
    if i>0:
        positivos.append(i)

somadospositivos = sum(positivos)

print(somadospositivos)

#Questão 11 - Contagem de vogais


def count_vogais(n):
    vogais = set('aeiou')
    count = 0
    for char in n.lower():
        if char in vogais:
            count += 1
    return count

palavras = "Programacao"

vgs= count_vogais(palavras)

print(vgs)

#Questão 13 - Verificar Palíndromo

words = "arara"
inverterword1 = words[::-1]
words2 = "casa"
inverterword2 = words2[::-1]

if inverterword1 == words:
    print(f"Verdadeiro")
else: print("Falso")

if inverterword2 == words2:
    print(f"Verdadeiro")
else: print("Falso")


#Questão 15 - Trocar caracteres

palavraorign = "banana"
c1 = "a"
c2 = "o"
trocada= ""
for i in palavraorign:
    if i!=c1:
        trocada+=i
    else:
        trocada+=c2

print(trocada)

#Questão 17 - Apagar espaços 

espaco = "ola mundo"
final= ""
for i in espaco:
    if i != " ":
        final+=i

print(final)

p = 'python'

print(p[0])