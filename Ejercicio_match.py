"""
Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año. 
En caso de hacerlo mostrar por print  el mensaje “Se viaja”, caso contrario mostrar “No se viaja”. 
Si es invierno: solo se viaja a Bariloche.
Si es verano: se viaja a Mar del plata y Cataratas.
Si es otoño: se viaja a todos los lugares.
Si es primavera: se viaja a todos los lugares menos Bariloche.

"""
# Entrada del usuario
viajar = input("¿Desea viajar? (si/no): ")
match viajar:
    case "si":
        estacion = input("¿En qué estación quiere viajar? (invierno/verano/otoño/primavera): ")

        match estacion:
            case "invierno":
                print("Opciones disponibles: Bariloche")
            case "verano":
                print("Opciones disponibles: Mar del plata, Cataratas")
            case "otoño":
                print("Opciones disponibles: Bariloche, Mar del plata, Cataratas")
            case "primavera":
                print("Opciones disponibles: Mar del plata, Cataratas")
            case _:
                print("Estación no válida")
    
    case "no":
        print("No se viaja")

    case _:
        print("Respuesta no válida")
