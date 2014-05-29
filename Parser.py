# coding=utf-8
import sys
import re
import time
import os


ArticlePattern = re.compile("(^\s*[0-9]+)")

class Parser:
   def __init__(self):
      self.debug = 0

   def Article(self, message):
      if self.debug is 1:
         print repr(message)

      DeleteArticlePattern = re.compile(u'(本文已被刪除)|(已被\w+刪除)')

      # \xe2\x97\x8f is ●
      # 3H is the position of article id
      lines = re.split('3H|\\xe2\\x97\\x8f|\\r\\n', message)

      articles = []
      for line in lines:

         if self.debug is 1:
            # PRINT RAW STRING
            print repr(line)

         if ArticlePattern.search(line):

            if re.search(u'(本文已被刪除)|(已被\w+刪除)', line) is None:
               articleID = ArticlePattern.search(line).group(0).strip()
               if self.debug is 1:
                  print articleID

               articles.append(articleID)

      return articles

   def getWebUrl(self, message):
      WebUrlPattern  = re.compile("http://www.ptt.cc/bbs/(\S)+(.html)")

      if(WebUrlPattern.search(message)):
         url = WebUrlPattern.search(message).group(0).strip()
         return url
   def getTitle(self, message):
      CurrentArticlePattern = re.compile(u'●')
      ArticleNamePattern = re.compile(u"(□|R:|轉).+(\S)")
      #print message
      # \u25cf is light ●
      # \u25a1 is □

      # First, split message into lines
      # find current line by light ●
      lines = re.split('\\r\\n', message)
      for line in lines:
         os.system('clear')
         if CurrentArticlePattern.search(line):
            # get article
            # article may start from □, R:, 轉
            articleName = ArticleNamePattern.search(line).group(0).strip()
            print articleName
            time.sleep(1)
            return articleName

