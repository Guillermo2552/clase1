class MenuInteractivo:
    def __init__(self):
        self.productos = []  

    def menu(self):
        while True:
            print("----------------------------------------------------------------------------------------------")
            print("===== MENU DE COMPRAS =====")
            print("\n1. Permitir agregar productos a una lista.") 
            print("2. Mostrar todos los productos registrados.")
            print("3. Calcular el total de la compra.") 
            print("4. Mostrar productos que cumplan una condición (por ejemplo: mayores a cierto precio).") 
            print("5. Salir.")
            print("----------------------------------------------------------------------------------------------")
            
            try:
                opcion = int(input("Seleccione una opción a continuación: "))
            except ValueError:
                print("Por favor, ingrese un número válido.")
                continue

            if opcion == 1:
                nombre = input("Ingrese el nombre del producto: ")
                try:
                    precio = float(input("Precio del producto: $"))
                    self.productos.append((nombre, precio))
                    print(f"Producto {nombre} agregado! ${precio}")
                except ValueError:
                    print("El precio debe ser en número.")

            elif opcion == 2:
                if not self.productos:
                    print("No hay productos registrados.")
                else:
                    print("Productos registrados: ")
                    for nombre, precio in self.productos:
                        print(f"- {nombre}: ${precio}")

            elif opcion == 3:
                # Se utiliza un condicional para validar si hay elementos 
                if not self.productos:
                    print("La lista está vacía. No hay total que calcular.")
                else:
                    total_compra = 0
                    # Se implementa un ciclo para recorrer la lista y sumar los precios 
                    for _, precio in self.productos:
                        total_compra += precio
                    print(f"El total acumulado de la compra es: ${total_compra}")

            elif opcion == 4:
                # Funcionalidad opcional de filtros [cite: 23, 55]
                if not self.productos:
                    print("No hay productos para filtrar.")
                else:
                    try:
                        limite = float(input("Mostrar productos con precio mayor a: $"))
                        print(f"Productos mayores a ${limite}:")
                        for nombre, precio in self.productos:
                            if precio > limite:
                                print(f"- {nombre}: ${precio}")
                    except ValueError:
                        print("Por favor, ingrese un valor numérico.")

            elif opcion == 5:
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

# Ejecución del programa [cite: 95]
if __name__ == "__main__":
    p = MenuInteractivo()
    p.menu()