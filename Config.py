import sys
import re

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
