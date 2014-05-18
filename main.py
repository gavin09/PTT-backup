import sys
import Config
from PTTBot import PTTBot

if __name__ == '__main__':
   account = sys.argv[1]
   passwd  = sys.argv[2]

   boards  = Config.getBoardFromFile('boards.txt')
   rules   = Config.getRuleFromFile('rules.txt')

   pttbot = PTTBot()
   pttbot.login(account, passwd)

   for board in boards:
      pttbot.goBoard(board)
      for rule in rules:
         articles = pttbot.search(rule)
#         for article in articles:
#            pttbot.backup(article)
#
   pttbot.leave()

