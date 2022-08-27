class DataBase:
	"""Класс для работы с БД"""

	__instance = None

	def __new__(cls, *args, **kwargs):
		"""паттерн Singltone"""
		if cls.__instance == None:
			cls.__instance = super().__new__(cls)
		return cls.__instance


	def __init__(self, name, psw, port):
		self.name = name
		self.psw = psw
		self.port = port

	def print_info(self):
		print(self.name, self.psw, self.port)

db1 = DataBase('root', '1234', 8080)
db2 = DataBase('toor', '5678', 8080)
print('hi')
print('hello dude')


print(id(db1), id(db2))

# db1.print_info()
# db2.print_info()






# class DataBase:
# 	"""Класс для работы с БД"""
# 	def get_data_from_db(self):
# 		"""берет информацию из дб по указанному id"""
# 		print("вызов из бд")

# class CurrentUser:
# 	def __init__(self, name='Vasya', age=19):
# 		self.name = name
# 		self.age = age
# 		print('вызов __init__ внутри CurrentUser')
# 		db.get_data_from_db()

# db = DataBase()
# user = CurrentUser()