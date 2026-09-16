#Día 6 - Tuplas

#Ejercicios nivel 1

#Ejercicio 1

tupla = ()

#Ejercicio 2 

hermanos = ('Jesús', 'Javier', 'Carlos')
hermanas = ('Carmen', 'Sandra', 'Julia')

#Ejercicio 3

familia = hermanos + hermanas
print(familia)

#Ejercicio 4

print(len(familia))

#Ejercicio 5

padres = ('Papa','Mama')
miembros_familia = padres + familia

print(miembros_familia)

#Ejercicios nivel 2

#Ejercicio 1

hermanos = miembros_familia[2:]
padres = miembros_familia[:2]

print(hermanos)
print(padres)

#Ejercicio 2

frutas = ('Naranja', 'Kiwi', 'Banana')
vegetales = ('Brocoli', 'Pimiento', 'Cebolla')
productos_animales = ('Carne', 'Huevos', 'Leche')

cosas_comida = frutas + vegetales + productos_animales

print(productos_animales)

#Ejercicio 3

cosas_comida = list(cosas_comida)

#Ejercicio 4

medio = cosas_comida[3:-3]

print(medio)

#Ejercicio 5

principio = cosas_comida[0:3]
final = cosas_comida[-3:]

#Ejercicio 6

cosas_comida = tuple(cosas_comida)

del cosas_comida

#Ejercicio 7

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
