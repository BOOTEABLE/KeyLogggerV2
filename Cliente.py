import socket
import time
import os
import threading

def enviar_archivo_automatico(sock, ruta, intervalo):
    while True:
        time.sleep(intervalo)
        if os.path.exists(ruta):
            with open(ruta, "r") as f:
                contenido = f.read()
            if contenido.strip():
                # Enviamos con una etiqueta especial para que el servidor lo reconozca
                sock.sendall(f"FILE_DATA:{contenido}".encode())

def recibir_mensajes(sock):
    while True:
        try:
            data = sock.recv(1024).decode()
            if data: print(f"\n[Servidor]: {data}\n>> ", end="")
        except: break

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9999))

threading.Thread(target=enviar_archivo_automatico, args=(sock, ".data.txt", 10), daemon=True).start()
threading.Thread(target=recibir_mensajes, args=(sock,), daemon=True).start()

while True:
    msg = input(">> ")
    sock.send(msg.encode())