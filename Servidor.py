import socket
import threading

def manejar_recepcion(conn):
    while True:
        try:
            recibido = conn.recv(1024).decode()
            if not recibido: break
            
            # PASO 3: Si el mensaje empieza con la etiqueta, NO se imprime
            if recibido.startswith("FILE_DATA:"):
                contenido_archivo = recibido.replace("FILE_DATA:", "")
                # Guardamos lo recibido en un archivo nuevo en el lado del servidor
                with open("reporte_recibido.txt", "w") as f:
                    f.write(contenido_archivo)
                # Opcional: imprimir un aviso pequeño o nada
                # print("\n[Sistema]: Archivo de registro actualizado.") 
            else:
                # Si es un mensaje normal del chat, sí se imprime
                print(f"\n[Cliente]: {recibido}\nSVR >> ", end="")
        except: break

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))
server.listen(1)
print("Servidor escuchando...")

conn, addr = server.accept()
threading.Thread(target=manejar_recepcion, args=(conn,), daemon=True).start()

while True:
    msg = input("SVR >> ")
    conn.send(msg.encode())