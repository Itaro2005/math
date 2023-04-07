import math



def fatorial2(n):
        valor = 1
        for i in range(1, n-1):
            valor *= i
        return valor

valor2 = fatorial2(n)/10


print(valor2)