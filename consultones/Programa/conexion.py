
from asyncio.windows_events import NULL
import mysql.connector
from mysql.connector import Error

class Conexion():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                    host='localhost',
                    port=3306,
                    user='root',
                    password='',
                    db='consultenos'
                )
        except Error as ex:
            print("Error de conexión: {0} ".format(ex))


    def loging(self,userName):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT Contaseña FROM usuario WHERE Rut = '{0}'".format(userName))
                result = cursor.fetchone()
                return result
            except Error as ex:
                print("Error de conexión: {0} ".format(ex))

    def TipoMenu(self,userName):
       if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT tipousuario FROM usuario us INNER JOIN tipousuario ti ON us.id_tipoUser = ti.id_tipoUser WHERE Rut = '{0}'".format(userName))
                result = cursor.fetchone()
                return result
            except Error as ex:
                print("Error de conexión: {0} ".format(ex)) 

    def idUser(self,userName):
       if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT id_usuario FROM usuario  WHERE Rut = '{0}'".format(userName))
                result = cursor.fetchone()
                return result
            except Error as ex:
                print("Error de conexión: {0} ".format(ex))
    
    def idUserPorUser(self,userName):
       if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT id_usuario FROM usuario  WHERE usuario.usuario = '{0}'".format(userName))
                result = cursor.fetchone()
                for i in result:
                    confirm = i
                return confirm

            except Error as ex:
                print("Error de conexión: {0} ".format(ex))
    
    def areaUser(self,userName):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT area FROM usuario  WHERE Rut = '{0}'".format(userName))
                result = cursor.fetchone()
                return result
            except Error as ex:
                print("Error de conexión: {0} ".format(ex))

    def listarTicketArea(self,area):
        if self.conexion.is_connected():
            try: 
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM ticket ti WHERE ti.id_area = {0};".format(area))
                result = cursor.fetchall()
                return result
            except Error as ex:
                print("Error de conexión: {0} ".format(ex))

    def listarTicket(self,dato):
        if self.conexion.is_connected():
            try: 
                cursor = self.conexion.cursor()
                cursor.execute("SELECT Nombre, Apellido, Fecha, tipoticket.Tipo,Criticidad ,areaticket.Area, estadoticket.Estado, Id_ticket FROM ticket INNER JOIN areaticket ON areaticket.id_area = ticket.id_area INNER JOIN estadoticket ON estadoticket.Id_estado = ticket.Id_estado INNER JOIN usuario ON usuario.id_usuario = ticket.id_usuario INNER JOIN tipoticket ON tipoticket.id_tipoTicket = ticket.id_tipoTicket {0};".format(dato))
                result = cursor.fetchall()
                return result
            except Error as ex:
                print("Error de conexión: {0} ".format(ex))

    def listarUsuarios(self):
        if self.conexion.is_connected():
            try: 
                cursor = self.conexion.cursor()
                cursor.execute("SELECT Nombre, Apellido, rut, tipoUsuario FROM usuario us INNER JOIN tipoUsuario tius ON tius.id_tipoUser = us.id_tipoUser;")
                result = cursor.fetchall()
                return result
            except Error as ex:
                print("Error de conexión: {0} ".format(ex))

    def confirmarContaseña(self,password,result):
        for i in result:
            if i == password:
                confirm = i
                return confirm
            else:
                confirm = None
                return confirm

    def confirmarTipoUsuario(self,tipoUser):
        for i in tipoUser:
            confirm = i
            return confirm

    def crearTicket(self, clienteNombre, rutCliente, Fecha, telefono, correo, criticidad, detallesServicio, detallesProblema, idOperador, idArea, idEstado, idTipo_ticket):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                orden = "INSERT INTO `ticket` (`Id_ticket`, `Nombre_cliente`, `Rut_cliente`, `Fecha`, `Telefono`, `Correo`, `Criticidad`, `Detalles_servicio`, `Detalles_problema`,`observación`, `id_usuario`, `id_area`, `Id_estado`, `id_tipoTicket`, `id_usuarioCierre`) VALUES ({0},'{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}',{14})"
                cursor.execute(orden.format(NULL,clienteNombre, rutCliente, Fecha, telefono, correo, criticidad, detallesServicio, detallesProblema, NULL, idOperador, idArea, idEstado, idTipo_ticket, NULL))
                self.conexion.commit()
            except Error as ex:
                print("Error de conexión: {0} ".format(ex))

    def crearUsuario(self, rut, nombre, apellido, contraseña, tipo, area):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                orden = "INSERT INTO `usuario` (`id_usuario`, `rut`, `Nombre`, `Apellido`, `Contaseña`, `id_tipoUser`, `id_area`) VALUES ({0},'{1}','{2}','{3}','{4}','{5}','{6}')"
                cursor.execute(orden.format(NULL, rut, nombre, apellido, contraseña, tipo, area))
                self.conexion.commit()
            except Error as ex:
                print("Error de conexión: {0} ".format(ex))

    def cierreTicket(self, ticket, estdo, observacion, idUser):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                orden = "UPDATE `ticket` SET `Id_estado` = '{0}', `observación` = '{1}', `id_usuarioCierre` = '{2}' WHERE `ticket`.`Id_ticket` = {3};"
                cursor.execute(orden.format(estdo, observacion, idUser, ticket))
                self.conexion.commit()
            except Error as ex:
                print("Error de conexión: {0} ".format(ex))
    
    def editarTicket(self, filtro, id):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                orden = "UPDATE `ticket` SET {0} WHERE `ticket`.`Id_ticket` = {1};"
                cursor.execute(orden.format(filtro, id))
                self.conexion.commit()
            except Error as ex:
                print("Error de conexión: {0} ".format(ex))