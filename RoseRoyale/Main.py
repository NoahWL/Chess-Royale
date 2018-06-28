"""The main module.  This starts the game and client connection or a server."""

import os
import random
import sys
from threading import Thread
import time

from RoseRoyale import StartScreen
from RoseRoyale.ClientConnection import ClientConnection
import RoseRoyale.Game
from RoseRoyale.Server import Server
from RoseRoyale.ServerGUI import ServerGUI

myServer = None
serverGUI = None
cc = None
username = str(random.randint(1, 1000))  # Temp - assign a random username


def Main(runServer, IP):  # Main function, starts the entire game
    if runServer:
        setupServer()
        serverGUI.startGUI()
    else:
        setupServerConnection(IP)
        RoseRoyale.Game.initialize(username, cc)
        
    shutdown()


def setupServerConnection(IP):
    global cc
    cc = ClientConnection(username)
    connectionThread = Thread(target=cc.connect, args=(IP,))
    connectionThread.start()


def setupServer():
    # Create a server instance
    global myServer
    global serverGUI
    
    # Start the instantiated server in its own thread
    myServer = Server(username)
    serverThread = Thread(target=myServer.initialize, args=())
    serverThread.start()
    
    # Create server GUI
    serverGUI = ServerGUI(myServer)


def shutdown():
    print('Shutting down')
    if cc != None:
        cc.close()
    
    if myServer != None:
        myServer.close()
        time.sleep(0.5)  # Allow some time for all threads to close cleanly
        os._exit(0)  # Ensure all threads are closed


if __name__ == "__main__":
    if getattr(sys, 'frozen', False):
        os.chdir(sys._MEIPASS)  # @UndefinedVariable
    
    Selected = StartScreen.waitOnStart()
    if Selected == None:
        pass
    else:
        Main(Selected, StartScreen.ipText)
