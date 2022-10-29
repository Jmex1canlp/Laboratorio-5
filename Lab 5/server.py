#Se importa el módulo
import socket
import sys
import random
from diffiehellman import exp_rapida
from Des
#instanciamos un objeto para trabajar con el socket
ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Puerto y servidor que debe escuchar
ser.bind(("localhost", 8050))
#Aceptamos conexiones entrantes con el metodo listen. Por parámetro las conexiones simutáneas.
ser.listen(5)
p = int(input("Introduzca el número primo 'p': "))
alpha = int (input("Introduzca el número 'alpha': "))
privado = int(input("Introduzca llave: "))
print("------------Llaves privadas------------------\n")
print("La llave privada de Alice es ",privado,"\n")
publico=exp_rapida(alpha,privado,p)
print("------------Llave publica------------------\n")
print("La llave publica de Alice es ",publico,'\n')
print('**********************************************')
while True:
    conexion, addr = ser.accept()
    print('nueva conexion')
    print(addr)
    Peticion=conexion.recv(1024)
    K=exp_rapida(alpha,int(Peticion),p)
    mens = raw_input("favor de enviar llave publica a servidor >> ")
    conexion.send(mens)
    respuesta = obj.recv(1024)
    conexion.send(K)
    if K == int(respuesta):
        print('conectando con cliente para mandar mensaje de entrada cifrada')
        mensajecif=Des.encriptar()
        des.Mensajecodificado(mensajecif)
        conexion.send(mensajecif)
    else:
        print('clave incorrecta')
        conexion.close()
    

    #Cerramos la instancia del socket cliente y servidor
conexion.close()
