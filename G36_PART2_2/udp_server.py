import socket

def start_server(port):
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Bind the socket to the address and port
    server_socket.bind(('0.0.0.0', port))
    
    print(f"Server is listening on port {port}")
    
    client_counter = 1  # Counter to assign unique IDs to clients
    client_map = {}     # Dictionary to map client addresses to IDs
    reverse_client_map = {}  # Dictionary to map IDs to addresses
    
    try:
        while True:
            # Receive message from a client
            message, client_address = server_socket.recvfrom(1024)
            decoded_message = message.decode('utf-8')
            
            # Map client address to a unique client ID
            client_id = None
            for cid, address in client_map.items():
                if address == client_address:
                    client_id = cid
                    break
            
            if client_id is None:
                # New client, assign a new ID
                client_id = f"Client {client_counter}"
                client_counter += 1
                client_map[client_id] = client_address
                reverse_client_map[client_address] = client_id
            
            # Print received message with client ID
            print(f"Message from {client_id}: {decoded_message}")
            
            # Prompt the server user to enter a response to this client
            response_message = input(f"Enter your message to {client_id}: ")
            
            # Send a response back to the client
            server_socket.sendto(response_message.encode('utf-8'), client_address)
    
    except KeyboardInterrupt:
        print("Server is shutting down.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    port = 1439  # Example port number based on student ID
    start_server(port)
