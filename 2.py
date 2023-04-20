
"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado
 pertence ou não a sequência.



IMPORTANTE:

Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
"""

valor = int(input('Insira um valor: '))
lista_f = [0]
n = 1
m=0

p = lista_f[len(lista_f)-1]
q = lista_f[len(lista_f)-2]

while True:
    while len(lista_f) < 3:
        lista_f.append(n)
    m = lista_f[len(lista_f)-1] + lista_f[len(lista_f)-2]
    lista_f.append(m)


    if len(lista_f) > 100:
        break
print(lista_f)
if valor in lista_f:
    print(f' O valor {valor} está na lista de sequência de Fibonacci')
else:
    print(f' O valor {valor}  NÃO está na lista de sequência de Fibonacci')