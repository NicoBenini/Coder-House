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

# Ejemplo crear y escribir archivo

class Persona:
    
    especie = "Es humano"
    cabeza = "Tiene una cabeza"
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def Hablar(self):
        
        print("Soy una persona y estoy hablando")
    
    def Lo_que_dije(self, digo):
        self.digo = digo
        print(f"Estoy diciendo: {self.digo}")
    

Persona1 = Persona("Nico", 31)
print(Persona.especie)
print(Persona.cabeza)
print(Persona1.nombre)
print(Persona1.edad)
Persona1.Hablar()
Persona1.Lo_que_dije("Esto funciona?")
        
        
    
