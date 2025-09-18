def validar_plan():
    """
    Pide al usuario que ingrese un plan válido (A, B o C).
    Repite la solicitud hasta que el valor ingresado sea correcto.
    Retorna el plan en mayúsculas.
    """
    while True:
        plan = input("Ingrese a qué plan pertenece (A, B o C) o 'salir' : ").upper()
        
        if plan == 'salir':  # si el usuario ingresa 'salir', devolvemos 'salir' para que entrada_datos pueda cancelar
            print ("Operación cancelada por el usuario.")
            return 
        
        if plan in ["A", "B", "C"]:
            return plan
        print("Plan inválido. Debe ser A, B o C.(ingrese A, B o C)")
