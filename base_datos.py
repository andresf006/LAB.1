def cargar_afiliados(nombre_archivo="personas_afiliadas.csv"):
    global ids_existentes  # Declaramos la variable global para usarla dentro de la función
    lista = []  # Lista vacía donde guardaremos los afiliados leídos del archivo
    try:
        # Abrimos el archivo en modo lectura ("r")
        with open(nombre_archivo, "r") as archivo:  #usamos with para gestion DE FORMA SEGURA EL ARCHIVO 
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

def validacion_correo():
    while True:
        correo = input("Ingrese correo electrónico: ")
        if "@" in correo and "." in correo:  # validación básica de formato de correo
            return correo 
        else:
            print("Correo electrónico inválido no está usando @ Intente nuevamente.")

def validacion_de_fecha():
    while True:
        fecha = input("Ingrese fecha de nacimiento (dd/mm/aaaa) o 'salir': ")
        partes_fecha = fecha.split("/")  # dividimos por "/"
        if fecha.lower() == 'salir':  # si el usuario ingresa 'salir', devolvemos 'salir' para que entrada_datos pueda cancelar
            print ("Operación cancelada por el usuario.")
            return menu()
        
         # Validamos que la fecha tenga el formato correcto
        if len(partes_fecha) == 3:  # deben existir 3 partes: día, mes, año, contamos q las partes dividas por el split / sean 3
            d, m, a = partes_fecha   # desempaquetamos las partes en variables al usar split quendan 3 variables desempaquetadas
            try: #intenta convertir a enteros 
                d, m, a = int(d), int(m), int(a)                         # convertimos a enteros para poder validar q cumplan con los rangos de dia, mes y año
                if 1 <= d <= 31 and 1 <= m <= 12 and 1930 <= a <= 2025: # validamos los rangos de dia, mes y año
                    return fecha  # fecha válida 
                else:
                    print("Día, mes o año fuera de rango, introduzca una fecha valida.")  # si no cumple con los rangos, muestra este mensaje
            except ValueError:    # si ocurre un error en lugar de romper el programa, se captura la excepción  y muestra el mensaje
                print("La fecha contiene caracteres no numéricos (no use letras meta dia/mes/año. En numeros).") # si no se pueden convertir a enteros, muestra este mensaje
        else:
            print("Formato inválido por favor use dd/mm/aaaa.")


def validar_plan():
    while True:
        plan = input("Ingrese a qué plan pertenece (A, B o C) o 'salir' : ").upper()
        
        if plan == 'salir':  # si el usuario ingresa 'salir', devolvemos 'salir' para que entrada_datos pueda cancelar
            print ("Operación cancelada por el usuario.")
            return menu()
        
        if plan in ["A", "B", "C"]:
            return plan
        print("Plan inválido. Debe ser A, B o C.(ingrese A, B o C)")


def validar_genero():
    while True:
        genero = input("Ingrese género (M o F) o 'salir': ").upper()

        if genero == "SALIR":  
            print("Operación cancelada por el usuario.")
            return menu()# devolvemos 'salir' para que entrada_datos cancele

        if genero in ["M", "F"]:
            return genero  # género válido

        print("Género inválido. Por favor ingrese M o F.")



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
                return menu()  # devolvemos al menú principal si el usuario ingresa 'salir'

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



def borrar_base_de_datos():
    confirmacion = input("¿Desea borrar la base de datos? (SI/NO): ").lower()
    if confirmacion == "si":
        with open("personas_afiliadas.csv", "w") as archivo:
            archivo.write("")  # Borra el archivo

        afiliados.clear()         # Borra la lista en memoria
        ids_existentes.clear()    # Borra los IDs cargados

        print("La base de datos fue borrada completamente.")
    else:
        print("Operación cancelada. La base de datos no ha sido borrada.")
        return menu ()





# funcion para calcular edad

def calcular_edad(fecha_nacimiento):
    partes = fecha_nacimiento.split("/")
    dia = int(partes[0])
    mes = int(partes[1])
    año = int(partes[2])

    hoy_dia, hoy_mes, hoy_año = 18, 9, 2025  # fecha fija: 16/09/2025

    edad = hoy_año - año
    if (hoy_mes, hoy_dia) < (mes, dia):
        edad -= 1

    return edad


# funcion de promedio y extremos de edad

