"""The main module.  This starts the game and client connection or a server."""

from RoseRoyale.Server import Server
from RoseRoyale.ClientConnection import ClientConnection
from threading import Thread
import RoseRoyale.Game
import time
import random
import os

myServer = None
cc = None
username = str(random.randint(1, 100))  # Temp - assign a random username


def Main(runServer):  # Main function, starts the entire game
    if runServer:
        setupServer(username)
        
    # setupServerConnection()
    RoseRoyale.Game.initialize()
    shutdown()


def setupServerConnection():
    global cc
    cc = ClientConnection(username)
    connectionThread = Thread(target=cc.connect, args=())
    connectionThread.start()

    
def setupServer(serverName):
    # Create a server instance
    global myServer
    myServer = Server(serverName)
    # Start the instantiated server in its own thread
    serverThread = Thread(target=myServer.initialize, args=())
    serverThread.start()

    
def shutdown():
    print('Shutting down')
    if cc != None:
        cc.close()
    
    if myServer != None:
        myServer.close()
        
    time.sleep(0.5)  # Allow some time for all threads to close cleanly
    os._exit(0)  # Ensure all threads are closed (unclean but works for now)


if __name__ == "__main__":
    Main(False)
