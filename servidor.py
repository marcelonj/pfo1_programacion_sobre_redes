import socket
from baseDatos import baseDatos

direccion_ip = "localhost"

#Se establece comunicación con la base de datos
try:
    db = baseDatos()
except:
    print("No se pudo establecer conexión con la base de datos.")
    exit()

def iniciar_socket():
    #Configuración del socket para usar IPV4 y TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((direccion_ip, 5000))
    server_socket.listen(1)
    return server_socket

def recibir_mensajes(server_socket):
    #Se escuchan las conexiones entrantes para aceptarlas y procesarlas
    print("Esperando conexión de un cliente...")
    client_socket, client_address = server_socket.accept()
    print("Cliente conactado.")
    client_socket.send(b"Hola, cliente! Bienvenido al servidor. Enviame tu mensaje para guardar")
    
    #Procesamos los mensajes hasta que el cliente cierra la conexión
    while True:
        data = client_socket.recv(1024)
        if not data:
            print("Cliente desconectado.")
            break
        mensaje_usuario = data.decode()
        escritura = db.insertarRegistro(mensaje_usuario, client_address[0])
        if escritura[0]:
            mensaje = f"Mensaje recibido: {escritura[1]}"
            client_socket.send(mensaje.encode('utf-8'))


#Ejecutamos el servidor, que se mantiene activo hasta que se recibe CTRL+C en la consola
try:
    #Se inicia el servidor
    servidor = iniciar_socket()

    #Empezamos a escuchar las conexiones entrantes
    while True:
        recibir_mensajes(servidor)
except KeyboardInterrupt:
    print("Servidor detenido.")