def estadistica_por_plan(): 
    # Muestra cuántos afiliados hay en cada plan y recorre la lista Afiliados y suma los valores en contadores.

    conteo_A = 0  # Contador de afiliados en Plan A
    conteo_B = 0  # Contador de afiliados en Plan B
    conteo_C = 0  # Contador de afiliados en Plan C

    # Recorremos cada afiliado registrado
    for af in Afiliados:
        if af["Plan"] == "A":       # Si el plan es A, sumamos en A
            conteo_A += 1
        elif af["Plan"] == "B":     # Si el plan es B, sumamos en B
            conteo_B += 1
        else:                       # Si no es A ni B, asumimos que es C
            conteo_C += 1

    # Mostramos los resultados
    print("\n--- TOTAL DE AFILIADOS POR PLAN ---")   # \n genera un salto de línea
    print("Plan A:", conteo_A)
    print("Plan B:", conteo_B)
    print("Plan C:", conteo_C)
