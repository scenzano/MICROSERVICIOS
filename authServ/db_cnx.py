import pymysql

class DbService():

	mysql_config = {
		"user": "root",
		"passwd": "lab4",
		"host": "localhost",
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
	
	def insert_user(self,user_name,password):
		try:
			answer = False
			cnx = pymysql.connect(**self.mysql_config)#este ** lo que hace es que convierte en tuplas de parametro= "valor", 
			cursor = cnx.cursor()
			insert_user = "INSERT INTO users (user_name, password) VALUES (%s, %s)"
			#select_stmt = "SELECT * FROM " + table_name + " WHERE emp_no = %(emp_no)s"
			data = (user_name, password)	
			if(cursor.execute(insert_user, data)):
				answer = True
			cnx.commit()
			cursor.close()
		except pymysql.Error as err:
			print "Failed to register user: {}".format(err)
		finally:
			cnx.close()
			return answer
		
	def get_user(self,user_name,password):
		try:
			answer = False
			cnx = pymysql.connect(**self.mysql_config)#este ** lo que hace es que convierte en tuplas de parametro= "valor", 
			cursor = cnx.cursor()
			select_stmt = "SELECT COUNT(*) FROM users WHERE user_name = %s and password = %s"
			data = (user_name, password)
			cursor.execute(select_stmt, data)
			result = cursor.fetchone()
			cnx.commit();
			if(result[0]):
				print result[0]
				answer = True;
			cursor.close()
		except pymysql.Error as err:
			print "Failed to get user: {}".format(err)
		finally:
			cnx.close()
			return answer

	"""
	select_stmt = "SELECT * FROM employees WHERE emp_no = %(emp_no)s"
	cursor.execute(select_stmt, { 'emp_no': 2 })
	"""
"""
d = DbService();
print d.get_user("seba","123");
print d.get_user("jjjj","7777");
"""