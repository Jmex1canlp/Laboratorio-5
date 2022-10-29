from Crypto.Cipher import DES
K=b'Toror'
I=b'vino'

def encriptar():
    file = open("mensajeentrada.txt", "r")
    mensaje_entrada = str(file.readline().lower()).encode()
    file.close()
    mensaje_entrada = "".join(mensaje_entrada)
    mensaje_entrada = mensaje_entrada.encode("ASCII")
    # se calcula el padding a añadir
    T = len(mensaje_entrada)%8
    mensaje_entrada = mensaje_entrada+b' '*(8-T) if T!= 0 else mensaje_entrada+ b''
    llave = DES.new(key, DES.MODE_CFB)
    mensaje_codificado = llave.encrypt(mensaje_entrada)
    return mensaje_codificado

def encriptar3des()
file = open("mensajeentrada.txt", "r")
    mensaje_entrada = str(file.readline().lower()).encode()
    file.close()
    mensaje_entrada = "".join(mensaje_entrada)
    mensaje_entrada = mensaje_entrada.encode("ASCII")
    # se calcula el padding a añadir
    T = len(mensaje_entrada)%8
    mensaje_entrada = mensaje_entrada+b' '*(8-T) if T!= 0 else mensaje_entrada+ b''
    llave = DES.new(key, DES.MODE_CFB)
    llave2 = DES.new(key, DES.MODE_CFB)
    mensaje_codificado = llave.encrypt(mensaje_entrada)
    mensaje_codificado = llave2.decrypt(mensaje_entrada)
    mensaje_codificado = llave.encrypt(mensaje_entrada)
    return mensaje_codificado

def Mensajecodificado(mensaje_codificado):
    file = open("Mensaje_Codificado.txt", "w+")
    file.write(str(mensaje_codificado))
    file.close()

def Mensajedecodificado(mensaje_codificado):
    llave = DES.new(key, DES.MODE_CFB, iv)
    mensaje_recibido = llave.decrypt(mensaje_codificado).decode()
    file = open("mensajerecibido.txt", "w+")
    file.write(mensaje_recibido)
    file.close()

def Mensajedecodificado3des(mensaje_codificado):
    llave = DES.new(key, DES.MODE_CFB)
    llave2 = DES.new(key, DES.MODE_CFB)
    mensaje_recibido = llave.decrypt(mensaje_codificado).decode()
    mensaje_recibido = llave2.encrypt(mensaje_codificado).decode()
    mensaje_recibido = llave.decrypt(mensaje_codificado).decode()
    file = open("mensajerecibido.txt", "w+")
    file.write(mensaje_recibido)
    file.close()
