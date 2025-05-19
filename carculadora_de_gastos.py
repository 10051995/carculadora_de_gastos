# Calculadora de gastos mensuales con guardado en archivos

# Solicitar el presupuesto mensual
presupuesto = float(input("Ingresa tu presupuesto mensual: "))
gastos = []

while True:
    # Solicitar el nombre del gasto
    nombre = input("Nombre del gasto (o escribe 'fin' para terminar): ")
    if nombre.lower() == 'fin':
        break

    # Solicitar la cantidad del gasto
    try:
        cantidad = float(input(f"¿Cuánto gastaste en {nombre}?: "))
        gastos.append((nombre, cantidad))
    except ValueError:
        print("Por favor, ingresa un número válido para la cantidad.")

# Calcular el total de gastos y el dinero restante
total_gastos = sum(gasto[1] for gasto in gastos)
restante = presupuesto - total_gastos

# Mostrar resumen en pantalla
print("\nResumen de gastos:")
for nombre, cantidad in gastos:
    print(f"- {nombre}: ${cantidad:.2f}")
print(f"\nTotal gastado: ${total_gastos:.2f}")
print(f"Dinero restante: ${restante:.2f}")

# Guardar los datos en un archivo
with open("reporte_gastos.txt", "w") as archivo:
    archivo.write(f"Presupuesto mensual: ${presupuesto:.2f}\n")
    archivo.write("Gastos:\n")
    for nombre, cantidad in gastos:
        archivo.write(f"- {nombre}: ${cantidad:.2f}\n")
    archivo.write(f"\nTotal gastado: ${total_gastos:.2f}\n")
    archivo.write(f"Dinero restante: ${restante:.2f}\n")

print("\nLos datos se han guardado en el archivo 'reporte_gastos.txt'.")
         