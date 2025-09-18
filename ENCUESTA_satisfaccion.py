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
