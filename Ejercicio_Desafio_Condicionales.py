"""
Facturación del Servicio de Agua Potable
El acceso al agua potable es un servicio esencial para hogares, comercios e industrias. Para garantizar un uso eficiente del recurso y establecer una estructura justa de costos, se han definido diferentes tarifas y ajustes según el consumo y el tipo de cliente.
Este sistema de facturación contempla una tarifa base que incluye un cargo fijo y un costo variable por metro cúbico consumido. Además, se aplican bonificaciones y recargos dependiendo del consumo y la categoría del usuario. En algunos casos especiales, también pueden otorgarse descuentos adicionales.
A continuación, se detallan las reglas del sistema de facturación y los cálculos necesarios para determinar el monto final a pagar.
Tarifa base:
Todas las facturas incluyen un cargo fijo de $7000 además del costo por consumo.
El costo por metro cúbico (m³) de agua es de $200/m³.
Bonificaciones y Recargos según tipo de cliente:
Cliente Residencial:
Si el consumo es menor a 30 m³, se aplica una bonificación del 10% sobre el costo del consumo.
Si el consumo supera los 80 m³, se aplica un recargo del 15% sobre el costo del consumo.
Cliente Comercial:
Si el consumo es superior a 150 m³, se aplica una bonificación del 8% sobre el costo del consumo.
Si el consumo supera los 300 m³, la bonificación aumenta al 12%.
Si el consumo es menor a 50 m³, se aplica un recargo del 5%.
Cliente Industrial:
Si el consumo es superior a 500 m³, se aplica una bonificación del 20% sobre el costo del 
consumo.
Si el consumo supera los 1,000 m³, la bonificación aumenta al 30%.

Si el consumo es menor a 200 m³, se aplica un recargo del 10%.
Casos especiales:
Si el cliente es Residencial y el total de la factura sin impuestos ni bonificaciones  es menor a $35000, se aplica un descuento adicional del 5%.
En todos los casos, se aplica el IVA del 21% sobre el total.
Requerimientos del programa:
Solicitar al usuario:
Cantidad de metros consumidos
Tipo de cliente, que puede ser: Residencial, Comercial o Industrial.
Calcular:
Subtotal de consumo.
Bonificaciones, si corresponde
Recargos, si corresponde
Subtotal, con recargos y bonificaciones.
IVA aplicado (21%), si corresponde.
Total final a pagar.
Mostrar en pantalla el desglose de los cálculos.

"""
# Entrada de datos
consumo = float(input("Ingrese la cantidad de metros cúbicos consumidos: "))
tipo_cliente = str(input("Ingrese el tipo de cliente (Residencial, Comercial o Industrial): "))

# Datos base
cargo_fijo = 7000
costo_m3 = 200
subtotal_consumo = consumo * costo_m3
ajuste = 0
descuento_especial = 0

# Lógica según tipo de cliente
match tipo_cliente:
    case "Residencial":
        if consumo < 30:
            ajuste = - (subtotal_consumo * 0.10)
        elif consumo > 80:
            ajuste = subtotal_consumo * 0.15

        if (subtotal_consumo + cargo_fijo) < 35000:
            descuento_especial = (subtotal_consumo + cargo_fijo + ajuste) * 0.05

    case "Comercial":
        if consumo > 300:
            ajuste = - (subtotal_consumo * 0.12)
        elif consumo > 150:
            ajuste = - (subtotal_consumo * 0.08)
        elif consumo < 50:
            ajuste = subtotal_consumo * 0.05

    case "Industrial":
        if consumo > 1000:
            ajuste = - (subtotal_consumo * 0.30)
        elif consumo > 500:
            ajuste = - (subtotal_consumo * 0.20)
        elif consumo < 200:
            ajuste = subtotal_consumo * 0.10

    case _:
        print("Tipo de cliente no válido.")
        exit()

# Cálculos
subtotal_con_ajustes = cargo_fijo + subtotal_consumo + ajuste - descuento_especial
iva = subtotal_con_ajustes * 0.21
total_final = subtotal_con_ajustes + iva

# Mostrar resultados
print("------ FACTURA ------")
print("Tipo de cliente:", tipo_cliente)
print("Consumo:", consumo, "m³")
print("Costo por consumo: $", subtotal_consumo)
print("Cargo fijo: $", cargo_fijo)

if ajuste < 0:
    print("Bonificación: $", ajuste)
elif ajuste > 0:
    print("Recargo: $", ajuste)
else:
    print("Sin bonificación ni recargo.")

if descuento_especial > 0:
    print("Descuento especial: $", -descuento_especial)

print("Subtotal con ajustes: $", subtotal_con_ajustes)
print("IVA (21%): $", iva)
print("TOTAL A PAGAR: $", total_final)
