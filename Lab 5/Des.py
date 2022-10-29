import os
from Crypto.Cipher import DES
from secrets import token_bytes

key = token_bytes(8)    #(solo 8)
iv = token_bytes(8)    # Vector de inicialización

def encriptar():
    file = open("mensajeentrada.txt", "r")
    mensaje_entrada = str(file.readline().lower()).encode()
    file.close()
    cipher1 = DES.new(key, DES.MODE_CFB, iv)
    mensaje_codificado = cipher1.encrypt(mensaje_entrada)
    return mensaje_codificado

def Mensajecodificado(mensaje_codificado):
    file = open("Mensaje_Codificado.txt", "w+")
    file.write(str(mensaje_codificado))
    file.close()

def Mensajedecodificado(mensaje_codificado):
    cipher2 = DES.new(key, DES.MODE_CFB, iv)
    mensaje_recibido = cipher2.decrypt(mensaje_codificado).decode()
    file = open("mensajerecibido.txt", "w+")
    file.write(mensaje_recibido)
    file.close()
