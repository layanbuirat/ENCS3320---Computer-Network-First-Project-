import socket

def replace_vowels(input_string):
    # Replace vowels with '#'
    return ''.join('#' if char in 'aeiouAEIOU' else char for char in input_string)

def start_server(port):
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the address and port
    server_socket.bind(('localhost', port))
    
    # Listen for incoming connections
    server_socket.listen(1)
    print(f'Server listening on port {port}...')
    
    while True:
        # Accept a connection
        client_socket, client_address = server_socket.accept()
        print(f'Connection from {client_address}')
        
        try:
            # Receive data from the client
            data = client_socket.recv(1024).decode()
            print(f'Received data: {data}')
            
            # Replace vowels in the received data
            modified_data = replace_vowels(data)
            print(f'Sending modified data: {modified_data}')
            
            # Send the modified data back to the client
            client_socket.sendall(modified_data.encode())
        finally:
            # Close the client connection
            client_socket.close()

if __name__ == "__main__":
    port_number = 1439  # Replace with the desired port number based on student ID = 1211439
    start_server(port_number)
