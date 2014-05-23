import Config

if __name__ == '__main__':
   config = Config.getRule()
   sections = config.sections()
   for section in sections:
      print section
