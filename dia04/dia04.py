#Día 4 de 3º days of Python

#Ejercicio 1: Concatenar cadenas

c1 = 'Thirty'
c2 = 'Days'
c3 = 'Of'
c4 = 'Python'

name = c1 + ' ' + c2 + ' ' + c3 + ' ' + c4
print(name)
print(type(name))

#Ejercicio 2: Une las cadenas 'Coding', 'For', 'All' en 'Coding For All'.

c1 = 'Coding'
c2 = 'For'
c3 = 'All'

name = c1 + ' ' + c2 + ' ' + c3
print(name)

#Ejercicio 3: Declara la variable company y asígnale el valor inicial "Coding For All".

company = 'Coding For All'

#Ejercicio 4: Imprime la variable company usando print().

print(company)

#Ejercicio 5: Imprime la longitud de la variable company usando la función len() y print().

print(len(company))

#Ejercicio 6: Cambia todos los caracteres de la variable company a mayúsculas usando el método upper().

print(company.upper())

#Ejercicio 7: Cambia todos los caracteres de la variable company a minúsculas usando el método lower().

print(company.lower())

#Ejercicio 8: Usa el método capitalize() para que la variable company solo tenga la primera letra en mayúscula.

print(company.capitalize())
print(company.title())
print(company.swapcase())

#Ejercicio 9: Corta (slice) la variable company desde el primer carácter hasta el carácter 6.

print(company[0:6])

#Ejercicio 10: Usa index, find u otros métodos para comprobar si la cadena 'Coding For All' contiene la palabra 'Coding'.

sub_string = 'Coding'

print(company.index(sub_string))
print(company.find(sub_string))

#Ejercicio 11: Reemplaza la palabra 'Coding' por 'Python' en 'Coding For All'.

frase = 'Coding For All'
frase_modificada = frase.replace('Coding','Python')
print(frase_modificada)

#Ejercicio 12: Reemplaza 'Python for Everyone' por 'Python for All' (usa replace() u otro método).

frase = 'Python for Everyone'
frase_modificada = frase.replace('Everyone','All')
print(frase_modificada)

#Ejercicio 13: Separa la cadena 'Coding For All' usando espacios como separador.

frase = 'Coding For All'
separado = frase.split((' '))
print(separado)

#Ejercicio 14: Divide la cadena 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon' por las comas.

empresas = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
separado = empresas.split(', ')
print(separado)

#Ejercicio 15: ¿Qué carácter está en el índice 0 de 'Coding For All'?

frase = 'Coding For All'
first_character = frase[0]
print(first_character)

#Ejercicio 16: ¿Cuál es el índice del último carácter de 'Coding For All'?

frase = 'Coding For All'
last_character = frase[-1]
print(last_character)

#Ejercicio 17: ¿Qué carácter está en el índice 10 de 'Coding For All'?

frase = 'Coding For All'
character10 = frase[10]
print(character10)

#Ejercicio 18: Crea una sigla (acrónimo) a partir de 'Python For Everyone'.

frase = 'Python For Everyone'
let1 = frase[0]
let2 = frase[7]
let3 = frase[11]
siglas = let1 + let2 + let3
print(siglas.upper())

#Ejercicio 19: Crea una sigla a partir de 'Coding For All'

frase = 'Coding For All'
palabras = frase.split()
siglas = palabras[0][0] + palabras[1][0] + palabras [2][0]  #Mejor método para siglas

print(siglas.upper())

#Ejercicio 20: Usando index, determina la primera aparición de la letra 'C' en 'Coding For All'.

frase = 'Coding For All'
print(frase.index('C'))

#Ejercicio 21: Usando index, determina la primera aparición de la letra 'F' en 'Coding For All'.

frase = 'Coding For All'
print(frase.index('F'))

#Ejercicio 22: Usa rfind para determinar la última aparición de 'l' en 'Coding For All People'.

frase = 'Coding For All People'
print(frase.rfind('l'))

#Ejercicio 23: Usa index o find para encontrar la primera aparición de la palabra 'because' en: 'You cannot end a sentence with because because because is a conjunction'

frase = 'You cannot end a sentence with because because because is a conjunction'
print(frase.find('because'))
print(frase.index('because'))

#Ejercicio 24: Usa rindex para encontrar la última aparición de la palabra 'because' en: 'You cannot end a sentence with because because because is a conjunction'.

frase = 'You cannot end a sentence with because because because is a conjunction'
print(frase.rindex('because'))

#Ejercicio 25: Elimina la frase 'because because because' de: 'You cannot end a sentence with because because because is a conjunction'.

frase = 'You cannot end a sentence with because because because is a conjunction'
limpia = frase.replace('because because because ', '')
print(limpia)

#Ejercicio 26: Encuentra la primera aparición de la palabra 'because' en: 'You cannot end a sentence with because because because is a conjunction'.

frase = 'You cannot end a sentence with because because because is a conjunction'
print(frase.find('because'))

#Ejercicio 27: Elimina la frase 'because because because' de la oración anterior.

frase = 'You cannot end a sentence with because because because is a conjunction'
limpia = frase.replace('because because because ', '')
print(limpia)

#Ejercicio 28: ¿La cadena 'Coding For All' empieza con la subcadena 'Coding'?

frase = 'Coding For All'
palabra = 'Coding'

print(frase.startswith(palabra))

#Ejercicio 29: ¿La cadena 'Coding For All' termina con la subcadena 'coding'?

frase = 'Coding For All'
palabra = 'coding'

print(frase.endswith(palabra))

#Ejercicio 30: Elimina los espacios en blanco a la izquierda y derecha de la cadena '   Coding For All      '.

frase = '   Coding For All      '
print(frase[3:-6])

#Ejercicio 31: Usando isidentifier(), ¿cuál de las siguientes devuelve True? -30DaysOfPython -thirty_days_of_python

frase1 = '30DaysOfPython'
frase2 = 'thirty_days_of_python'

print(frase1.isidentifier())
print(frase2.isidentifier())

#Ejercicio 32: Dada la lista ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'], únela en una cadena separada por espacios.

lista = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
separado = ' '.join(lista)

print(separado)

#Ejercicio 33: Usa la secuencia de escape de nueva línea para separar las siguientes oraciones.

frase = 'I am enjoying this challenge.\nI just wonder what is next.'

print(frase)

#Ejercicio 34: Usa la secuencia de tabulación para mostrar:

tabla = 'Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki'
print(tabla)

#Ejercicio 35: Usa un método de formateo de cadenas para imprimir:

radio = 10
area = 3.14 * (radio**2)
frase = 'El area de un círculo con radio {} es {} metros cuadrados.'.format(int(radio), int(area))

print(frase)

#Ejercicio 36: Usa un método de formateo de cadenas para imprimir:

a = 8
b = 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.5f}'.format(a, b, a / b)) # limitar a dos decimales
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))