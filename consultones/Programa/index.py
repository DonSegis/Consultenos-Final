from ast import Break
from ctypes.wintypes import HLOCAL
from conexion import Conexion
from menuLogin import MenuLogin
conexion = Conexion()



while True:
    try:

        userName = input("Nombre de Usuario (rut eje: 12.345.678-9)\n") 
        userPassword = input("\ncontaseña\n")

        confirm = conexion.loging(userName)
        if confirm == None:
            print("Nombre de usuario incorrecto!!")

        else:
            confirm = conexion.confirmarContaseña(userPassword,confirm)
            if confirm == None:
                print("contraseña incorrecta!!")
            else:
                print("Bienvenido!!")
                while True:
                    tipoUsuario = conexion.TipoMenu(userName)
                    tipoUsuario = conexion.confirmarTipoUsuario(tipoUsuario)
                    menuLogin = MenuLogin(tipoUsuario)
                    idUsuario = conexion.idUser(userName)
                    id = conexion.confirmarTipoUsuario(idUsuario)

                    if tipoUsuario == "jefe ejecutivo":
                        menu = menuLogin.menuJe_Ej()
                        if menu == "stop":
                            break
                    elif tipoUsuario == "ejecutivo de area":
                        area = conexion.areaUser(userName)
                        area = conexion.confirmarTipoUsuario(area)
                        lista = conexion.listarTicketArea(area)
                        if len(lista) > 0:                         
                            menu = menuLogin.menuJe_Ar(id,lista)
                        else:
                            print("No hay Ticket asignados!!")
                        if menu == "stop":
                            break
                    elif tipoUsuario == "operador de mesa":
                        menu = menuLogin.menuOp_Me(id)
                        if menu == "stop":
                            break
                    else:
                        print("ERROR 404!!")
                        break
                break
        
    except ValueError:
        print("El dato ingresado es erroneo!!, intente no ingresar letras")