from threading import Thread
import RoseRoyale.Game as rg
import time
import socket

theClientConnection = None


class ClientConnection:

    def __init__(self, username):
        global theClientConnection
        theClientConnection = self  # Singleton
        
        self.username = username
        self.shouldRun = True
        self.connectionManager = None
        print("Client connection starting...")
        
    def connect(self, IP):
        if IP == '' or IP == None:
            IP = '127.0.0.1'
        connection = socket.socket()
        try:
            connection.connect((IP, 2396))
        except socket.error:
            print('Could not connect to that server.')
            return
            
        self.connectionManager = ConnectionManager(connection, self.username)
        self.connectionManager.start()
        
        while self.shouldRun:  # Main server connection loop
            messages = self.connectionManager.read()
            if messages != None:
                for message in messages:
                    # print("Message from server:" + message)
                    self.handleMessage(message)
            time.sleep(0)
    
    def _sendMessage(self, message):
        self.connectionManager.sendMessage(message)
        
    def handleMessage(self, message):
        # print('handling:', message)
        messageType = message[message.find('!type') + 5 : message.find('!/type')]  # Get message messageType
        
        if messageType == 'PLAYERPOSITION':
            playerName = message[message.find('!name') + 5 : message.find('!/name')]  # Get player name
            x = message[message.find('!posX') + 5 : message.find('!/posX')]
            y = message[message.find('!posY') + 5 : message.find('!/posY')]
            direction = message[message.find('!direction') + 10 : message.find('!/direction')]
            weaponName = message[message.find('!weapon') + 7 : message.find('!/weapon')]
            
            x = int(x)
            y = int(y)
            
            if direction == 'True':
                direction = True
            else:
                direction = False
            
            rg.updateMPPlayer(playerName, x, y, direction, weaponName)
            
        elif messageType == 'SPAWNBULLET':
            owner = message[message.find('!name') + 5 : message.find('!/name')]
            bulletX = int(message[message.find('!posX') + 5 : message.find('!/posX')])
            bulletY = int(message[message.find('!posY') + 5 : message.find('!/posY')])
            bulletType = message[message.find('!bulletType') + 11 : message.find('!/bulletType')]
            bulletDirection = message[message.find('!bulletDirection') + 16 : message.find('!/bulletDirection')]
            
            if bulletDirection == 'True':
                bulletDirection = True
            else:
                bulletDirection = False
            
            rg.spawnBullet(bulletX, bulletY, bulletType, bulletDirection, owner)
        
        elif messageType == 'STARTGAME':
            rg.startGame()
            
        elif messageType == 'DAMAGE':
            print('received damage:', message)
            playerHit = message[message.find('!playerHit') + 10 : message.find('!/playerHit')]
            amount = message[message.find('!amount') + 7 : message.find('!/amount')]
            amount = int(amount)
            rg.DamagePlayer(playerHit, amount)
            
    def close(self):
        print('Disconnecting from server')
        self.shouldRun = False
        if self.connectionManager != None:
            self.connectionManager.close()
        
    """Player action commands:"""

    def sendBullet(self, bulletX, bulletY, bulletType, bulletDirection):
        bulletX = str(bulletX)
        bulletY = str(bulletY)
        bulletDirection = str(bulletDirection)
        
        message = '!typeSPAWNBULLET!/type !name' + self.username + '!/name' + '!posX' + bulletX + '!/posX !posY' + bulletY + '!/posY !bulletType' + bulletType + '!/bulletType !bulletDirection' + bulletDirection + '!/bulletDirection !end'
        self._sendMessage(message)
        
    def sendPlayerPos(self, x, y, direction, weaponName):
        direction = str(direction)
        message = '!typePLAYERPOSITION!/type !name' + self.username + '!/name !posX' + str(x) + '!/posX !posY' + str(y) + '!/posY !direction' + direction + '!/direction !weapon' + weaponName + '!/weapon !end'
        # print(message)
        self._sendMessage(message)
        
    def sendDamage(self, playerHit, amount):
        playerHit = str(playerHit)
        amount = str(amount)
        message = '!typeDAMAGE!/type !playerHit' + playerHit + '!/playerHit !amount' + amount + '!/amount !end'
        print('sending damage:', message)
        self._sendMessage(message)


class ConnectionManager:

    def __init__(self, connection, name):
        Thread.__init__(self)
        self.connection = connection
        self.shouldRun = True
        self.name = name
        
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
        self.connection.close()

    
class ServerListener(Thread):

    def __init__(self, manager, connection):
        Thread.__init__(self)
        self.manager = manager
        self.connection = connection
        self.receivedMessages = []
        
    def run(self):
        while self.manager.shouldRun:
            buffer = ''
            received = self.connection.recv(256)
            buffer += received.decode('utf-8')
            if buffer != '':
                self.receivedMessages.append(buffer[0 : buffer.find("!end")])
            time.sleep(0.001)
    
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
        nameInfo = '!typeCLIENTNAME!/type! !name' + self.manager.name + '!/name !end'
        self.connection.sendall(nameInfo.encode("utf-8"))
        print('Sent client name')
        while self.manager.shouldRun:
            if len(self.messages) > 0:
                self.connection.sendall(self.messages[0].encode("utf-8"))
                del self.messages[0]
            time.sleep(0.001)
                
    def sendMessage(self, message):
        self.messages.append(message)
