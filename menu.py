def menu():
    # Al iniciar mostramos cuántos afiliados ya existen
    print("\n===== SISTEMA DE AFILIADOS EPS =====")

    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Registrar nuevo afiliado")
        print("2. Mostrar afiliados")
        print("3. Ordenar afiliados por apellido")
        print("4. Buscar afiliado por cédula")
        print("5. Estadísticas rápidas")
        print("6. Salir (guardar y cerrar)")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            entrada_datos()

        elif opcion == "2":
            if not afiliados:
                print("Todavía no hay afiliados registrados.")
            else:
                print("\nUsuarios registrados:")
                for af in afiliados:
                    print(
                        f"cédula: {af['cedula']} | "
                        f"nombre: {af['nombres']} | "
                        f"apellidos: {af['apellidos']} | "
                        f"fecha de nacimiento: {af['fecha de nacimiento']} | "
                        f"plan: {af['plan']} | "
                        f"género: {af['genero']} | "
                        f"correo: {af['correo']}"
                    )

        elif opcion == "3":
            ordenar_afi_apellido()

        elif opcion == "4":
            cedula_buscar = input("Ingrese la cédula a buscar (o 'salir' para cancelar): ")
            if cedula_buscar.lower() == "salir":
                continue
            resultado = buscar_afiliado_por_id(cedula_buscar)
            if resultado:
                print("Afiliado encontrado:", resultado)
            else:
                print("No se encontró el afiliado.")

        elif opcion == "5":
            print("\n--- ESTADÍSTICAS RÁPIDAS ---")
            estadistica_por_plan()
            promedio_edad_por_genero()

        elif opcion == "6":
            # Al salir guardamos automáticamente
            exportar_csv(afiliados)
            print(f"Saliendo del sistema... Se guardaron {len(afiliados)} afiliados en 'personas_afiliadas.csv'.")
            break

        else:
            print("Opción inválida, intente de nuevo.")


# Ejecutar el menú principal
menu()
