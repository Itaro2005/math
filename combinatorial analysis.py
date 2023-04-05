import math
p = p
def fatorial(n):
    valor = 1
    for i in range(1, n+1):
        valor *= i
    return valor

pfatorial = fatorial(p)
nfatorial = fatorial(n)
pmenosn = n-p
pmenosnfatorial = fatorial(pmenosn)
denominador = pfatorial*pmenosnfatorial

Cnp = nfatorial/denominador
print(Cnp)