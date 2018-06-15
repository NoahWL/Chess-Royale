from RoseRoyale.Server import Server

def Main():
    myServer = Server("miserver")
    try:
        myServer.initialize()
    except (KeyboardInterrupt, SystemExit):
        print("except")
        myServer.close()
    
    
    

if __name__ == "__main__":
    Main()