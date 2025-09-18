def validacion_correo():
    while True:
        correo = input("Ingrese correo electrónico: ")
        if "@" in correo and "." in correo:  # validación básica de formato de correo
            return
        else:
            print("Correo electrónico inválido no está usando @ Intente nuevamente.")
