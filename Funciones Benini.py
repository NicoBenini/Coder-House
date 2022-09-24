#Ejercicio 1
def area_rectangulo(base, altura):
    resultado = base * altura 
    return resultado
area_rectangulo(15, 10)

#Ejercicio 2
import math

def area_circulo(radio):
    resultado = ((radio ** 2) * math.pi)  
    return resultado
area_circulo(5)

#Ejercicio 3
def relacion(primer_numero, segundo_numero):
    if primer_numero > segundo_numero:
        return 1
    elif primer_numero < segundo_numero:
        return -1
    else:
        return 0
      
    
test1 = relacion(5, 10)
print(test1)   

test2 = relacion(10, 5) 
print(test2)
 
test3 = relacion(5, 5)
print(test3)

#Ejercicio 4
def intermedio(primer_numero, segundo_numero):
    resultado = (primer_numero + segundo_numero) / 2
    return resultado
       
intermedio(-12, 24)

#Ejercicio 5
def recortar(numero_a_recortar, limite_inferior , limite_superior):
    if numero_a_recortar < limite_inferior:
        return limite_inferior
    elif numero_a_recortar > limite_superior:
        return limite_superior
    else:
        return numero_a_recortar

recortar(15, 0, 10)

#Ejercicio 6
def separar(lista):
    lista.sort()
    lista_pares = []
    lista_impares = []
    for valor in lista:
        if valor %2 == 0:
            lista_pares =lista_pares + [valor]
            
        else:
            lista_impares = lista_impares + [valor]
            
    
    return lista_pares, lista_impares

pares, impares = separar([6,5,2,1,7])

print("Pares: ", pares)
print("Impares: ", impares)