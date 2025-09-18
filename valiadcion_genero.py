def validar_genero():
    while True:
        genero = input("Ingrese género (M o F) o 'salir': ").upper()

        if genero == "SALIR":  
            print("Operación cancelada por el usuario.")
            return # devolvemos 'salir' para que entrada_datos cancele

        if genero in ["M", "F"]:
            return genero  # género válido

        print("Género inválido. Por favor ingrese M o F.")
