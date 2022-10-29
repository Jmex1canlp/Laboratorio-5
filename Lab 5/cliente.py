#Se importa el módulo
import socket
import sys
import random
import diffiehellman
import Des
#Variables
host = 'localhost'
port = 8050
#Creación de un objeto socket (lado cliente)
obj = socket.socket() 
#Conexión con el servidor. Parametros: IP (puede ser del tipo 192.168.1.1 o localhost), Puerto
obj.connect((host, port))
print("Conectado al servidor")
p = int(input("Introduzca el número primo 'p': "))
alpha = int (input("Introduzca el número 'alpha': "))
privado = int(input("Introduzca llave: "))
print("------------Llaves privadas------------------\n")
print("La llave privada de Alice es ",privado,"\n")
publico=exp_rapida(alpha,privado,p)
print("------------Llave publica------------------\n")
print("La llave publica de Alice es ",publico,'\n')
print('**********************************************')
#Instanciamos una entrada de datos para que el cliente pueda enviar mensajes
mens = raw_input("favor de enviar llave publica a servidor >> ")
#Con el método send, enviamos el mensaje
obj.send(mens)
respuesta = obj.recv(1024)
K=exp_rapida(alpha,int(respuesta),p)
obj.send(K)
respuesta = obj.recv(1024)
if K == int(respuesta):
    print('conectando con servidor descriptando mensaje enviado')
    mensajecif=Des.Mensajedecodificado()
    print('decriptacion hecha')
else:
    print('clave incorrecta')
#Cerramos la instancia del objeto servidor
obj.close()

#Imprimimos la palabra Adios para cuando se cierre la conexion
print("Conexión cerrada")
