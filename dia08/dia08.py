#Dia 8 de 30 días de  python - Diccionarios

#Ejercicio 1

dog = {}

#Ejercicio 2

cat = {
    'name':'Freya',
    'color':'Tricolor',
    'breed':'Carey',
    'legs':4,
    'age':1,
}

#Ejercicio 3

student = {
    'first_name':'Carlos',
    'last_name':'Ventura',
    'gender':'Male',
    'age':33,
    'marital_status':'Single',
    'skills':['Music', 'Teaching', 'Coding', 'AI'],
    'country':'Spain',
    'city':'Ablitas',
    'address':'Calle San Pancracio 9',
}

#Ejercicio 4

print(len(student))

#Ejercicio 5

print(student['skills'])
print(type(student['skills']))

#Ejercicio 6

student['skills'].append('Drums')

print(student['skills'])

#Ejercicio 7

keys = student.keys()

print(keys)

#Ejercicio 8

values = student.values()

print(values)

#Ejercicio 9

lista_tuplas = student.items()

print(lista_tuplas)

#Ejercicio 10

student.pop('address')
print(student)

#Ejercicio 11

del student

print(student)