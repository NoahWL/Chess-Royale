from threading import Thread
import time
import socket

class Server:
    def __init__(self, name):
        self.serverName = name
        self.shouldRun = True
        self.clients = []
    
    def initialize(self):
        print("Server " + self.serverName + " starting...")
        connectionListenerThread = Thread(target=self.ConnectionListener, args=())
        connectionListenerThread.start()
        
        time.sleep(0.5)
        while self.shouldRun:
            for client in self.clients:
                messages = client.read()
                if messages != None:
                    for message in messages:
                        print("Message from client:" + message)
            time.sleep(0.001)
        
        for client in self.clients:
            client.close()
        
    def ConnectionListener(self):
        print("connection listener started")
        serverSocket = socket.socket()
        print("socket created")
        serverSocket.bind(("127.0.0.1", 2396))
        print("socket bound")
        serverSocket.listen(5)
        print("socket listening")
        
        while self.shouldRun:
            print("waiting for clients")
            clientConnection, addressInfo = serverSocket.accept()
            print("connection requested")
            cHandler = ClientHandler(self, clientConnection)
            print("created client handler")
            cHandler.start()
            print("started client handler")
            self.clients.append(cHandler)
            print("added client handler to client list")
            
    def close(self):
        self.shouldRun = False

class ClientHandler:
    def __init__(self, server, clientConnection):
        Thread.__init__(self)
        self.theServer = server
        self.shouldRun = True
        self.connection = clientConnection
        
    def start(self):
        self.listener = ClientListener(self, self.connection)
        self.writer = ClientWriter(self, self.connection)
        self.listener.start()
        self.writer.start()
        
    def read(self):
        return self.listener.getMessages()
    
    def sendMessage(self, message):
        self.writer.sendMessage(message)
        
    def close(self):
        self.shouldRun = False
    
class ClientListener(Thread):
    def __init__(self, handler, connection):
        Thread.__init__(self)
        self.theHandler = handler
        self.receivedMessages = []
        self.connection = connection
        print("Client listener created")
        
    def run(self):
        buffer = ''
        while self.theHandler.shouldRun:
            received = self.connection.recv(2048)
            buffer += received.decode('utf-8')
            if buffer != '':
                self.receivedMessages.append(buffer[0:buffer.find("!end")])
            time.sleep(0.001)
                
        
    
    def getMessages(self):
        messages = self.receivedMessages.copy()
        self.receivedMessages.clear()
        return messages
        
class ClientWriter(Thread):
    def __init__(self, handler, connection):
        Thread.__init__(self)
        self.theHandler = handler
        self.connection = connection
        self.messages = []
        self.hasMessages = False
        print("Client writer created")
        
    def run(self):
        while self.theHandler.shouldRun:
            if len(self.messages) > 0:
                print("Writing message: " + self.messages[0])
                del self.messages[0]
            time.sleep(0.001)
                
    def sendMessage(self, message):
        self.messages.append(message)