import socket

#Configuración del socket para usar IPV4 y TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Intentamos conectarnos al servidor
try:
    client_socket.connect(("localhost", 5000))
    message = client_socket.recv(1024)
    print(f"Recibido del servidor: {message.decode()}")

    mensaje = input("Ingrese el mensaje para el servidor: ")

    while mensaje != "éxito":
        client_socket.send(mensaje.encode('utf-8'))
        message = client_socket.recv(1024)
        print(f"Recibido del servidor: {message.decode()}")
        mensaje = input("Ingrese el mensaje para el servidor: ")

    client_socket.close()
except ConnectionError:
    print("No se pudo establecer conexión con el servidor")
finally:
    print("Cliente finalizado")