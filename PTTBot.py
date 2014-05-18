import socket
import time

class PTTBot:
   def __init__(self):
      self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      self.socket.settimeout(60)

      self.leaveCount = 0

      self.debug = 1
   def login(self, account, password):
      self.socket.connect(('ptt.cc',23))
      self.showScreen()

      self.sendMsg(account + '\r' + password + '\r')
      self.showScreen()

      # Jump to main menu
      self.sendMsg('\r')
      self.showScreen()

   def sendMsg(self, message):
      if self.debug is 1:
         print message
      self.socket.send(message)

   def recvMsg(self, message):
      self.socket.recv(65535).decode('big5', 'ignore')

   def leave(self):

      # If there is a search, we need more left arrow to leave
      for i in range(0, self.leaveCount):
         self.sendMsg('\x1bOD')
         self.showScreen()

      # left arrow
      self.sendMsg('\x1bOD')
      self.showScreen()

      self.sendMsg('q')
      self.showScreen()

      self.sendMsg('\x1bOD')
      self.showScreen()

      self.sendMsg('\r')
      self.showScreen()

      self.sendMsg('y')
      self.showScreen()

      self.sendMsg('\r')
      self.showScreen()

      self.socket.close()
   def goBoard(self, board):
      self.sendMsg('s')
      self.showScreen()

      self.sendMsg(board + '\r')
      self.showScreen()
   def search(self, rule):
      # Fix, we need skip animation
      self.sendMsg('Z')
      self.showScreen()

      self.sendMsg('Z')
      self.showScreen()

      self.sendMsg(rule)
      self.showScreen()

      self.leaveCount = self.leaveCount + 1

#   def backup(self):
#
   def showScreen(self):
      if self.debug is 1:
         time.sleep(5)
      else:
         time.sleep(1)

      msg = self.socket.recv(65535).decode('big5', 'ignore')
      print msg
      return msg
