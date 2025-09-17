afiliados = []   # lista global

def entrada_datos():
    persona_afiliadas = afiliados # lista para almacenar los datos de las personas 
    numeros_de_identificacion = []   #lista para verificar q por numero de identificacion no haya datos repetidos 
    while True:  
        cedula = input("Ingrese el número de identificación o 'salir' o 'mostrar': ") 

        
        if cedula.lower() == 'mostrar':  
            try: 
                with open("personas_afiliadas.csv", "r") as archivo:
                    print("\nUsuarios registrados:") 
                    for linea in archivo:
                        datos = linea.strip().split(",")  
                        print(
                            f"cedula: {datos[0]} | "
                            f"nombre: {datos[1]} | "
                            f"apellidos: {datos[2]} | "
                            f"fecha de nacimiento: {datos[3]} | "         #imprime los datos en dichas posciciones y les pone el nombre q le corresponde a cada una (pedi ayuda al chat)
                            f"plan: {datos[4]} | "
                            f"género: {datos[5]} | "
                            f"correo: {datos[6]}"
                        )
            except FileNotFoundError:
                print("Todavía no hay afiliados registrados.")
            continue   
   # si el usuario ingresa 'salir', se termina el bucle 
        if cedula in numeros_de_identificacion:
         print("Número de identificación existente. Verifique e intente nuevamente.")
         continue
    
        if cedula.lower() == 'salir':
                break
        if cedula in numeros_de_identificacion: # verifica si la id ya existe en el conjunto
            print("El Número de identificación ya es existente. Verifique e intente nuevamente.")
            continue

        nombre = input("Ingrese nombres: ")                                           
        apellidos = input("Ingrese apellidos: ")                                      
        fechas_de_nacimiento = validacion_de_fecha()    #
        plan = input("Ingrese a  que plan pertenece (A,B,C): ").lower()               #usa lower() para convertir a minusculas     pide el ingreso de todos los datos de la persona afiliada 
        genero = input("Ingrese género (M o F): ").lower()                            #usa lower() para convertir a minusculas
        correo = input("Ingrese correo electrónico: ")
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
        numeros_de_identificacion.append(cedula)                                            # agrega el id a la lista para  verificaciones   futuras  

        with open("personas_afiliadas.csv", "a") as archivo:                         # abre el archivo en modo de agregar  para no sobrescribir sino agregar los datos existentes
            archivo.write(f"{cedula},{nombre},{apellidos},{fechas_de_nacimiento},{plan},{genero},{correo}\n")  # escribe los datos en el archivo en formato CSV

        print("Datos ingresados correctamente.")

    while  True: 
        opcion = input ("desea byscar un afiliado por su Cedula?, ingrese SI o NO: ")    #pregunta si desea buscar un afiliado por su ID
        if opcion.lower() == "si":                            
            cedula_buscar = input("Ingrese el ID del afiliado que desea buscar: ")      #pide el ID a buscar
            resultado_busqueda = buscar_afiliado_por_id(cedula_buscar)                  #llama a la funcion buscar_afiliado_por_id con el ID ingresado
            if resultado_busqueda:
                print("Afiliado encontrado:")
                print(resultado_busqueda)
            else:
                print("Afiliado no encontrado.")
                break 
        elif opcion.lower() == "no":
            break
        else:
            print("Opción no válida, ingrese si o no")
