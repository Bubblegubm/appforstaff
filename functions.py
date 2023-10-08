import sys
import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow
from connection import Data
import re

conn = Data()


def check_login(login):
    if login == conn.output_login_query(login):
        return False


def check_password(password, login):
    if check_login(login) == True: return True
    if password == conn.output_password_query(password, login):
        return False


def check_valid_name(name):
    pattern = r'^[a-zA-Zа-яА-ЯёЁ]+$'
    if re.match(pattern, name):
        return 1
    else:
        return 0


def check_valid_login(login):
    pattern = r'^[a-zA-Z][a-zA-Z0-9_-]{5,19}$'
    if re.match(pattern, login):
        return 1
    else:
        return 0


def check_valid_password(password):
    if len(password) < 6:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    return True


def check_secret_word(secret_word):
    pattern = r'^[a-zA-Zа-яА-ЯёЁ0-9]+$'
    if re.match(pattern, secret_word):
        return 1
    else:
        return 0


def check_valid_input_registration(surname, name, surname2, login, password, secret_word):
    if check_valid_name(surname):
        A = 0
    else:
        A = 1
    if check_valid_name(name):
        B = 0
    else:
        B = 1
    if check_valid_name(surname2):
        C = 0
    else:
        C = 1
    if check_valid_login(login):
        D = 0
    else:
        D = 1
    if check_valid_password(password):
        E = 0
    else:
        E = 1
    if check_secret_word(secret_word):
        F = 0
    else:
        F = 1

    if A == 0 and B == 0 and C == 0 and D == 0 and E == 0 and F == 0:
        conn.add_new_user_query(name, surname, surname2, login, password, secret_word, 1)

    return A, B, C, D, E, F
