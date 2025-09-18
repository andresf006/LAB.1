def validacion_de_fecha():
    while True:
        fecha = input("Ingrese fecha de nacimiento (dd/mm/aaaa) o 'salir': ")
        partes_fecha = fecha.split("/")  # dividimos por "/"
        if fecha.lower() == 'salir':  # si el usuario ingresa 'salir', devolvemos 'salir' para que entrada_datos pueda cancelar
            print ("Operación cancelada por el usuario.")
            return 
        
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
