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
                   "Surname VARCHAR(30), Surname2 VARCHAR(30), Login VARCHAR(30), Password VARCHAR(30), Role BOOLEAN)")

        query.exec("CREATE TABLE IF NOT EXISTS statistics (ID integer primary key AUTOINCREMENT, "
                   "Time REAL, Count REAL, User_ID INTEGER)")

        return True

    def execute_query_with_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()
        return query

    def add_new_user_query(self, name, surname, surname2, login, password, role):
        sql_query = "INSERT INTO users (Name, Surname, Surname2, Login, Password, Role) VALUES (?, ?, ?, ?, ?, ?)"
        self.execute_query_with_params(sql_query, [name, surname, surname2, login, password, role])

    def update_user_query(self, name, surname, surname2, login, password, role, id):
        sql_query = "UPDATE users SET Name=?, Surname=?, Surname2=?, Login=?, Password=?, Role=?, WHERE ID=?"
        self.execute_query_with_params(sql_query, [name, surname, surname2, login, password, role, id])

    def delete_use_query(self, id):
        sql_query = "DELETE FROM users WHERE ID=?"
        self.execute_query_with_params(sql_query, [id])

    def output_user(self, column):
        sql_query = f"SELECT ({column}) FROM users"

        self.execute_query_with_params(sql_query)

        return '0'