def promedio_edad_por_genero(): 
    # Calcula: Promedio de edad de hombres (M) promedio de edad de mujeres (F) y Afiliado más joven y más veterano.

    edades_M = []       # Lista para almacenar edades de los hombres
    edades_F = []       # Lista para almacenar edades de las mujeres
    todas_edades = []   # Lista con tuplas (nombre completo, edad) de todos los afiliados

    # Recorremos todos los afiliados en la lista principal
    for af in afiliados:
        edad = calcular_edad(af["fecha de nacimiento"])   # Calculamos la edad del afiliado
        genero = af["genero"].upper()                     # Aseguramos que la letra esté en mayúscula con .upper

        # Clasificamos la edad según el género
        if genero == "M":
            edades_M.append(edad)
        elif genero == "F":
            edades_F.append(edad)

        # Guardamos en la lista general el nombre completo + la edad
        nombre = af["nombres"] + " " + af["apellidos"]   # unimos nombres y apellidos con separacion de " "
        todas_edades.append((nombre, edad))              # Ejemplo: ("Felipe Castro", 18)

    print("\n--- PROMEDIO DE EDAD POR GÉNERO ---")   #Mostramos promedio y mediante \n saltamos un renglon

    if edades_M:   # Si hay hombres en la lista
        prom_M = sum(edades_M) / len(edades_M)   # Sacamos el promedio
        print("Hombres (M):", round(prom_M, 1), "años en promedio")
    else:
        print("Hombres (M): sin afiliados")           #Si no hay

    if edades_F:   # Si hay mujeres en la lista
        prom_F = sum(edades_F) / len(edades_F)   # Sacamos el promedio
        print("Mujeres (F):", round(prom_F, 1), "años en promedio")
    else:
        print("Mujeres (F): sin afiliados")    #Si no hay

    # Buscamos al más joven y al más veterano

    if todas_edades:  
        # Inicializamos las variables con el primer afiliado de la lista
        joven = todas_edades[0]
        veterano = todas_edades[0]

        # Se recorre el resto de la lista comparando edades
        for persona in todas_edades:
            nombre, edad = persona  # la tupla pasa en variables

            # Si encontramos una edad menor, actualizamos al más joven
            if edad < joven[1]:
                joven = persona

            # Si encontramos una edad mayor, actualizamos al más veterano
            if edad > veterano[1]:
                veterano = persona

        print("\n--- EXTREMOS DE EDAD ---")              # Salto de línea para claridad
        print("Afiliado más joven:", joven[0], "-", joven[1], "años")
        print("Afiliado más veterano:", veterano[0], "-", veterano[1], "años")   
        # Desplegamos los datos necesarios.


def estadistica_por_plan(): 
    # Muestra cuántos afiliados hay en cada plan y recorre la lista Afiliados y suma los valores en contadores.

    conteo_A = 0  # Contador de afiliados en Plan A
    conteo_B = 0  # Contador de afiliados en Plan B
    conteo_C = 0  # Contador de afiliados en Plan C

    # Recorremos cada afiliado registrado
    for af in afiliados:
        if af["plan"] == "A":       # Si el plan es A, sumamos en A
            conteo_A += 1
        elif af["plan"] == "B":     # Si el plan es B, sumamos en B
            conteo_B += 1
        else:                       # Si no es A ni B, asumimos que es C
            conteo_C += 1

    # Mostramos los resultados
    print("\n--- TOTAL DE AFILIADOS POR PLAN ---")   # \n genera un salto de línea
    print("Plan A:", conteo_A)
    print("Plan B:", conteo_B)
    print("Plan C:", conteo_C)



def ecuesta_satisfaccion(): 
    afili = afiliados  #Usamos el diccionario que guarda los datos de los afiliados registrados

    preguntas = [
        "¿Qué tan satisfecho está con la atención recibida por parte del personal?",

        "¿Consideras que el tiempo de espera para recibir atención fue adecuado?",

        "¿Qué tan clara fue la información suministrada sobre tus servicios?",

     "¿El proceso para solicitar un servicio te resultó fácil de realizar por la pagina?",

     "¿Qué tan satisfecho está con la calidad de los servicios de salud prestados?",

     "¿Recomendarías esta EPS a tus familiares o amigos?"
                    ]                                                                             # Defininimos las preguntas de satisfacción y las guardamos en una lista

    respuestas = []  # Lista para almacenar resultados

    print("Responda la siguiente encuesta de satisfacción (1 = Muy insatisfecho, 5 = Muy satisfecho).\n")

# Recorremos la lista global "afiliados" buscando el que tenga esa cédula
    cedula = input("Ingrese la cédula del afiliado que responderá la encuesta: ")
    for af in afiliados:
        
        if af["cedula"] == cedula:   # Si encontramos coincidencia
            respuestas = []  # Creamos una lista vacía para almacenar las respuestas de este afiliado

            # Mostramos instrucciones al usuario
            print("\nResponda la siguiente encuesta de satisfacción (1 = Muy insatisfecho, 5 = Muy satisfecho). \n")

            # Recorremos cada pregunta de la encuesta
            for pregunta in preguntas:
                while True:  # Usamos un ciclo para asegurarnos que la respuesta sea válida
                    try:
                        # Solicitamos la respuesta al usuario
                        respuesta = int(input(f"{pregunta} (1-5): "))
                        
                        # Validamos que la respuesta esté entre 1 y 5
                        if 1 <= respuesta <= 5:
                            respuestas.append(respuesta)  # Si es válida, la agregamos a la lista
                            break  # Salimos del ciclo while para pasar a la siguiente pregunta
                        else:
                            # Si el número no está en el rango correcto
                            print("Por favor, ingresa un número entre 1 y 5.")
                    except ValueError:
                        # Si el usuario ingresa letras o símbolos en vez de un número
                        print("Entrada inválida. Solo se aceptan números enteros.")

            # Una vez contestadas todas las preguntas, guardamos la lista en el afiliado encontrado
            af["respuestas"] = respuestas[:]   # Creamos una copia de la lista con [:] para mayor seguridad

            # Mostramos confirmación al usuario con los datos del afiliado
            print(f"\n Encuesta guardada para {af['nombres']} {af['apellidos']} (cédula: {af['cedula']})")
            return  # Terminamos la función porque ya procesamos al afiliado
    
    # Si el for termina y no encontró ninguna coincidencia de cédula
    print("No se encontró un afiliado con esa cédula.")  


