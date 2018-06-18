from RoseRoyale.Server import Server
from RoseRoyale.ClientConnection import ClientConnection
from threading import Thread
import time

def Main():
    myServer = Server("miserver")
    serverThread = Thread(target = myServer.initialize, args=())
    serverThread.start()
    
    time.sleep(1.0)
    cc = ClientConnection("testName")
    cc.connect('127.0.0.1')
    time.sleep(1.0)

if __name__ == "__main__":
    Main()