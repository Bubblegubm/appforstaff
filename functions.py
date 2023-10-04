import sys
import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow
from connection import Data
import re


def check_login():
    return True

def check_password():
    if check_login() == False: return False
    return True

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
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    return True

def check_valid_input(surname, name, surname2, login, password):
    if check_valid_name(surname): A = 0
    else: A = 1
    if check_valid_name(name): B = 0
    else: B = 1
    if check_valid_name(surname2): C = 0
    else: C = 1
    if check_valid_login(login): D = 0
    else: D = 1
    if check_valid_password(password): E = 0
    else: E = 1

    return A, B, C, D, E