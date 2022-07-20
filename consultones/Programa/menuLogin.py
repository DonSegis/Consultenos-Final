
from conexion import Conexion
import datetime
conexion = Conexion()


class MenuLogin():
    def __init__(self,tipoUser):
        self.jefeEjecutivo  =  "jefe ejecutivo"
        self.ejecutivoDeArea = "ejecutivo de area"
        self.operadorDeMesa = "operador de mesa"
        try:
            if tipoUser == self.jefeEjecutivo:
                print("\n1. Listar Tickets "+\
                    "\n2. Crear Usuarios"+\
                    "\n0. Salir")

            elif tipoUser == self.ejecutivoDeArea:
                print("\n1. Asiganr estado Tickets"+\
                    "\n0. Salir")

            elif tipoUser == self.operadorDeMesa:
                print("\n1. Crear Ticket "+\
                     "\n0. Salir")

        except ValueError:
            print("El dato ingresado es erroneo!!")
            
    def menuOp_Me(self,Operador):
        try:
            opcion = int(input("opcion: "))
            if opcion == 1:
                clienteNombre = input("Nombre Cliente: ")
                rutCliente = input("Rut Cliente: ")
                fecha = datetime.date.today()
                telefono = int(input("telefone: +56"))
                correo = input("Correo: ")
                criticidad = input("Criticidad: ")
                detallesServicio = input("Detalles Servicio: ")
                detallesProblema = input("Detalles Problema: ")
                idOperador = Operador
                print("\n1. Area 1"+\
                    "\n2. Area 2"+\
                    "\n3. Area 3"+\
                    "\n4. Area 4")
                idArea = int(input("Area: "))
                idEstado = 1
                print("\n1. Felicitracion"+\
                    "\n2. Consulta"+\
                    "\n3. Reclamo"+\
                    "\n4. Problema")
                idTipo_ticket = int(input("Tipo Ticket: "))
                while True:
                        print("\n1. Previsualizar"+\
                            "\n2. generar ticket")
                        opcion = int(input("Opcion: "))
                        
                        if opcion == 1:
                            if idArea == 1:
                                idArea = "Area 1"
                            elif idArea == 2:
                                idArea = "Area 2"
                            elif idArea == 3:
                                idArea = "Area 3"
                            else:
                                idArea = "Area 4"
                            
                            if idTipo_ticket == 1:
                                idTipo_ticket = "Felicitracion"
                            elif idTipo_ticket == 2:
                                idTipo_ticket = "Consulta"
                            elif idTipo_ticket == 3:
                                idTipo_ticket = "Reclamo"
                            else:
                                idTipo_ticket = "Problema"
                            
                            print("\nCliente: ",clienteNombre,\
                                "\nRut: ",rutCliente,\
                                "\nFecha: ",fecha,\
                                "\nTelefono: ",telefono,\
                                "\nCorreo: ",correo,\
                                "\nCriticidad: ",criticidad+\
                                "\nDetalles del servicio: ",detallesServicio,\
                                "\nDetalles del problema: ",detallesProblema,\
                                "\nArea: ",idArea,\
                                "\nEstado: Revision"+\
                                "\nTipo de Ticket: ",idTipo_ticket)
                        elif opcion == 2:
                            conexion.crearTicket(clienteNombre, rutCliente, fecha, telefono, correo, criticidad, detallesServicio, detallesProblema, idOperador, idArea, idEstado, idTipo_ticket)
                            break
            elif opcion == 0:
                stop = "stop"
                return stop    
        except ValueError:
                    print("El dato ingresado es erroneo!!")        
            

    def menuJe_Ar(self,user,lista):
        try:
            opcion = int(input("opcion: "))
            if opcion == 1:
                ticketPrint = ("\nId Ticket: {}"+\
                    "\nCliente: {}"+\
                    "\nRut: {}"+\
                    "\nFecha: {}"+\
                    "\nTelefono: {}"+\
                    "\nCorreo: {}"+\
                    "\nCriticidad: {}"+\
                    "\nDetalles del servicio: {}"+\
                    "\nDetalles del problema: {}"+\
                    "\nArea: {}"+\
                    "\nEstado: Revision"+\
                    "\nTipo de Ticket: {}")

                for i in lista:
                    if i[11] == 1:
                        idArea = "Area 1"
                    elif i[11] == 2:
                        idArea = "Area 2"
                    elif i[11] == 3:
                        idArea = "Area 3"
                    elif i[11] == 4:
                        idArea = "Area 4"
                    
                    if i[13] == 1:
                        idTipo_ticket = "Felicitracion"
                    elif i[13] == 2:
                        idTipo_ticket = "Consulta"
                    elif i[13] == 3:
                        idTipo_ticket = "Reclamo"
                    elif i[13] == 4:
                        idTipo_ticket = "Problema"
                    tabla = (ticketPrint.format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],idArea,idTipo_ticket))
                    print(tabla)
                ticket = int(input("\nid Ticket: "))
                print("\n1. Resuelto"+\
                    "\n2. No Aplicable")
                estado = int(input("Estado: "))
                observacion = input("observación: ")
                idUser = user
                if estado == 1:
                    estado = 2
                elif estado == 2:
                    estado = 3
                conexion.cierreTicket(ticket, estado, observacion, idUser)
            elif opcion == 0:
                stop = "stop"
                return stop

        except ValueError:
                    print("El dato ingresado es erroneo!!")

    
    def menuJe_Ej(self):
        try:
            opcion = int(input("opcion: "))
            filtro = []
            if opcion == 1:
                
                listaFiltro = ["Fecha","Criticidad","Tipo","Ejecutivo que abre el tique","Ejecutivo que cierra el tique","Area","Ninguno/stop"]
                for i in range(len(listaFiltro)):
                    
                    cont = 1
                    for j in listaFiltro:
                        print("\n{0}. {1}".format(cont,j))
                        cont = cont + 1
                    cont = cont - (len(listaFiltro)-2)
                    opcionFiltrado = int(input("opcion: "))
                    if opcionFiltrado == 1:
                        op = input("fecha (año/mes/dia): ")
                        fecha = "Fecha = '{0}'".format(op)
                        print(fecha)
                        filtro.append(fecha)
                    elif opcionFiltrado == 2:
                        op =  input("Criticidad: ")
                        criticidad = "Criticidad = '{0}'".format(op)
                        filtro.append(criticidad)
                    elif opcionFiltrado == 3:
                        print("\n1. Felicitracion"+\
                            "\n2. Consulta"+\
                            "\n3. Reclamo"+\
                            "\n4. Problema")
                        op =  input("Tipo: ")
                        if op == 1:
                            op = "Felicitracion"
                        elif op == 2:
                            op = "Consulta"
                        elif op == 3:
                            op = "Reclamo"
                        elif op == 4:
                            op = "Problema"
                        tipo = "Tipo = '{0}'".format(op)
                        filtro.append(tipo)
                    elif opcionFiltrado == 4:
                        op = input("Ejecutivo que abre el tique: ")
                        op = conexion.idUserPorUser(op)
                        ejecutivo = "ticket.id_usuario = '{0}'".format(op)
                        filtro.append(ejecutivo)
                    elif opcionFiltrado == 5:
                        op = input("Ejecutivo que cierra el tique: ")
                        op = conexion.idUserPorUser(op)
                        ejecutivo = "ticket.id_usuarioCierre = '{0}'".format(op)
                        filtro.append(ejecutivo)
                    elif opcionFiltrado == 6:
                        print("\n1. Area 1"+\
                            "\n2. Area 2"+\
                            "\n3. Area 3"+\
                            "\n4. Area 4")
                        op = input("Area: ")
                        if op == 1:
                            op = "Area 1"
                        elif op == 2:
                            op = "Area 2"
                        elif op == 3:
                            op = "Area 3"
                        elif op == 4:
                            op = "Area 4"
                        area = "areaticket.Area = '{0}'".format(op)
                        filtro.append(area)
                    elif opcionFiltrado == 7:
                        print("hola")
                        if len(filtro) > 0:
                            if len(filtro) >= 2:
                                dato = " AND ".join(map(str,filtro))
                                final = "WHERE {}".format(dato)
                                mostrar = conexion.listarTicket(final)
                                
                            elif len(filtro) == 1:
                                for i in filtro:
                                    final = "WHERE {}".format(i)
                                mostrar = conexion.listarTicket(final)
                                
                        else:
                            nada = " "
                            mostrar = conexion.listarTicket(nada)
                    
                    ticketPrint = ("\n{0}"+\
                                "\nNombre del ejecutivo: {1} {2}"+\
                                "\nFecha de creación: {3}"+\
                                "\nTipo: {4}"+\
                                "\nCriticidad: {5}"+\
                                "\nÁrea de destino: {6}"+\
                                "\nEstado: {7}")
                    
                    while True:
                        cont = 1
                        for i in mostrar:
                            tabla = (ticketPrint.format(cont,i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
                            cont = cont + 1
                            print(tabla)

                        print("\n1. Editar Tickes"+\
                                "\n0. salir")
                        opcion = int(input("Opcion: "))

                        if opcion == 1:
                            numTicket = int(input("Numero del ticket: "))
                            editar = mostrar[(numTicket - 1)]
                            idTicket = editar[7]

                            print("\n1. Editar area"+\
                                "\n2. Editar Tipo"+\
                                "\n3. Editar Criticidad")
                            opcion = int(input("Opcion: "))

                            if opcion == 1:
                                print("\n1. Area 1"+\
                                "\n2. Area 2"+\
                                "\n3. Area 3"+\
                                "\n4. Area 4")
                                nuevaArea = input("Nueva Area: ")
                                Area = "`id_area` = " + nuevaArea
                                conexion.editarTicket(Area, idTicket)

                            elif opcion == 2:
                                print("\n1. Felicitracion"+\
                                    "\n2. Consulta"+\
                                    "\n3. Reclamo"+\
                                    "\n4. Problema")
                                nuevoTipo = input("Nuevo Tipo: ")
                                Tipo = "`Id_estado` = " + nuevoTipo
                                conexion.editarTicket(Tipo, idTicket)

                            elif opcion == 3:
                                nuevaCriticidad = input("Nueva Criticidad: ")
                                Criticidad = "`Criticidad` = " + nuevaCriticidad
                                conexion.editarTicket(Criticidad, idTicket)
                        elif opcion == 0:
                            break
                        break    
            elif opcion == 2:
                rut = input("Rut del Usuario: ")
                nombre = input("Nombre del Usuario: ")
                apellido = input("Apellido del Usuario: ")
                contaseña = input("Contaseña del Usuario: ")
                print("\n1. jefe ejecutivo"+\
                    "\n2. ejecutivo de area"+\
                    "\n3. operador de mesa")
                cargo = int(input("Cargo del Usuario: ")) 
                if cargo == "jefe ejecutivo" or cargo =="operador de mesa":
                    areaUser = 5
                else:
                    print("\n1. Area 1"+\
                        "\n2. Area 2"+\
                        "\n3. Area 3"+\
                        "\n4. Area 4")
                    areaUser = int(input("Area del Usuario: "))
                userPrint = ("\nNombre del ejecutivo: {0} {1}"+\
                                "\nRut: {2}"+\
                                "\nContaseña: {3}"+\
                                "\nCargo: {4}"+\
                                "\nÁrea: {5}")
                if areaUser == 1:
                    op = "Area 1"
                elif areaUser == 2:
                    op = "Area 2"
                elif areaUser == 3:
                    op = "Area 3"
                elif areaUser == 4:
                    op = "Area 4"
                elif areaUser == 5:
                    op = "Sin Area"

                if cargo == 1:
                    tipo = "jefe ejecutivo"
                elif cargo == 2:
                    tipo = "ejecutivo de area"
                elif cargo == 3:
                    tipo = "operador de mesa"
                listar = userPrint.format(nombre,apellido,rut,contaseña,tipo,op)
                print(listar)
                print("\n1. Crea"+\
                    "\n2. Eliminar")
                opcion = int(input("Opcion: "))    
                if opcion == 1:
                    conexion.crearUsuario(rut,nombre,apellido,contaseña,cargo,areaUser)
                    print("El Usuario Fue Creado con Exito!!")
                else:
                    None

            elif opcion == 0:
                stop = "stop"
                return stop
                
        except ValueError:
            print("El dato ingresado es erroneo!!")
