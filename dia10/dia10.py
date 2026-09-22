#DÍA 10 DE 30 DIAS DE PYTHON

#Ejercicios  nivel 1

#Ejercicio 1

number = 0

while number != 11:
    print(number)
    number = number + 1

numbers = [0,  1, 2, 3, 4, 5,  6,  7, 8, 9, 10]

for number in numbers:
    print(number)

#Ejercicio 2

number = 10

while number >= 0:
    print(number)
    number = number - 1

number = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

for number in number:
    print(number)

#Ejercicio 3

hash = '#'

while len(hash) != 8:
    print(hash)
    hash = hash + '#'

#Ejercicio 4

for fila in range(8):
    for columna in range(8):
        print("#", end=" ")
    print()

#Ejercicio 5

number = 0

while number !=11:
    print(str(number) + ' X ' + str(number) + ' = ' + str(number**2))
    number = number + 1


#Ejercicio 6

lst = ['Python', 'Numpy','Pandas','Django', 'Flask']

for element in lst:
    print(element)

#Ejercicio 7

lista = range(101)

for  num in lista:
    if num %2 == 0 and num /2 != 0:
        print(num)

#Ejercicio 8

lista = range(101)

for  num in lista:
    if num %2 != 0 and num /2 != 0:
        print(num)

#Ejercicios nivel 2

#Ejercicio  1

suma = 0

for num in range(101):
    suma = suma + num
    
print('The sum  of al  number  is  ' + str(suma))

#Ejercicio 2

par = 0
impar = 0

for num  in range(101):
    if num %2 == 0:
        par = par + num
    else:
        impar = impar + num

print('The sum of all odd numbers is ' + str(impar) +  '. And the sum of all even numbers is ' + str(par))

#Ejercicios nivel 3

#Ejercicio 1

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]

for country in countries:
    if 'land' in country:
        print(country)

#Ejercicio 2

fruits = ['banana',  'orange', 'mango', 'lemon']

for fruit in fruits:
    print(fruit