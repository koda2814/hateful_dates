from multiprocessing import connection
import vk_api
import psycopg2
from config import host, user, password, db_name



try:
	conn = psycopg2.connect(
		host=host,
		user = user,
		password = password,
		database = db_name,
	)

	conn.autocommit = True

	with conn.cursor() as cursor:
		cursor.execute(
			"SELECT version();"
		)
		print(f'SERVER VERSION: {cursor.fetchone()}' )

	with conn.cursor() as cursor:
		cursor.execute(
			"""CREATE TABLE users(
			id INT,
			name VARCHAR(15),
			gender VARCHAR(6),
			age INT,
			city VARCHAR(30),
			orientation VARCHAR(6),
			description VARCHAR(500),
			photo_link VARCHAR(50)
			);"""
		)
	print('done')

except psycopg2.Error as e:
	print(f'PSQL ERROR WHILE CONNECT')
	print(e)
finally:
	if conn:
		conn.close()
		print('PSQL CONNECTION CLOSED')

class DataBase:
	"""Класс для работы с БД"""

	__instance = None
	def __new__(cls, *args, **kwargs):
		"""паттерн Singltone"""
		if cls.__instance == None:
			cls.__instance = super().__new__(cls)
		return cls.__instance


	def __init__(self, host, user, password, db_name):
		self.host = host
		self.user = user
		self.password = password
		self.db_name = db_name

	def to_connect(self):
		self.connection = psycopg2.connect(
		host=self.host,
		user = self.user,
		password =self.password,
		database =self.db_name
	)
		self.connection.autocommit=True

	def close_connection(self):
		if self.connection:
			self.connection.close()

db1 = DataBase('root', '1234', 8080, 'bot_users')

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