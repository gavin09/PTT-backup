# coding=utf-8
import socket
import time
import select

Enter      = '\r'
UpArrow    = '\x1bOA'
DownArrow  = '\x1bOB'
RightArrow = '\x1bOC'
LeftArrow  = '\x1bOD'

class PTTBot:
   def __init__(self):
      self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      self.socket.settimeout(60)

      self.debug = 1
   def login(self, account, password):
      self.socket.connect(('ptt.cc',23))
      self.recvMsg()

      self.sendMsg(account + Enter + password + Enter)
      self.recvMsg()

      # Jump to main menu
      self.sendMsg(Enter)
      self.recvMsg()

   def sendMsg(self, message):
      if self.debug is 1:
         print message
      self.socket.send(message)

   def recvMsg(self):
      if self.debug is 1:
         time.sleep(3)

      timeout_in_seconds = 1
      ready = select.select([self.socket], [], [], timeout_in_seconds)

      if ready[0]:
         msg = self.socket.recv(65535).decode('big5', 'ignore')
         if self.debug is 1:
            self.showScreen(msg)
         return msg
      else:
         if self.debug is 1:
            print 'receive msg timeout'
         return ''

   def leave(self):

      while u"主功能表" not in self.recvMsg():
         self.sendMsg(LeftArrow)

      self.sendMsg(LeftArrow)
      self.recvMsg()

      self.sendMsg(Enter)
      self.recvMsg()

      self.sendMsg('y')
      self.recvMsg()

      self.sendMsg(Enter)
      self.recvMsg()

      self.socket.close()
   def goBoard(self, board):
      self.sendMsg('s')
      self.recvMsg()

      self.sendMsg(board + Enter)

      if u"請按任意鍵繼續" in self.recvMsg():
         self.sendMsg(Enter)
         self.recvMsg()
   def search(self, rule):
      self.sendMsg('Z')
      self.recvMsg()

      self.sendMsg(rule + Enter)
      self.recvMsg()

#   def backup(self):
#
   def showScreen(self, message):
      print message
