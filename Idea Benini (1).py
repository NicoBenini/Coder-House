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

# ejercicio 6
print(list(range(0, 11)))
print(list(range(-10, 1)))
print(list(range(0, 22, 2)))
print(list(range(-19, 0, 2)))
print(list(range(0, 51, 5)))