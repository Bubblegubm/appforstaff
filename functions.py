import sys
import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow
from connection import Data
import re
import random

conn = Data()


def check_login_password(login, password):
    return conn.output_login_password_query(login, password)


def output_ID(login, password):
    return conn.output_ID(login, password)


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


def dataUser(ID):
    return conn.dataUser(ID)


def recoverPassword1(name, surname, surname2, login, secret_word):
    return conn.recoverPassword1(name, surname, surname2, login, secret_word)


def recoverPassword2(password, id):
    return conn.update_user_query(password, id)


def output_test():
    return conn.output_test_query()


def output_speed_test():
    return conn.output_speed_test_query()


def add_statistic_test(time, score_test, score_speed_test, user_id):
    conn.add_statistic_test_query(time, score_test, score_speed_test, user_id)


def update_statistic_test(score_test, user_id):
    conn.update_statistic_test_query(score_test, user_id)


def update_statistic_speed_test(time, score_speed_test, user_id):
    conn.update_statistic_speed_test_query(time, score_speed_test, user_id)


def output_user_statistic(ID):
    return conn.output_user_statistic(ID)


def shuffle_answers(array):
    questions_with_shuffled_answers = []
    correctness_array = []

    for item in array:
        question, true_answer, false1, false2 = item

        answers = [true_answer, false1, false2]
        shuffled_answers = answers.copy()
        random.shuffle(shuffled_answers)

        correctness = [answer == true_answer for answer in shuffled_answers]

        questions_with_shuffled_answers.append([question] + shuffled_answers)
        correctness_array.append(correctness)

    return questions_with_shuffled_answers, correctness_array

def get_number_of_questions(array):
    return len(array)
