import vk_api
import psycopg2
from config import host, user, password, db_name





# try:
# 	conn = psycopg2.connect(
# 		host=host,
# 		user = user,
# 		password = password,
# 		database = db_name,
# 	)

# 	conn.autocommit = True

	# with conn.cursor() as cursor:
	# 	cursor.execute(
	# 		"SELECT * FROM users;"
	# 	)
	# 	print(f'SERVER VERSION: {cursor.fetchone()}' )

	# with conn.cursor() as cursor:
	# 	cursor.execute(
	# 		"""INSERT INTO users (id, name, gender, age, 
	# 		city, looking_for, description, photo_link) VALUES
	# 		(1337, 'Артем', 'муж', '19', 
	# 		'Владивосток', 'гетеро', 'Я наруто узумаки!', 'photo_13123632_3234521'); """
	# 	)

	# with conn.cursor() as cursor:
	# 	cursor.execute(
	# 		"""CREATE TABLE users(
	# 		id INT,
	# 		name VARCHAR(15),
	# 		gender VARCHAR(6),
	# 		age INT,
	# 		city VARCHAR(30),
	# 		looking_for VARCHAR(6),
	# 		description VARCHAR(500),
	# 		photo_link VARCHAR(50)
	# 		);"""
	# 	)
	# print('done')

# except psycopg2.Error as e:
# 	print(f'PSQL ERROR WHILE CONNECT')
# 	print(e)
# finally:
# 	if conn:
# 		conn.close()
# 		# print('PSQL CONNECTION CLOSED')

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

	def insert_user_info(self, data, table_name):
		"""Вставляет в БД словарь с данными о пользователе
			[id, name, gender, age, city, looking_for, description, photo_link]"""
		with self.connection.cursor() as cursor:
			cursor.execute(
				f"""INSERT INTO {table_name} (id, name, gender, age, 
				city, looking_for, description, photo_link) VALUES
				({data['id']}, '{data['name']}', '{data['gender']}', '{data['age']}', '{data['city']}', 
				'{data['looking_for']}', '{data['description']}', '{data['photo_link']}'); """
			)
	
	def get_users(self, data, table):
		"""Возвращает список пользователей из БД по фильтру из data"""
		"""Бля чуваки ебать я щас накуренный время 20:53 и я попробую чуток покодить хотя мне 
		наверное скоро станет похуй ))"""
		with self.connection.cursor() as cursor:
			cursor.execute(
				f"""SELECT * FROM {table} WHERE city={data['city']} AND gender={data['looking_for']} LIMIT 10"""
			)
			return cursor.fetchone()

	def get_version(self):
		"""Возвращает версию сервера psql в формате строки"""
		with self.connection.cursor() as cursor: 		#TODO: Оберни через декораторы
			cursor.execute(
				f"""SELECT version(); """
			)
			return str(cursor.fetchone())


#тещу как работает класс, не вызывают метод Get_users()

data = {'id': 5214, 'name': 'Dima', 'age': 18, 'city': 'vladivostok',  	#TODO: НЕ ПРИНИМАЕТ АЙДИ ВЫШЕ ОПРЕДЛЕННОГО ЗНАЧЕНИЯ
		'gender': 'man', 'looking_for': 'woman', 'description': 'hello world',
		'photo_link': 'photo_1434234_432432'}

db = DataBase(host, user, password, db_name)

db.to_connect()
print(db.get_version())

db.insert_user_info(data, 'users')
db.close_connection()


# db1 = DataBase('root', '1234', 8080, 'bot_users')

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