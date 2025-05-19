#EJERCICIO 1 if / else / elif

"""
A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:
Menos de 160 cm: Base
Entre 160 cm y 179 cm: Escolta
Entre 180 cm y 199 cm: Alero
200 cm o más: Ala-Pívot o Pívot

"""

altura = float(input("Ingresa la altura en centimeros: "))

if altura < 160:
    print("Tu posicion es BASE")
elif 160 <= altura <= 179:
    print("Tu posicion es ESCOLTA")
elif 180 <= altura <= 199:
    print("Tu posicion es ALERO")
else:
    print("Tu posicion es PIVOT")

#EJERCICIO 2 if / else / elif

"""
Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
4 y 5            ---> Aprobado, la nota es ...
1, 2 y 3         ---> Desaprobado, la nota es ...

"""
nota = float(input("Ingresa la nota del estudiante: "))

if nota < 4:
    print("Desaprobado, la nota es: ", nota)
elif 4 <= nota <= 5:
    print("Aprobado, la nota es: ", nota)
else:
    print("Promoción directa, la nota es ", nota)

"""
Ejercicio en clase 04:
Escribi un programa en Python que le pida al usuario ingresar su edad
Si la edad es menor a 0 o mayor a 120, mostrar un mensaje que diga Edad Invalida
Si la edad es menor a 13, mostrar Acceso denegado. Debes tener al menos 13 años para entrar"
Si la edad está entre 13 y 17 inclusive, mostrar acceso restringido. Estás en modo adolescente
Si la edad es 18 o más, mostrar Acceso completo concedido

"""
edad = int(input("Ingresa tu edad: "))


if 0 > edad or edad > 120:
    print("Edad Invalida")
elif edad < 13:
    print("Acceso denegado")
elif 13 <= edad <= 17:
    print("Acceso restringido; estas en modo adolescente")
else:
    print("Acceso completo concedido")

