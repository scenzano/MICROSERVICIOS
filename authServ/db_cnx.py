import pymysql

class DbService():

	mysql_config = {
		"user": "root",
		"passwd": "lab4",
		"host": "db", #"host": "localhost", now is db to connect to mysql container,
		"db": "spi"
	}


	def test_mysql(self):
		try:
			cnx = pymysql.connect(**self.mysql_config)#este ** lo que hace es que convierte en tuplas de parametro= "valor", 
			cursor = cnx.cursor()
			insert_test = "INSERT INTO test (id, msg) VALUES (%s, %s)"
			data = ("666", "from db_cnx")
			cursor.execute(insert_test, data)
			cnx.commit();
			cursor.close()
		except pymysql.Error as err:
			print "Failed to insert data: {}".format(err)
		finally:
			cnx.close()

	def init_mysql(self):
		try:
			cnx = pymysql.connect(**self.mysql_config)#este ** lo que hace es que convierte en tuplas de parametro= "valor", 
			cursor = cnx.cursor()
			create_users = "CREATE TABLE IF NOT EXISTS users (user_name VARCHAR(50) not null primary key, password VARCHAR(50) not null)"
			cursor.execute(create_users)
			cnx.commit();
			cursor.close()
		except pymysql.Error as err:
			print "Failed to create table: {}".format(err)
		finally:
			cnx.close()
	
	def insert_user(self,user_name,password):
		try:
			result = True
			cnx = pymysql.connect(**self.mysql_config)#este ** lo que hace es que convierte en tuplas de parametro= "valor", 
			cursor = cnx.cursor()
			insert_user = "INSERT INTO users (user_name, password) VALUES (%s, %s)"
			data = (user_name, password)
			cursor.execute(insert_user, data)
			cnx.commit()
			cursor.close()
		except pymysql.Error as err:
			print "Failed to register user: {}".format(err)
			result = False
		finally:
			cnx.close()
			return result
		
	def get_user(self,user_name,password):
		try:
			cnx = pymysql.connect(**self.mysql_config)#este ** lo que hace es que convierte en tuplas de parametro= "valor", 
			cursor = cnx.cursor()
			select_stmt = "SELECT COUNT(*) FROM users WHERE user_name = %s and password = %s"
			data = (user_name, password)
			cursor.execute(select_stmt, data)
			result = cursor.fetchone()
			cnx.commit();
			cursor.close()
		except pymysql.Error as err:
			print "Failed to get user: {}".format(err)
			#print err.args[0]
		finally:
			cnx.close()
			return result[0]
