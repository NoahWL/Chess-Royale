from threading import Thread
import time
import socket

class ClientConnection:
    def __init__(self, username):
        self.username = username
        print("Client connection starting...")
        
    def connect(self, IP):
        connection = socket.socket()
        connection.connect((IP, 2396))
        self.connectionManager = ConnectionManager(connection)
        self.connectionManager.start()
        
    def sendMessage(self, message):
        self.connectionManager.sendMessage(message)

class ConnectionManager:
    def __init__(self, connection):
        Thread.__init__(self)
        self.connection = connection
        self.shouldRun = True
        
    def start(self):
        self.listener = ServerListener(self, self.connection)
        self.writer = ServerWriter(self, self.connection)
        self.listener.start()
        self.writer.start()
        
    def read(self):
        return self.listener.getMessages()
    
    def sendMessage(self, message):
        self.writer.sendMessage(message)
        
    def close(self):
        self.shouldRun = False
    
class ServerListener(Thread):
    def __init__(self, manager, connection):
        Thread.__init__(self)
        self.manager = manager
        self.connection = connection
        self.receivedMessages = []
        
    def run(self):
        self.receivedMessages.append("Test message")
    
    def getMessages(self):
        messages = self.receivedMessages.copy()
        self.receivedMessages.clear()
        return messages
        
class ServerWriter(Thread):
    def __init__(self, manager, connection):
        Thread.__init__(self)
        self.manager = manager
        self.connection = connection
        self.messages = []
        self.hasMessages = False
        print("Client writer created")
        
    def run(self):
        while self.manager.shouldRun:
            if len(self.messages) > 0:
                print("Writing message: " + self.messages[0])
                self.connection.sendall(self.messages[0].encode("utf-8"))
                del self.messages[0]
            time.sleep(0.001)
                
    def sendMessage(self, message):
        self.messages.append(message)