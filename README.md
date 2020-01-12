# ATM
# app is using Redis as database.
# redis could run at localhost and config right database
(default setting is "db = redis.Redis(host="localhost", port=6379, db=1)")
# download all files 
  run app by type python app.py in your terminal 


class Fetcher:
	def __inti__(self, database,bank):
		self.datbase = database
		self.bank = bank
	def get(self,  name):
		balance = self.database.get(name)
		return balance
		

TD_fetcher = Fetcher(redis, TD)
Cibc_fetcher = Fetcher(sql, cibc) 

Jiaqi_Td_money=TD_fetcher(jiaqi)
