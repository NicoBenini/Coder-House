def dividir(a, b):
    if b == 0:
        return None
    else:
        return a / b


print(dividir(4, 2) == 2)
print(dividir(9, 3) == 3)
print(dividir(2, 4) == 0.5)
print(dividir(0, 8) == 0)
print(dividir(8, 0) == None)
print(dividir(-1, 0) == None)
print(dividir(99, 0) == None)