def exportar_csv(lista_afiliados, nombre_archivo="personas_afiliadas.csv"):
    """
    Exporta todos los afiliados actuales a un archivo CSV.
    Sobrescribe el archivo con los datos actuales en memoria.
    """
    if not lista_afiliados:  # Si la lista está vacía
        print("No hay afiliados para exportar.")
        return

    with open(nombre_archivo, "w") as archivo:  # "w" = sobrescribe el archivo
        # Escribir cabecera una sola vez
        archivo.write("cedula,nombres,apellidos,fecha de nacimiento,plan,genero,correo\n")

        # Escribir cada afiliado en formato CSV
        for af in lista_afiliados:
            linea = f"{af['cedula']},{af['nombres']},{af['apellidos']},{af['fecha de nacimiento']},{af['plan']},{af['genero']},{af['correo']}\n"
            archivo.write(linea)

    print(f"Datos exportados correctamente a {nombre_archivo}")
