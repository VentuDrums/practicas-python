#Estos  son los ejercicios del día 3 de 30 dias con python

edad = int(30)
altura = float(1,78)
complex = complex(1 + 1j)

#script que pide base y altura de un triangulo y calcula su area

base = input("Base: ")
altura = input("Altura: ")

area_triangulo = 0.5 * (int(base) * int(altura))

print("La base del triangulo es " + str(base) +", la altura del triangulo es " + str(altura) + 
"."  +  "Por lo que el area del triangulo es " + str(area_triangulo))

#script que pide lados de un triangulo y calcula el perimetro

lado_a = input("Lado A:")
lado_b = input("Lado  B:")
lado_c = input("Lado C:")

perimetro = int(lado_a) + int(lado_b) + int(lado_c)

print("El lado A es " + str(lado_a) + ", el lado B es " + str(lado_b) 
+ " y el lado C es " + str(lado_c) + ". Por lo que el perímetro es: " + str(perimetro))

#scrip que pide longitud y anchura de un rectangulo y calcula area y perímetro

largo = int(input("¿Cuánto mide de largo?"))
ancho = int(input("¿Cuánto mide de ancho?"))

area_rectangulo = largo * ancho
perimetro = 2*(largo+ancho)

print("El area del rectágulo es " + str(area_rectangulo) + " y su perimetro es " 
+ str(perimetro))

#script que pide radio de un círculo y calcula su area y su circunferencia

import math

radio = float(input("Radio del círculo: "))

area = math.pi * (radio**2)
circun = 2 * math.pi * radio

print("El area del triangulo es " + str(area) + "  y la ciircunferencia es "  + str(circun))

#ejercicio 8  - calcular pendiente, intersección de X e intersección de Y

m = 2
b = -2

#y = m*x - b

pendiente = m
inter_y = m*0 + b
inter_x = -b/m

print(pendiente)
print(inter_x)
print(inter_y)

#ejercicio 9 - pendiente y distancia euclidea

x1, x2, y1, y2 = 2, 6, 2, 10

pendiente = (y2 - y1) / (x2 - x1)

distancia_euclidia = (((x2-x1)**2)+((y2-y1)**2))**0.5

print(pendiente)
print(distancia_euclidia)

#ejercicio 10 - compara las pendientes del ejercicio 8 y 9

print(m==pendiente)

#ejercicio 11 - y = x^2 + 6x + 9

x = 10
y = x**2 + 6*x + 9


print(y)

for  x in range(-5,5):
    y=x**2+6*x+9
    print(x,y)

#ejercicio 12 - longitud de python y dragon

x = "python"
y = "dragon"

print(len(x)==len(y))

#ejercicio 13 - and con python y dragon

x = "python"
y = "dragon"

print("on" in x and "on" in y)

#ejercicio 14 - palabra en frase

phrase = "I hope this course is not full of jargon"
word = "jargon"

print(word in phrase)

#ejercicio 15 - ni 'dragon' ni 'python' contienen 'on'

x = "dragon"
y = "python"

print("on" in x or "on"in y)

#ejercicio 16 - Encuentra la longitud de 'python', conviértela a float y luego a string.

x = len("python")

x = float(x)
print(type(x))

x = str(x)
print(type(x))

#ejercicio 17 - ¿Es este número par o impar?

numero = int(input("introduce un número: "))

if numero % 2 == 0:
    print("Es par")
else:
    print("Es impar")

#ejercicio 18 - Comprueba si la división entera de 7 entre 3 es igual al valor entero de 2.7

print(int(7/3) == int(2.7))

#ejercicio 19 - Comprueba si el tipo de '10' es igual al tipo de 10.

x = "10"
y = 10

print(type(x) == type(y))

#ejercicio 20 - Comprueba si int('9.8') es igual a 10.

print(int("9.8") == 10) #error porque no se puede convertir a entero una cadena con punto

#ejercicio 21 -  Escribe un script que solicite las horas trabajadas y 
#la tarifa por hora al usuario y calcule el salario.

horas = int(input("Horas trabajadas"))
precio_hora = int(input("¿Cuanto cobras la hora?"))

salario = horas*precio_hora

print("Vas a cobrar", salario)

#Ejercicio 22 - Script de segundos vividos

edad = int(input("¿Cuántos  años tienes?"))

segundos = edad * 365 * 24 * 3600

print("Has vivido", segundos, "segundos")

#ejercicio 23 - tabla

n = 1
print(n**0, n**1, n**2, n**3, n**4)
n = 2
print(n**0, n**1, n**2, n**3, n**4)
n = 3
print(n**0, n**1, n**2, n**3, n**4)
n = 4
print(n**0, n**1, n**2, n**3, n**4)
n = 5
print(n**0, n**1, n**2, n**3, n**4)