def promedio(lista):       #Calcular promedio de la lisat
    return sum(lista) / len(lista) if lista else 0 #si la lista no está vacía, calcula el promedio, si está vacía devuelve 0


def estadisticas_satisfaccion():
    # ---- ESTADÍSTICAS GENERALES ----
    print("\n Estadísticas Generales ")

    # Creamos una lista vacía que va a contener TODAS las respuestas
    # de todos los afiliados registrados en el sistema
    todas = []

    # Recorremos la lista global "afiliados".
    # Cada "datos" es un diccionario con info: nombre, genero, plan, edad, respuestas...
    for datos in afiliados:
        try:
            todas.extend(datos["respuestas"])         
        # Extendemos la lista "todas" con las respuestas del afiliado actual
        # (extend agrega los elementos de la lista, no la lista entera como append)
        except KeyError:
        # Si el afiliado no tiene la clave "respuestas" (no ha hecho la encuesta)
        # simplemente ignoramos ese error y seguimos con el siguiente afiliado
            continue     

    # Calculamos y mostramos el promedio general de satisfacción
    # Usamos la función promedio(lista) definida antes
    # round(..., 2) redondea a 2 decimales
    print("Promedio general de satisfacción:", round(promedio(todas), 2))

  
    print("\n Estadísticas por género ")

    # Creamos un conjunto con los géneros presentes (ejemplo: {"M", "F"})
    # Lo hacemos con una comprensión de conjuntos
    generos = set(datos["genero"] for datos in afiliados)

    # Recorremos cada género único que existe en afiliados
    for g in generos:
        # Lista para acumular solo las respuestas de afiliados de ese género
        resp_genero = []
        
        # Recorremos otra vez todos los afiliados
        for datos in afiliados:
            # Si el género del afiliado coincide con el que estamos analizando (g)
            if datos["genero"] == g:
                # Agregamos sus respuestas a la lista resp_genero
                resp_genero.extend(datos["respuestas"])
        
        # Mostramos el promedio de satisfacción para ese género
        print(f"Género {g}: {round(promedio(resp_genero), 2)}/5")

    # ---- ESTADÍSTICAS POR PLAN ----
    print("\n Estadísticas por plan ")

    # Igual que con los géneros, pero ahora obtenemos los planes distintos (A, B, C)
    planes = set(datos["plan"] for datos in afiliados) #recorre la lista afiliados, ya que cada elemto es un diccionario, y extrae el valor asociado a la clave "plan", creando un conjunto con los planes distintos
    # planes será un conjunto con los planes únicos, ej: {"A", "B", "C"} asi no se repite el mismo plan 

    # Recorremos cada plan único
    for p in planes: #este for se ejecutass tres veces, una por cada plan distinto
        # Lista para acumular respuestas solo de los afiliados que tengan ese plan
        resp_plan = [] #Cada vez que empieza un nuevo planen el bucle, creamos una lista vacía que va a acumular todas las respuestas de los afiliados que estén en ese plan.
        
        # Recorremos todos los afiliados y comparamos su plan si no coincide con el plan actual del bucle, no hacemos nada
        for datos in afiliados:
            # Si el plan del afiliado coincide con el que estamos analizando (p)
            if datos["plan"] == p:
                # Agregamos sus respuestas a la lista resp_plan
                resp_plan.extend(datos["respuestas"]) #Si el afiliado está en el plan correcto, le agregamos sus respuestas a la lista resp_plan extend() sirve para añadir los elementos de una lista dentro de otra.
        
        # Mostramos el promedio de satisfacción de todos los afiliados de ese plan
        print(f"Plan {p}: {round(promedio(resp_plan), 2)} de 5") #promedio(resp_plan) → calcula el promedio de esas respuestas. f"Plan {p}: .../5" → construye el texto bonito con el nombre del plan y su promedio.


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
        print("6. Eliminar base de datos, (dejar vacio)")
        print("7. salir y exportar CSV")

        opcion = input("Seleccione una opción (1-7): ")

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
         borrar_base_de_datos()

        elif  opcion == "7":
                    # Al salir guardamos automáticamente
            exportar_csv(afiliados)
            print(f"Saliendo del sistema... Se guardaron {len(afiliados)} afiliados en 'personas_afiliadas.csv'.")  
            break # Salimos del bucle y terminamos el programa 

        else:
            print("Opción inválida, intente de nuevo.")


menu ()  # Iniciamos el programa mostrando el menú principal
