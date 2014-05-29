# coding=utf-8
import sys
import re
import time
import os

class Parser:
   def __init__(self):
      self.debug = 0

   def Article(self, message):
      if self.debug is 1:
         print repr(message)

      # Start with a space,        AricleNumber
      ArticlePattern = re.compile("(^\s*[0-9]+)")
      DeleteArticlePattern = re.compile(u'(本文已被刪除)|(已被\w+刪除)')

      # To figure unread articles           ArticleNumber
      #                                         XXXXX   +
      UnReadArticlePattern = re.compile('(^\s*[0-9]+)\s\+')

      # \xe2\x97\x8f is ●
      # 3H is the position of article id
      lines = re.split('3H|\\xe2\\x97\\x8f|\\r\\n', message)

      articles = []
      for line in lines:

         if self.debug is 1:
            # PRINT RAW STRING
            print repr(line)

         if ArticlePattern.search(line) and UnReadArticlePattern.search(line):

            # This article exists
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

