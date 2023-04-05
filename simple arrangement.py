import math
p = p
def fatorial(n):
    valor = 1
    for i in range(1, n+1):
        valor *= i
    return valor
    
pmenosn = fatorial(p-n)    
nfatorial = fatorial(n)
print(nfatorial)


Anp = nfatorial/pmenosn
print(Anp)