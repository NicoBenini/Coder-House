#ejercicio 1
from re import X


def hola_mundo(texto):
    return print(texto)

hola_mundo("hola mundo")

#ejercicio 2
def suma():
    mi_numero = 10
    mi_numero_2 = 20
    suma = mi_numero + mi_numero_2
    return print(f"La suma es: {suma}") #f"fuera de la funcion vale: {mi_variable}"

suma()

#Ejercicio 3
def devuelve_el_tipo_de_dato(dato):
    tipo_de_dato = type(dato)
    if tipo_de_dato == str:
        tipo_de_dato = "Esto es texto"
    elif tipo_de_dato == int:
        tipo_de_dato = "Esto es número"
    elif tipo_de_dato == bool:
        tipo_de_dato = "Esto es un boleano"
    elif tipo_de_dato == tuple:
        tipo_de_dato = "Esto es una tupla"
    elif tipo_de_dato == list:
        tipo_de_dato = "Esto es una lista"
    elif tipo_de_dato == dict:
        tipo_de_dato = "Esto es un diccionario"
    else:
        tipo_de_dato = "No se que tipo de dato es"
    return print(f"He recibido como parámetro: {tipo_de_dato}")

devuelve_el_tipo_de_dato(dict())

#Ejercicio 4

def mi_funcion (a , b):
    x = a + b
    return print(x)
mi_funcion(5 , 8)
mi_funcion("hola" , " mundo")

#ejercicio 5 y 6
def mi_funcion_par_o_impar(numero):
    if type(numero) != int:
        return print(f"Argumento incorrecto: {type(numero)}")
    elif numero % 2 == 0:
        return print(f"El numero {numero} es par")
    elif numero % 2 == 1:
        return print(f"El número {numero} es impar")
    
mi_funcion_par_o_impar("m")

#Ejercicio 7
def mi_funcion_str(un_valor, otro_valor):
    if type(un_valor) == str or type (otro_valor) == str:
        mi_lista = (list(un_valor.upper() + otro_valor.upper()))
        
        return print(mi_lista)
    else:
        return print("El resultado es: False")
   
mi_funcion_str("nico", "hola")

#Ejercicio 8 y 9
def mi_funcion_str_matusculas_largo(un_texto):
    if type(un_texto) == str:
        if len(un_texto) > 10:
            return print(un_texto.upper())
        elif len(un_texto) % 2 == 0:
            return print(list(un_texto))
        elif len(un_texto) % 2 == 1:
            return print(len(un_texto))
    else:
        print("Ingrese un texto por favor")

mi_funcion_str_matusculas_largo("hola")
mi_funcion_str_matusculas_largo("Nicolas")
mi_funcion_str_matusculas_largo("87")
mi_funcion_str_matusculas_largo(942)
mi_funcion_str_matusculas_largo("ddddddddddd")
mi_funcion_str_matusculas_largo("kkkkkkkkkk")