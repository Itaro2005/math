import math
p = 5
n = 8
def fatorial(n):
    valor = 1
    for i in range(1, n+1):
        valor *= i
    return valor

pfatorial = fatorial(p)
numerador = fatorial(n+p-1)
pmenosn = n-p
nmenos1fatorial = fatorial(n-1)
denominador = pfatorial*nmenos1fatorial

Crnp = numerador/denominador
print(Crnp)