#Día 2: 30 días de programación en python

#Ejercicios nivel 1

nombre = "Carlos"
apellido = "Ventura"
pais = "España"
ciudad = "Ablitas"
edad = 33
año = 1993
es_casado = False
is_true = True
is_light_on = False
familia = ["Carlos", "Jesús", "MªCarmen", "Alexandra"]

#Ejercicios nivel 2

#funcion type() -  ejercicio 1

print(type(nombre))
print(type(apellido))
print(type(pais))
print(type(ciudad))
print(type(edad))
print(type(año))
print(type(es_casado))
print(type(is_true))
print(type(is_light_on))
print(type(familia))

#funcion len() - ejercicio 2

print(len(nombre))

#ejercicio 3

len(nombre) == len(apellido)

#operaciones con variables -  ejercicio 4

num_one = 5
num_two = 4

total = (num_one+num_two)
diff = (num_one-num_two)
product = (num_one+num_two)
division = (num_one/num_two)
remainder = (num_two%num_one)
exp = (num_one++num_two)
floor_division = (num_one//num_two)

#Ejercicio círculo - ejercicio 5

radio = 30

_area_of_circle_ = math.pi*(radio**2)
_circum_of_circle_ = 2*math.pi*radio

import math

radio = float(input("Inserte radio:"))

_area_of_circle_ = math.pi*(radio**2)

#Ejercicio 6

nombre = input("¿Cual es tu nombre?")
apellido = input("¿Cómo  te apellidas?")
pais = input("¿De  quépaís eres?")
edad = input("¿Cuántos años tienes?")

#Ejercicio 7 

help("keywords")