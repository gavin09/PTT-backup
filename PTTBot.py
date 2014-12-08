# coding=utf-8
import socket
import time
import select
from Parser import Parser
import os
import sys

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
      message = self.recvMsg()

      if u'您想刪除其他重複登入的連線嗎' in message:
         self.sendMsg('n' + Enter)
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
         time.sleep(1)

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
   def search(self, ruleType, target):

      if ruleType == 'num':
         self.sendMsg('Z')
      if ruleType == 'author':
         self.sendMsg('a')
      if ruleType == 'title':
         self.sendMsg('/')
         target = unicode(target, 'utf-8')
         target = target.encode('big5')
      self.recvMsg()

      self.sendMsg(target + Enter)
      self.socket.send('\f')
      message = self.recvMsg()

      if self.debug is 1:
         writer = open('dump.txt', 'w')
         writer.write(message.encode('utf-8', 'ignore'))
         writer.close()

      return Parser().Article(message)

   def record(self, article):
      self.sendMsg(article + Enter)
      self.recvMsg()

      self.sendMsg('Q')
      message = self.recvMsg()

      if self.debug is 1:
         writer = open('case.txt', 'w')
         writer.write(message.encode('utf-8', 'ignore'))
         writer.close()

      url = Parser().getWebUrl(message)
      title = Parser().getTitle(message)

      os.system('clear')
      writer = open('result.txt', 'a')
      writer.write(url.encode('ascii','ignore') + '\n')
      writer.write(title.encode('utf-8','ignore') + '\n')
      writer.write('================================\n')
      writer.close()

      self.sendMsg(Enter)
      self.recvMsg()

      # Make It read
      self.sendMsg(RightArrow)
      self.recvMsg()

      self.sendMsg(LeftArrow)
      self.recvMsg()

   def showScreen(self, message):
      os.system('clear')
      print message
