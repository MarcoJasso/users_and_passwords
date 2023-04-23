# bandera_mayusculas = False
# bandera_minusculas = False
# bandera_numeros = False
# bandera_caracters_especiales = False
# bandera_caracteres_minimos = False
# bandera_espacios_en_blanco = False


# def reiniciar_valores():
#     global bandera_mayusculas
#     bandera_mayusculas = False

#     global bandera_minusculas
#     bandera_minusculas = False

#     global bandera_numeros
#     bandera_numeros = False

#     global bandera_caracters_especiales
#     bandera_caracters_especiales = False

#     global bandera_caracteres_minimos
#     bandera_caracteres_minimos = False

#     global bandera_espacios_en_blanco
#     bandera_espacios_en_blanco = False


def validar_contrasenia(password=""):

    CARACTERES_MINIMO = 8
    tituto_error = ""

    bandera_mayusculas = False
    bandera_minusculas = False
    bandera_numeros = False
    bandera_caracters_especiales = False
    bandera_caracteres_minimos = False
    bandera_espacios_en_blanco = False

    if (len(password) >= CARACTERES_MINIMO):
        bandera_caracteres_minimos = True

    for caracter in password:
        if (caracter.isspace()):
            bandera_espacios_en_blanco = True
        elif (caracter.isalnum() == False):
            bandera_caracters_especiales = True

        if (caracter.isdigit()):
            bandera_numeros = True

        if (caracter.islower()):
            bandera_minusculas = True

        if (caracter.isupper()):
            bandera_mayusculas = True

        tituto_error = f"\nCaracteristicas para definir una contraseña :\n [ { ('✘', '✓') [bandera_minusculas]} ] Minúsculas \n [ { ('✘', '✓') [bandera_mayusculas]} ] Mayúsculas \n [ { ('✘', '✓') [bandera_numeros]} ] Números \n [ { ('✘', '✓')[bandera_caracters_especiales] } ] Contiene caracteres especiales \n [ { ('✘', '✓') [bandera_caracteres_minimos]} ] Mayor o igual a {CARACTERES_MINIMO} caracteres.\n{ ('', ':: ADVERTENCIA => La contraseña no debe de tener espacion en blanco ::') [bandera_espacios_en_blanco]}"

    if (bandera_caracteres_minimos and bandera_caracters_especiales and bandera_espacios_en_blanco == False and bandera_numeros and bandera_minusculas and bandera_mayusculas):
        tituto_error = f"La contraseña < {password} > cumple con todos los requerimientos solicitados."
        return tituto_error, True
    else:
        return tituto_error, False
