# coding=utf-8
import sys
import re

ArticlePattern = re.compile("(^\s*[0-9]+)")

class Parser:
   def __init__(self):
      self.debug = 0

   def openFile(self):
      reader = open('dump.txt', 'r')
      return reader.read()

   def Article(self, message):
      if self.debug is 1:
         message = self.openFile()

      if self.debug is 1:
         print repr(message)

      # \xe2\x97\x8f is ●
      # 3H is the position of article id
      lines = re.split('3H|\\xe2\\x97\\x8f|\\r\\n ', message)

      for line in lines:

         if self.debug is 1:
            # PRINT RAW STRING
            print repr(line)

         if ArticlePattern.search(line):
            print ArticlePattern.search(line).group(0).strip()
