import sys
import Config
from PTTBot import PTTBot

if __name__ == '__main__':
   config   = Config.ConfigReader('config.ini')
   account  = config.getAccount()
   passwd   = config.getPassword()

   pttbot = PTTBot()
   pttbot.login(account, passwd)

   sections = config.sections()

   for section in sections:
      board = config.get(section, 'board')
      pttbot.goBoard(board)

      ruleType   = config.get(section, 'Type')
      ruleTarget = config.get(section, 'Target')
      articles = pttbot.search(ruleType, ruleTarget)
#     for article in articles:
#        pttbot.backup(article)
#
   pttbot.leave()


