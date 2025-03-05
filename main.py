import sys

class Servermy:
    def __init__(self):
        self.domain = 4
        self.type = 1
        self.protocol = 1
        self.port=9000

    def socketcreator(self, domain, type, protocol):
        error="is not true"
        temp=True
        if domain != self.domain:
            error="domain number "+error
            temp=False
        if type != self.type:
            error="type number "+error
            temp=False
        if protocol != self.protocol:
            error="protocol number "+error
            temp=False

        if temp:
            print("server is created")
            print("Server: Server is listening")
            return 1
        else:
            print(error)
            return 0

    def serveraccept(self, client_port):
        if client_port == self.port:
            print("Server: Connected to the server")
        else:
            print("Server: Connection denied.")
            sys.exit(0)

    def serverreader(self, message):
        print(f"Server: Client Address= {self.port}-{self.port} , {self.port}")
        if message == f"Access{self.port}":
            print(f"Server: Message is {message} access permitted")
        elif message == "end":
            print("Server: Server closed")
            sys.exit(0)
        else:
            print("Server: Access Denied")

class Clientmy:
    def __init__(self):
        self.domain = 4
        self.type = 1
        self.protocol = 1

    def clientcreator(self, domain, type, protocol):
        if domain == self.domain and type == self.type and protocol == self.protocol:
            print("client is created")
            print("Client: Client is ready to connection")
            return 1
        else:
            return 0

    def clientconnect(self, server):
        print("Client: Send connection demand to the server")
        port = int(input("Client: Enter the port number: \n"))
        server.serveraccept(port)

    def clientwriter(self, server):
        while True:
            message = input("Client: Enter the message: \n")
            server.serverreader(message)

if __name__ == "__main__":
    # Set domain, type, and protocol
    uDomain = int(input("Enter domain number: \n"))
    uType = int(input("Enter type number: \n"))
    uProtocol = int(input("Enter protocol number: \n"))

    # Create and verify domain, type, and protocol for server
    server = Servermy()
    verifyServer=server.socketcreator(uDomain, uType, uProtocol)
    
    # Create and verify domain, type, and protocol for client
    client = Clientmy()
    verifyClient=client.clientcreator(uDomain, uType, uProtocol)

    if verifyServer and verifyClient:
      client.clientconnect(server)
      client.clientwriter(server)
    # Client writes messages to server
    sys.exit(0)