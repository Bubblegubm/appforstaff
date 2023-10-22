from PySide6 import QtWidgets, QtSql
from cryptography.fernet import Fernet



class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('app_db.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open database",
                                           "Click Cancel to exit.", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS users (ID integer primary key AUTOINCREMENT, Name VARCHAR(20), "
                   "Surname VARCHAR(30), Surname2 VARCHAR(30), Login VARCHAR(30), Password VARCHAR(1000),"
                   " Secret_word VARCHAR(30), Role BOOLEAN, Crypt_key VARCHAR(1000))")

        query.exec("CREATE TABLE IF NOT EXISTS statistics (ID integer primary key AUTOINCREMENT, "
                   "Time INTEGER, Score_test INTEGER, Score_speed_test INTEGER, User_ID INTEGER)")

        query.exec("CREATE TABLE IF NOT EXISTS theory (ID integer primary key AUTOINCREMENT, Question VARCHAR(200),"
                   "Answer VARCHAR(1000))")

        query.exec("CREATE TABLE IF NOT EXISTS test (ID integer primary key AUTOINCREMENT, Question VARCHAR(200),"
                   "True_answer VARCHAR(1000), False_answer VARCHAR(1000), Second_false_answer VARCHAR(1000))")

        query.exec("CREATE TABLE IF NOT EXISTS speed_test (ID integer primary key AUTOINCREMENT, Question VARCHAR(200),"
                   "True_answer VARCHAR(1000), False_answer VARCHAR(1000), Second_false_answer VARCHAR(1000))")

        return True

    def execute_query_with_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()
        return query

    def add_new_user_query(self, name, surname, surname2, login, password, secret_word, role):
        crypt_key = Fernet.generate_key().decode('utf-8')
        encrypted_password = self.Crypt_password(password, crypt_key)
        sql_query = "INSERT INTO users (Name, Surname, Surname2, Login, Password, Secret_word, Role, Crypt_key)" \
                    " VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        self.execute_query_with_params(sql_query,
                                       [name, surname, surname2, login, encrypted_password, secret_word, role,
                                        crypt_key])

    def update_user_query(self, password, id):
        crypt_key = self.get_crypt_key(id)
        encrypted_password = self.Crypt_password(password, crypt_key)
        sql_query = "UPDATE users SET Password=? WHERE ID=?"
        self.execute_query_with_params(sql_query, [encrypted_password, id])

    def delete_user_query(self, id):
        sql_query = "DELETE FROM users WHERE ID=?"
        self.execute_query_with_params(sql_query, [id])

    def output_login_password_query(self, login, password):
        sql_query = QtSql.QSqlQuery()
        sql_query.exec("SELECT Login, Password, Crypt_key FROM users")
        sql_login, sql_password, sql_crypt_key = range(3)

        while sql_query.next():
            decrypted_password = self.Decrypt_password(sql_query.value(sql_password), sql_query.value(sql_crypt_key))
            if sql_query.value(sql_login) == login and decrypted_password == password:
                return True, True
            elif sql_query.value(sql_login) == login and decrypted_password != password:
                return True, False

        return False, False

    def output_ID(self, login, password):
        sql_query = QtSql.QSqlQuery()
        sql_query.exec("SELECT ID, Login, Password, Crypt_key FROM users")
        sql_id, sql_login, sql_password, sql_crypt_key = range(4)

        while sql_query.next():
            decrypted_password = self.Decrypt_password(sql_query.value(sql_password), sql_query.value(sql_crypt_key))
            if sql_query.value(sql_login) == login and decrypted_password == password:
                return sql_query.value(sql_id)

    def dataUser(self, ID):
        sql_query = QtSql.QSqlQuery()
        sql_query.exec("SELECT ID, Name, Surname, Surname2, Login, Password, Secret_word, Role, Crypt_key FROM users")
        sql_id, sql_name, sql_surname, sql_surname2, sql_login, sql_password, sql_secret_word, sql_role, sql_crypt_key = range(
            9)
        while sql_query.next():
            if ID == sql_query.value(sql_id):
                decrypted_password = self.Decrypt_password(sql_query.value(sql_password),
                                                           sql_query.value(sql_crypt_key))
                return {'ID': sql_query.value(sql_id), 'Name': sql_query.value(sql_name),
                        'Surname': sql_query.value(sql_surname), 'Surname2': sql_query.value(sql_surname2),
                        'Login': sql_query.value(sql_login), 'Password': decrypted_password,
                        'SecretWord': sql_query.value(sql_secret_word), 'Role': sql_query.value(sql_role)}

    def recoverPassword1(self, name, surname, surname2, login, secret_word):
        sql_query = QtSql.QSqlQuery()
        sql_query.exec("SELECT ID, Name, Surname, Surname2, Login, Secret_word, Password, Crypt_key FROM users")
        sql_id, sql_name, sql_surname, sql_surname2, sql_login, sql_secret_word, sql_password, sql_crypt_key = range(8)
        while sql_query.next():
            decrypted_password = self.Decrypt_password(sql_query.value(sql_password), sql_query.value(sql_crypt_key))
            if (sql_query.value(sql_name) == name) and (sql_query.value(sql_surname) == surname) \
                    and (sql_query.value(sql_surname2) == surname2) and (sql_query.value(sql_login) == login) \
                    and (sql_query.value(sql_secret_word) == secret_word):
                return sql_query.value(sql_id)
        return -1

    def add_statistic_test_query(self, time, score_test, score_speed_test, user_id):
        sql_query = "INSERT INTO statistics (Time, Score_test, Score_speed_test, User_ID) VALUES (?, ?, ?, ?)"
        self.execute_query_with_params(sql_query, [time, score_test, score_speed_test, user_id])

    def update_statistic_test_query(self, score_test, user_id):
        sql_query = "UPDATE statistics SET Score_test=? WHERE User_ID=?"
        self.execute_query_with_params(sql_query, [score_test, user_id])

    def update_statistic_speed_test_query(self, time, score_speed_test, user_id):
        sql_query = "UPDATE statistics SET Time=?, Score_speed_test=? WHERE User_ID=?"
        self.execute_query_with_params(sql_query, [time, score_speed_test, user_id])

    def output_test_query(self):
        sql_query = QtSql.QSqlQuery()
        sql_query.exec("SELECT Question, True_answer, False_answer, Second_false_answer FROM test")
        sql_quest, sql_true, sql_false1, sql_false2 = range(4)
        array = []
        while sql_query.next():
            array.append([sql_query.value(sql_quest), sql_query.value(sql_true), sql_query.value(sql_false1),
                          sql_query.value(sql_false2)])
        return array

    def output_speed_test_query(self):
        sql_query = QtSql.QSqlQuery()
        sql_query.exec("SELECT Question, True_answer, False_answer, Second_false_answer FROM speed_test")
        sql_quest, sql_true, sql_false1, sql_false2 = range(4)
        array = []
        while sql_query.next():
            array.append([sql_query.value(sql_quest), sql_query.value(sql_true), sql_query.value(sql_false1),
                          sql_query.value(sql_false2)])
        return array

    def output_user_statistic(self, ID):
        sql_query = QtSql.QSqlQuery()
        sql_query.exec("SELECT Time, Score_test, Score_speed_test, User_ID FROM statistics")
        sql_time, sql_score_test, sql_score_speed_test, sql_id = range(4)
        while sql_query.next():
            if sql_query.value(sql_id) == ID:
                return [sql_query.value(sql_time), sql_query.value(sql_score_test),
                        sql_query.value(sql_score_speed_test)]

    def output_theory_query(self):
        sql_query = QtSql.QSqlQuery()
        sql_query.exec("SELECT Question, Answer FROM theory")
        sql_quest, sql_answer = range(2)
        array = []
        while sql_query.next():
            array.append([sql_query.value(sql_quest), sql_query.value(sql_answer)])
        return array

    def get_crypt_key(self, user_id):
        sql_query = QtSql.QSqlQuery()
        sql_query.prepare("SELECT Crypt_key FROM users WHERE ID=?")
        sql_query.addBindValue(user_id)
        sql_query.exec()

        if sql_query.next():
            key = sql_query.value(0)
            return key
        else:
            return None

    def Crypt_password(self, password, crypt_key):
        cipher = Fernet(crypt_key.encode('utf-8'))
        crypt_password = cipher.encrypt(password.encode('utf-8'))
        return crypt_password.decode('utf-8')

    def Decrypt_password(self, password, crypt_key):

        cipher = Fernet(crypt_key.encode('utf-8'))
        decrypt_password = cipher.decrypt(password.encode('utf-8'))
        return decrypt_password.decode('utf-8')

    def is_login_exist(self, login):
        sql_query = QtSql.QSqlQuery()
        sql_query.prepare("SELECT Login FROM users WHERE Login=?")
        sql_query.addBindValue(login)
        sql_query.exec()

        if sql_query.next():
            return True
        else:
            return False