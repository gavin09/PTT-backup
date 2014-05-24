import ConfigParser
import sys
import re

class ConfigReader:
   def __init__(self, filename):
      self.config = ConfigParser.ConfigParser()
      self.config.optionform = str
      self.config.read(filename)

   def getAccount(self):
      return self.config.get('Account', 'account')

   def getPassword(self):
      return self.config.get('Account', 'password')

   def getRule(self):
      config = ConfigParser.ConfigParser()
      config.optionform = str
      config.read('config.ini')
      return config
   
   def getBoardFromFile(self, filename):
      f = open(filename, 'r')
      boards = f.readlines()
      f.close()
      return boards
   
   def getRuleFromFile(self, filename):
      f = open(filename, 'r')
      rules = f.readlines()
   
      for i in range(len(rules)):
         rules[i] = re.sub('\n', '', rules[i])
      f.close()
      return rules


