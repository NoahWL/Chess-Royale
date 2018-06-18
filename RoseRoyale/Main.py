from RoseRoyale.Server import Server
from RoseRoyale.ClientConnection import ClientConnection
from threading import Thread
import RoseRoyale.Graphics
import time

def Main():
    setupServer()
    time.sleep(1) # Temp
    setupServerConnection()
    RoseRoyale.Graphics.init() # Start main game loop in this thread

def setupServerConnection():
    cc = ClientConnection("testName")
    cc.connect('127.0.0.1')
    
def setupServer():
    myServer = Server("miserver") # Create server instance
    serverThread = Thread(target = myServer.initialize, args=())
    serverThread.start() # Start server in its own thread

if __name__ == "__main__":
    Main()