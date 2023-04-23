import os

def validar_caracteristicas_usuario(nombre_usuario = ""):
    CARACTERES_MINIMO = int(6)
    CARACTERES_MAXIMO = int(12)

    longitud_cadena = len(nombre_usuario)

    bandera_caracteres_minimo = (longitud_cadena < CARACTERES_MINIMO)
    bandera_caracteres_maximo = (longitud_cadena > CARACTERES_MAXIMO)

    if (bandera_caracteres_maximo or bandera_caracteres_minimo):
        titulo_error = " == WARNING : El nombre de usuario" + ("", f" debe de tener mas de {CARACTERES_MINIMO} caracteres. == ")[
            bandera_caracteres_minimo] + ("", f" debe de tener menos de {CARACTERES_MAXIMO} caracteres. ==")[bandera_caracteres_maximo]
        return titulo_error, False

    if (nombre_usuario.isalnum() == False):
        titulo_error = " == WARNING : El nombre de usuario puede contener solo números y letras. =="
        return titulo_error, False
    
    titulo_error = f"El nombre de usuario < {nombre_usuario} > es valido."
    return titulo_error, True
