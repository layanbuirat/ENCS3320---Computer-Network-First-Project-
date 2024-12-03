import socket

def start_client(server_ip, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        while True:
            message = input("Enter your message to server: ")
            client_socket.sendto(message.encode('utf-8'), (server_ip, server_port))
            
            response, _ = client_socket.recvfrom(1024)
            print(f"Server response: {response.decode('utf-8')}")
    
    except KeyboardInterrupt:
        print("Client is shutting down.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    server_ip = '127.0.0.1'  # Replace with the server's IP address
    server_port = 1439    # Must match the server port
    start_client(server_ip, server_port)

