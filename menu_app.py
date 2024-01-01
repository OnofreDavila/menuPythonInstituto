def agregar_compra (compras, total_gastado):
    monto = float(input("Ingrese el monto de la compra: "))
    compras.append(monto)
    total_gastado += monto
    print("Compra agregada correctamente.")

def mostrar_compras (compras):
    if not compras:
        print("no hay compra registrada.")
    else:
        print("lista de compras:")
        N = len(compras)
        for i, compra in enumerate(compras,start=1):
            print(f"compra {i}: ${compra}")
def mostrar_total(total_gastado):
    print("Total gastado: $",sum(total_gastado))

def main():
    compras = []
    total_gastado = 0

    while True:
        print("\nMenu:")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. salir")
        opcion = input("Seleccione una opcion:")

        if opcion == "1":
            agregar_compra(compras, total_gastado)
        elif opcion == "2":
            mostrar_compras(compras)
        elif opcion == "3":
            mostrar_total(compras)
        elif opcion == "4":
            print("Hasta luego.")
            break
        else:
            print("Opcion inválida. Intente nuevamente.")
main()
