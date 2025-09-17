def buscar_afiliado_por_id(id_buscar):
    try:
        with open("personas_afiliadas.csv", "r") as archivo:  #lo abrimos en modo lectura porq solo queremos buscar
            for linea in archivo:                 #leemos linea por linea
                datos = linea.strip().split(",")  #separamos los datos por comas y eliminamos espacios en blanco
                if datos[0] == id_buscar:         #comparamos la id en la posicion 0 con la id q queremos buscar asi ahorramos q paso por todas las lineas del archivo 
                    return {
                        'cedula': datos[0],          
                        'nombres': datos[1],
                        'apellidos': datos[2],
                        'fecha de nacimiento': datos[3],
                        'plan': datos[4],
                        'genero': datos[5],
                        'correo': datos[6]
                    }                             #si la id coincide, retornamos un diccionario con los datos del afiliado encontrado
        return
    except FileNotFoundError:
        print("El archivo no existe.")            # si el archivo no existe, muestra este mensaje, ya q estamos intentando leer un archivo q no existe
        return
