#Día 9 de 30 días de python

#Ejercicios nivel 1

#Ejercicio 1

user_age = int(input('Introduce tu edad: '))

if user_age >= 18:
    print('Ya tienes la edad suficiente para aprender a conducir')
else:
    print('Aún tienes que esperar ' + str(18 - user_age) + ' años')

#Ejercicio 2

my_age = 33
your_age = int(input('Introduce tu edad: '))

if my_age < your_age:
    if int(your_age - my_age) > 1:
        print('Tienes ' + str(your_age - my_age) + ' años más que yo.')
    elif int(your_age - my_age) == 1:
        print('Tienes un año más que yo.')
    else:
        print('Tenemos la misma edad')
else:
    if int(my_age - your_age) > 1:
        print('Tengo ' + str(my_age - your_age) + ' años más que tu.')
    elif int(my_age - your_age) == 1:
        print('Tengo un año más que tu.')
    else:
        print('Tenemos la misma edad')

#Ejercicio 3

a = int(input('Introduce el primer número: '))
b = int(input('Introduce el segundo número: '))

if a > b:
    print(str(a) + ' es mayor que ' + str(b))
elif a < b:
    print(str(a) + ' es menor que ' + str(b))
else:
    print('Los números son iguales')

#Ejercicios nivel 2

#Ejercicio 1

nota = int(input('¿Qué nota has sacado? '))

if nota >= 70:
    if nota >= 80:
        print('Tu nota es A')
    else:
        print('Tu nota es B')
elif nota >= 50:
    if nota >= 60:
        print('Tu nota es C')
    else:
        print('Tu nota es D')
else:
    print('Tu nota es F tontolculo')

#Ejercicio 2

mes = input('¿En qué mes estamos? ').lower()
otoño = ['septiembre', 'octubre', 'noviembre']
invierno = ['diciembre', 'enero', 'febrero']
primavera = ['marzo', 'abril', 'mayo']
verano = ['junio', 'julio', 'agosto']

if mes in otoño:
    print('Estamos en otoño')
elif mes in invierno:
    print('Estamos en invierno')
elif mes in primavera:
    print('Estamos en primavera')
elif mes in verano:
    print('Estamos en verano')
else:
    print('Introduce un mes válido')

#Ejercicio 3

user_fruta = input('Introduce una fruta: ').lower()
frutas = ['banana', 'naranja', 'mango', 'limon']

if user_fruta in frutas:
    print('La fruta ya está en la lista')
else:
    frutas.append(user_fruta)
    print(frutas)

#Ejercicios nivel 3

#Ejercicio 1

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finlandia',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Calle Espacial',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    print(person['skills'][2])
else:
    print('No existe skills')

#Ejercicio 2

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finlandia',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Calle Espacial',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    print('Python' in 'skills')

#Ejercicio 3

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finlandia',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Calle Espacial',
        'zipcode': '02210'
    }
}

titulos = {
    'frontend': ['JavaScript', 'React'],
    'backend': ['Node', 'Python', 'MongoDB'],
    'full_stack': ['React', 'Node', 'MongoDB']
}

if set(titulos['full_stack']).issubset(set(person['skills'])):
    print('Es desarrollador full stack')
elif set(titulos['backend']).issubset(set(person['skills'])):
    print('Es desarrollador backend')
elif set(titulos['frontend']).issubset(set(person['skills'])):
    print('Es desarrollador frontend')
else:
    print('Este no sabe ni sumar')

#Ejercicio 4

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finlandia',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Calle Espacial',
        'zipcode': '02210'
    }
}

if person['is_married'] == True and person['country'] == 'Finlandia':
    print('Asabeneh Yetayeh vive en Finlandia. Está casado.')