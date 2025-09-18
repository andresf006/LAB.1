
def calcular_edad(fecha_nacimiento):
    partes = fecha_nacimiento.split("/")
    dia = int(partes[0])
    mes = int(partes[1])
    año = int(partes[2])

    hoy_dia, hoy_mes, hoy_año = 18, 9, 2025  # fecha fija: 16/09/2025

    edad = hoy_año - año     #el año actual menos el año de nacimiento 
    if (hoy_mes, hoy_dia) < (mes, dia): #mira si ya cumplio años 
        edad -= 1 #si no edad es edad menos 1

    return edad
