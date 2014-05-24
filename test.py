import Config

if __name__ == '__main__':
   # == Config ==
   config = Config.ConfigReader('config.ini.sample')
   # Get account
   assert('myaccount' == config.getAccount())
   # Get password
   assert('12345678'  == config.getPassword())

