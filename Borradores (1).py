# borrador

lista = list(range(0, 10))
print(lista)
numero = int(input("Escriba un número entre 0 y 9: "))


while numero > 9 or numero < 0: 
    numero = int(input("Escriba un número entre 0 y 9: "))
    
else:
    print("Ok")
 
if (numero in lista) == True:
    print("El número esta en la lista")
else: print("El número no esta en la lista")
    
    
print("termine")    


nombre = "Nicolas"
edad = 31 

print(f"mi nombre es {nombre} y mi edad es {edad}")
