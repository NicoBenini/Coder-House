#funcion año bisiesto entregable
def año_bisiesto(year):  # year es año en inglés
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False
year = input("Ingrese año: ")
if year.isdigit():
    es_bisiesto = año_bisiesto(int(year))
    if es_bisiesto == True:
        print(f"El año {year} es bisiesto")
    else:
        print(f"El año {year} no es bisiesto")
else:
    print("ingrese un numero por favor")
## 1988 es bisiesto 
#es_bisiesto = año_bisiesto(1988)
#if es_bisiesto == True:
#    print("correcto")
#else:
#    print("incorrecto")
## 400 es bisiesto (porque 400 es multiplo de 400)
#es_bisiesto = año_bisiesto(400)
#if es_bisiesto == True:
#    print("correcto")
#else:
#   print("incorrecto")
## 100 no es bisiesto
#es_bisiesto = año_bisiesto(100)
#if es_bisiesto == False:
#    print("correcto")
#else:
#    print("incorrecto")
## 2012 es bisiesto,
#es_bisiesto = año_bisiesto(2012)
#if es_bisiesto == True:
#    print("correcto")
#else:
#    print("incorrecto")
## 2010 no es bisiesto, 
#es_bisiesto = año_bisiesto(2010)
#if es_bisiesto == False:
#    print("correcto")
#else:
#    print("incorrecto")
## 2000 es bisiesto,
#es_bisiesto = año_bisiesto(2000)
#if es_bisiesto == True:
#    print("correcto")
#else:
#    print("incorrecto")
## 1900 no es bisiesto.
#es_bisiesto = año_bisiesto(1900)
#if es_bisiesto == False:
#    print("correcto")
#else:
#    print("incorrecto")