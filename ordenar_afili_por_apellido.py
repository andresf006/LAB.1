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
