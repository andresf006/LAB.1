def cargar_afiliados(nombre_archivo="personas_afiliadas.csv"):
    global ids_existentes  # Declaramos la variable global para usarla dentro de la función
    lista = []  # Lista vacía donde guardaremos los afiliados leídos del archivo
    try:
        # Abrimos el archivo en modo lectura ("r")
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()  # Leemos todas las líneas del archivo

            # Recorremos cada línea leída
            for linea in lineas:
                datos = linea.strip().split(",")  # Quitamos saltos de línea y separamos por comas 
# Verificamos que la línea tenga al menos 7 campos (cedula, nombres, apellidos, fecha, plan, genero, correo)
                if len(datos) >= 7:
                    # Creamos un diccionario con la información del afiliado
                    afiliado = {
                        "cedula": datos[0],
                        "nombres": datos[1],
                        "apellidos": datos[2],
                        "fecha de nacimiento": datos[3],
                        "plan": datos[4],
                        "genero": datos[5],
                        "correo": datos[6]
                    }
                    lista.append(afiliado)        # Agregamos el afiliado a la lista
                    ids_existentes.add(datos[0])  # Guardamos la cédula en el set global para evitar duplicados
    except FileNotFoundError:
        # Si el archivo no existe, mostramos un mensaje y devolvemos lista vacía
        print("No existe el archivo, se creará uno nuevo al registrar un afiliado.") 

    return lista  # Retornamos la lista con todos los afiliados cargados
