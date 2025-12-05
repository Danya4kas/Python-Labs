import socket
import threading
import json

HOST = "0.0.0.0"
PORT = 8888

clients = {}
positions = {}


def broadcast(data, exclude_client=None):
    message = json.dumps(data, ensure_ascii=False).encode("utf-8")
    for client in clients:
        if client != exclude_client:
            try:
                client.send(message + b"\n")
            except:
                pass


def handle_client(conn):
    username = None
    try:
        username = conn.recv(1024).decode("utf-8").strip()
        if not username:
            return
        
        clients[conn] = username
        positions[username] = (0.0, 0.0)
        
        print(f"{username} підключився")
        
        broadcast({
            "type": "message",
            "user": "SERVER",
            "text": f"{username} підключився"
        }, exclude_client=conn)
        
        while True:
            data = conn.recv(1024)
            if not data:
                break
            
            for raw in data.splitlines():
                try:
                    msg = json.loads(raw.decode("utf-8"))
                except:
                    continue
                
                if msg["type"] == "position":
                    positions[username] = (msg["x"], msg["y"])
                    broadcast(msg, exclude_client=conn)
                    print(f"{username}: ({msg['x']}, {msg['y']})")
                
                if msg["type"] == "message":
                    broadcast(msg, exclude_client=conn)
                    print(f"{username}: {msg['text']}")
    
    except Exception as e:
        print(f"Помилка: {e}")
    
    finally:
        username = clients.get(conn, "unknown")
        print(f"{username} відключився")
        clients.pop(conn, None)
        positions.pop(username, None)
        broadcast({
            "type": "message",
            "user": "SERVER",
            "text": f"{username} відключився"
        })
        conn.close()


def start():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Сервер на {HOST}:{PORT}")
    
    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn,), daemon=True).start()


if __name__ == "__main__":
    start()
