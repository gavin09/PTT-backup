import socket
import time

UpArrow    = '\x1b0A'
DownArrow  = '\x1b0B'
RightArrow = '\x1b0C'
LeftArrow  = '\x1b0D'

class PTTBot:
   def __init__(self):
      self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      self.socket.settimeout(60)

      self.leaveCount = 0

      self.debug = 1
   def login(self, account, password):
      self.socket.connect(('ptt.cc',23))
      self.recvMsg()

      self.sendMsg(account + '\r' + password + '\r')
      self.recvMsg()

      # Jump to main menu
      self.sendMsg('\r')
      self.recvMsg()

   def sendMsg(self, message):
      if self.debug is 1:
         print message
      self.socket.send(message)

   def recvMsg(self):
      if self.debug is 1:
         time.sleep(3)
      else:
         time.sleep(1)

      msg = self.socket.recv(65535).decode('big5', 'ignore')

      if self.debug is 1:
         self.showScreen(msg)

      return msg

   def leave(self):

      # If there is a search, we need more left arrow to leave
      for i in range(0, self.leaveCount):
         self.sendMsg(LeftArrow)
         self.recvMsg()

      # left arrow
      self.sendMsg(LeftArrow)
      self.recvMsg()

      self.sendMsg('q')
      self.recvMsg()

      self.sendMsg(LeftArrow)
      self.recvMsg()

      self.sendMsg('\r')
      self.recvMsg()

      self.sendMsg('y')
      self.recvMsg()

      self.sendMsg('\r')
      self.recvMsg()

      self.socket.close()
   def goBoard(self, board):
      self.sendMsg('s')
      self.recvMsg()

      self.sendMsg(board + '\r')
      self.recvMsg()
   def search(self, rule):
      # Fix, we need skip animation
      self.sendMsg('Z')
      self.recvMsg()

      self.sendMsg('Z')
      self.recvMsg()

      self.sendMsg(rule + '\r')
      self.recvMsg()

      self.leaveCount = self.leaveCount + 1

#   def backup(self):
#
   def showScreen(self, message):
      print message
