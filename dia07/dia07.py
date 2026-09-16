#Día 7 de 30 dias de Python

#Ejercicios Nivel 1

#Ejercicio 1

# Conjuntos
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

#Ejercicio 2

it_companies.add('Twitter')
print(it_companies)

#Ejercicio 3

it_companies.update(['Empresa 1', 'Empresa 2', 'Empresa 3'])
print(it_companies)

#Ejercicio 4

it_companies.remove('Empresa 3')
print(it_companies)

#Ejercicio 5

respuesta = ('Discard no devuelve un error si el elemento que que intentas borrar no está en el conjunto')

#Ejercicios Nivel 2

#Ejercicio 1

C = A.union(B)
print(C)

#Ejercicio 2

C = A.intersection(B)
print(C)

#Ejercicio 3

print(A.issubset(B))

#Ejercicio 4

print(A.isdisjoint(B))

#Ejercicio 5

C = A.union(B)
D = B.union(A)

print(C)
print(D)

#Ejercicio 6

C = A.symmetric_difference(B)

print(C)

#Ejercicio 7

del A

#Ejercicios Nivel 3

#Ejercicio 1

age = [22, 19, 24, 25, 26, 24, 25, 24]

set_age = set(age)

print(len(age) > len(set_age))

#Ejercicio 2

#cadenas y listas son mutables y tuplas y sets no. 

#Ejercicio 3

frase = 'Soy profesor, profesor, me me gusta motivar motivar y enseñar a las personas'

lista = set(frase.split())

print(len(lista))