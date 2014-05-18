import sys

def getBoardFromFile(filename):
   f = open(filename, 'r')
   boards = f.readlines()
   f.close()
   return boards

def getRuleFromFile(filename):
   f = open(filename, 'r')
   rules = f.readlines()
   f.close()
   return rules
