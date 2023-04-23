import os
from valicacion_contrasenias import validar_contrasenia
from validacion_nombres_usuario import validar_caracteristicas_usuario

if __name__ == "__main__":

    os.system("clear")

    nombre_usuario = ""
    contrasenia_usuario = ""

    error_nombre_usuario = ""
    error_contrasenia = ""

    while (True):

        nombre_usuario = input("\nIngresa el nombre de usuario : ")
        error_nombre_usuario, bandera_nombre_usuario = validar_caracteristicas_usuario(
            nombre_usuario)
        
        if (bandera_nombre_usuario):
            os.system("clear")
            print(error_nombre_usuario)
            break
        else:
            os.system("clear")
            print(error_nombre_usuario)

    while (True):

        contrasenia = input("\nContraseña : ")
        error_contrasenia, bandera_contrasenia = validar_contrasenia(contrasenia)

        os.system("clear")

        if (bandera_contrasenia):
            os.system("clear")
            break
        else:
            os.system("clear")
            print(error_nombre_usuario)
            print(error_contrasenia)
    
    print(error_nombre_usuario, "\n" ,error_contrasenia)
