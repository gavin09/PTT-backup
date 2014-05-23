import ConfigParser
import sys
import re

def getRule():
   config = ConfigParser.ConfigParser()
   config.optionform = str
   config.read('config.ini')
   return config

def getBoardFromFile(filename):
   f = open(filename, 'r')
   boards = f.readlines()
   f.close()
   return boards

def getRuleFromFile(filename):
   f = open(filename, 'r')
   rules = f.readlines()

   for i in range(len(rules)):
      rules[i] = re.sub('\n', '', rules[i])
   f.close()
   return rules


