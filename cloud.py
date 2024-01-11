import socket
import ssl
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 8443)
    # Load server certificate and private key
    server_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    server_context.load_cert_chain(certfile=r'C:\Users\Suliat\PycharmProjects\transit\cert-1.pem',
                                   keyfile=r'C:\Users\Suliat\PycharmProjects\transit\key 1.pem')
    # Wrap the socket with SSL
    server_socket = server_context.wrap_socket(server_socket, server_side=True)
    # Bind the socket to a specific address and port
    server_socket.bind(server_address)
    server_socket.listen(1)
    print("Server is listening on {}:{}".format(*server_address))
    while True:
        print("Waiting for a connection...")
        connection, client_address = server_socket.accept()
        try:
            print("Accepted connection from", client_address)
            # Receive data from the client
            data = connection.recv(1024)
            print("Received data from client:", data.decode('utf-8'))
            # processing the data
            response = "Server received your data: {}".format(data.decode('utf-8'))
            # Send a response back to the client
            connection.sendall(response.encode('utf-8'))
        finally:
            # Clean up the connection
            connection.close()
if __name__ == "__main__":
    start_server()