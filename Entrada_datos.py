
ids_existentes = set()  # conjunto global para almacenar IDs existentes y evitar duplicados
afiliados = cargar_afiliados()  # lista global

def entrada_datos():
    persona_afiliadas = afiliados # lista para almacenar los datos de las personas 
    numeros_de_identificacion = set()
       #conjunto para verificar q por numero de identificacion no haya datos repetidos 
    while True:  
        cedula = input("Ingrese el número de identificación o 'salir': ")  
   # si el usuario ingresa 'salir', se termina el bucle 
        if cedula in ids_existentes:    # validamos contra el set global
            print("Número de identificación existente. Verifique e intente nuevamente.")
            continue
    
        if cedula.lower() == 'salir':
                break

        nombre = input("Ingrese nombres: ")                                           
        apellidos = input("Ingrese apellidos: ")                                      
        fechas_de_nacimiento = validacion_de_fecha()    #
        plan = validar_plan()              #usa lower() para convertir a minusculas     pide el ingreso de todos los datos de la persona afiliada 
        genero = validar_genero()                         #usa lower() para convertir a minusculas
        correo = validacion_correo ()
        afiliado  = {
            'cedula': cedula,
            'nombres': nombre,
            'apellidos': apellidos,
            'fecha de nacimiento': fechas_de_nacimiento,                             # crea un diccionario con todos los datos del afiliado
            'plan': plan,
            'genero': genero,
            'correo': correo
        }
        persona_afiliadas.append(afiliado)                                            # agrega el diccionario a la lista de personas afiliadas   
        numeros_de_identificacion.add(cedula)                                            # agrega el id al conjunto para  verificaciones   futuras  

        with open("personas_afiliadas.csv", "a") as archivo:                         # abre el archivo en modo de agregar  para no sobrescribir sino agregar los datos existentes
            archivo.write(f"{cedula},{nombre},{apellidos},{fechas_de_nacimiento},{plan},{genero},{correo}\n")  # escribe los datos en el archivo en formato CSV

        print("Datos ingresados correctamente.")

def ordenar_afi_apellido():
    try:
        with open("personas_afiliadas.csv", "r") as archivo:
            afiliados = []
            for linea in archivo:
                datos = linea.strip().split(",")
                afiliados.append(datos)  # Guardamos cada afiliado como lista en lugar de un diccionario, asi cada afiliado sera una lista aparte

            if not afiliados:                                      #si no hay afiliados registrados tira este mensaje y nos hace un return none
                print("No hay afiliados registrados todavía.")
                return

            #usamos metodo de burbuja para ordenar los datos , intercambiando de tal forma q quedan prdenados alfabeticamente 
            n = len(afiliados)  #cuenta el numero total de afiliados 
            for i in range(n - 1): #hacemos n-1 porq no es necesario pasar la ultima vez ya q al ser el ultimo elemento queda ordenado 
                for j in range(n - i - 1):   #aqui n es la cantidad total de afiliados, n es el numero de pasadas totatel qq hemos hecho por la lista, en cada pasada (i), ya hay un apellido colocado al final, 
                    #por lo que no necesitamos comparar ese ultimo elemento en la siguiente pasada por lo q ya no compara el ultimo elemento 
                    if afiliados[j][2].lower() > afiliados[j + 1][2].lower():                     #afiliados[j][2]  es el apellido del afiliado en la posicion j. siendo J cada afiliado, 
                        #j+1 salta al siguientte afiliado  y compara los apellidos,
                        afiliados[j], afiliados[j + 1] = afiliados[j + 1], afiliados[j] # si j+1 es menor alfabeticamente, se intercambian

            # Imprimimos la lista ya ordenada
            print("\nLISTA DE AFILIADOS ORDENADOS POR APELLIDOS (Alfabeticamente):")
            for datos in afiliados:
                print(
                    f"cedula: {datos[0]} | "
                    f"nombre: {datos[1]} | "
                    f"apellidos: {datos[2]} | "
                    f"fecha de nacimiento: {datos[3]} | "
                    f"plan: {datos[4]} | "
                    f"género: {datos[5]} | "
                    f"correo: {datos[6]}"
                )
    except FileNotFoundError:
        print("El archivo 'personas_afiliadas.csv' no existe todavía. Registre un  afiliado primero como minimo.")



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
