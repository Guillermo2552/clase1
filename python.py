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
                print("Opción 3 seleccionada.")
            elif opcion == 4:
                print("Opción 4 seleccionada.")
            elif opcion == 5:
                print("Saliendo...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")


p = MenuInteractivo()
p.menu()