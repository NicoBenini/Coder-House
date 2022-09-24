# Desafio entregable clase 4 y 5
#Ejercicio 1
numero1 = int(input("Escriba primer número: "))
numero2 = int(input("Escriba segundo número: "))
que_hacer = input("Escriba una de las 4 operaciones: Suma; Resta; Mulpitlicacion; Salir: ")
if que_hacer == "Suma":
    print(numero1 + numero2)
elif que_hacer == "Resta":
    print(numero1 - numero2)
elif que_hacer == "Multiplicacion":
    print(numero1 * numero2)
elif que_hacer == "Salir":
    print("Salió del sistema")
else:
    print("Opción no correcta")
    
    
print("Terminó")

#Ejercicio 2 numero = input("Escriba un número impar: ")
while int(input("Escriba un número impar: ")) % int(2) == 0:
    numero = input("Escriba un número impar: ")
else:
    print("Gracias")

#Ejercicio 3
print(sum(list(range(1, 100, 2))))


#Opciones_Numero = [1,2,3,4]
#numero = input("escriba un numero entero del 1 al 4: ")
#
#
#
#
#
#
#Chance = 1
#while Chance <=3:
#    txt = input("Escribe SI: ")
#    if txt == "SI":
#        print("Ok, lo conseguiste en el intento", Chance)
#        break
#    Chance += 1
#else:
#    print("Has agotado tus tres intentos") 

#Ejercicio 4
chance = 1
numero_1 = 0
numero_2 = 0
cantidad = int(input("Cuantos numeros quiere introducir: "))
while chance <= cantidad:
    numero_1 = int(input("Intrudicir numero : "))
    chance += 1
    numero_2 += numero_1

print(numero_2 / cantidad)

#ejercicio 5
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


# ejercicio 6
print(list(range(0, 11)))
print(list(range(-10, 1)))
print(list(range(0, 22, 2)))
print(list(range(-19, 0, 2)))
print(list(range(0, 51, 5)))
#ejercicio 6 bis
lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
lista_completa = lista_1 + lista_2
print(lista_completa)
lista_compreta_sin_repetidos = set (lista_completa)
print(lista_compreta_sin_repetidos)