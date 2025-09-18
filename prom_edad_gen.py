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
