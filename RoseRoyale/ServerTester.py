"""Temporary module for running a separate server instance for testing purposes"""

from RoseRoyale.Server import Server
from threading import Thread

myServer = None
cc = None


def Main():
    setupServer()

    
def setupServer():
    global myServer
    myServer = Server("Test Server")
    serverThread = Thread(target=myServer.initialize, args=())
    serverThread.start()


if __name__ == "__main__":
    Main()