#frutas = ["manzana", "banana", "naranja", "pera", "uva"]

#for i in frutas:
#    print("fruta actual:", i)

#Ejercicio 1 FOR


#1) Mostrar los números ascendentes desde el 1 al 10
#for i in range(1, 11):
#    print(i)

#2) Mostrar los números descendentes desde el 10 al 1
#for i in range(10, 0, -1):
#    print(i)

#3) Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.
#numero = int(input("Ingresa un numero: "))
#for i in range(0, numero + 1):
#    print(i)

#4) Ingresar un número y mostrar la tabla de multiplicar de ese número. Por ejemplo si se ingresa el numero 5:

#	5 x 0 = 0
#	5 x 1  = 5
#	5 x 2 = 10
#	5 x 3  = 15

#num = int(input("\nIngresa un numero: "))
#print(f"\nTabla de multiplicación de {num}: \n")

#for i in range(1, 11):
#    resultado = num * i
#    print(f"{num} x {i} = {resultado}")

#5) Se ingresan un máximo de 10 números o hasta que el usuario ingrese
# el número 0. Mostrar la suma y el promedio de todos los números.

#suma = 0 # Variable para acumular la suma total
#contador = 0 # Variable para contar cuántos números hemos ingresado

#print("Ingrese hasta 10 números (0 para terminar):")

#for _ in range(10): # El _ significa que no usaremos el valor del contador del bucle
#    num = float(input("-")) #para mayor prolijidad
#    if num == 0: 
#        break  # Si el número es 0, salimos del bucle inmediatamente
#    suma += num # Sumamos el número al total acumulado
#    contador += 1 # Incrementamos el contador de números válidos

#if contador > 0:
#    promedio = suma / contador
#    print(f"\nSuma total: {suma}")
#    print(f"Promedio: {promedio}")
#else:
#    print("\nNo se ingresaron números") 


#6) Imprimir los números múltiplos de 3 entre el 1 y el 10.

#print("Múltiplos de 3 entre 1 y 10:")
#for numero in range(1, 11):  # range(1, 11) genera números del 1 al 10
#    if numero % 3 == 0:       # Si el residuo de dividir entre 3 es 0, es múltiplo
#        print(numero)

# Alternativa usando paso en range()
#print("Múltiplos de 3 entre 1 y 10:")
#for numero in range(3, 11, 3):  # Comienza en 3, hasta 10, en pasos de 3
#    print(numero)


#7) Mostrar los números pares que hay desde la unidad hasta el número 50

#print("Números pares de la unidad hasta el 50")

#for num_par in range(2, 51, 2):
#    print(num_par)

