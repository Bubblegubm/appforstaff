from PySide6 import QtWidgets, QtSql


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
                   "Surname VARCHAR(30), Surname2 VARCHAR(30), Login VARCHAR(30), Password VARCHAR(30),"
                   " Secret_word VARCHAR(30), Role BOOLEAN)")

        query.exec("CREATE TABLE IF NOT EXISTS statistics (ID integer primary key AUTOINCREMENT, "
                   "Time REAL, Count REAL, User_ID INTEGER)")

        query.exec("CREATE TABLE IF NOT EXISTS theory (ID integer primary key AUTOINCREMENT, Question VARCHAR(200),"
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

    def add_new_user_query(self, name, surname, surname2, login, password,
                           secret_word, role):
        sql_query = "INSERT INTO users (Name, Surname, Surname2, Login, Password, Secret_word, Role)" \
                    " VALUES (?, ?, ?, ?, ?, ?, ?)"
        print(True)
        self.execute_query_with_params(sql_query, [name, surname, surname2, login, password, secret_word, role])

    def update_user_query(self, name, surname, surname2, login, password, secret_word, role, id):
        sql_query = "UPDATE users SET Name=?, Surname=?, Surname2=?, Login=?, Password=?, Secret_word=?," \
                    " Role=?, WHERE ID=?"
        self.execute_query_with_params(sql_query, [name, surname, surname2, login, password, secret_word, role, id])

    def delete_user_query(self, id):
        sql_query = "DELETE FROM users WHERE ID=?"
        self.execute_query_with_params(sql_query, [id])

    def output_login_password_query(self, login, password):
        sql_query = QtSql.QSqlQuery()
        sql_query.exec("SELECT Login, Password FROM users")
        sql_login, sql_password = range(2)

        while sql_query.next():
            if sql_query.value(sql_login) == login and sql_query.value(sql_password) == password:
                return True, True
            elif sql_query.value(sql_login) == login and sql_query.value(sql_password) != password:
                return True, False

        return False, False

    def output_ID(self, login, password):
        sql_query = QtSql.QSqlQuery()
        sql_query.exec("SELECT ID, Login, Password FROM users")
        sql_id, sql_login, sql_password = range(3)

        while sql_query.next():
            if sql_query.value(sql_login) == login and sql_query.value(sql_password) == password:
                return sql_query.value(sql_id)

    def dataUser(self, ID):
        return 1

    #def output_user(self, name=None, surname=None, surname2=None, login=None, password=None,
    #                secret_word=None, role=None, id=None):
    #    sql_query = QtSql.QSqlQuery()
    #    sql_query.exec("SELECT ID, Name, Surname, Surname2, Login, Password, Secret_word, Role FROM users")
    #    sql_id, sql_name, sql_surname, sql_surname2, sql_login, sql_password, sql_secret_word, sql_role = range(8)
    #
    #    while sql_query.next():
    #        print(sql_query.value(sql_login))
    #        if sql_query.value(sql_login) == login and sql_query.value(sql_password) == password:
    #            return login, password
    #        elif sql_query.value(sql_login) == login and sql_query.value(sql_password) != password:
    #            return login, False
    #        elif sql_query.value(sql_login) != login and sql_query.value(sql_password) == password:
    #            return False, password
