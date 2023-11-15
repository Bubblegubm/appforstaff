import functools

import PySide6
from PySide6.QtCore import Qt, QTimer, QSize
from PySide6.QtGui import Qt, QFontDatabase, QStandardItemModel
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtWidgets, QtCore
import time

from authorization import Ui_Authorization
from registration import Ui_Registration
from main_window import Ui_MainWindow
from theory import Ui_Theory
from test import Ui_Test
from recover_password_1 import Ui_RecoverPassword1
from recover_password_2 import Ui_RecoverPassword2
from change_password import Ui_ChangePassword
from profile import Ui_Profile
from speed_test import Ui_SpeedTest
from main_window_admin import Ui_MainWindowAdmin
from statistics_users import Ui_StatisticsUsers

from functions import check_valid_input_registration, check_valid_password, check_login_password, output_ID, dataUser, \
    recoverPassword1, recoverPassword2, output_test, output_speed_test, add_statistic_test, \
    output_user_statistic, shuffle_answers, get_number_of_questions, update_statistic_test, \
    update_statistic_speed_test, output_theory, get_data_statistics_users

StyleSheetForButtonAvailable = u"QPushButton{color: rgba(255, 255, 255, 255); border: 3px solid rgb(255, 255, 255);" \
                               "border-radius: 7px; font: 26pt \"Ambient(RUS BY LYAJKA)\"; background-color: rgba(0, 0, 0, 100); width: 50px;}" \
                               "QPushButton::hover{background-color: rgba(0, 0, 0, 150);}" \
                               "QPushButton::pressed{background-color: rgba(0, 0, 0, 200);}"

StyleSheetForButtonAvailableForVariantAnswer = u"QPushButton{color: rgb(255, 255, 255); border: 3px solid rgb(255, 255, 255);" \
                                               "border-radius: 7px; font: 26pt \"Ambient(RUS BY LYAJKA)\";" \
                                               "background-color: rgba(0, 0, 0, 100); width: 50px; text-align:" \
                                               "top, left; padding-left: 10px; padding-top: 5px;}" \
                                               "QPushButton::hover{background-color: rgba(0, 0, 0, 150);}" \
                                               "QPushButton::pressed{background-color: rgba(0, 0, 0, 200);}"

StyleSheetForButtonUnavailable = u"color: rgba(255, 255, 255, 100); border: 3px solid rgb(255, 255, 255);" \
                                 "border-radius: 7px; font: 26pt \"Ambient(RUS BY LYAJKA)\"; background-color: rgba(0, 0, 0, 100); width: 50px;"

StyleSheetForButtonSelected = u"color: rgba(255, 255, 255, 255); border: 3px solid rgb(255, 255, 255);" \
                              "border-radius: 7px; font: 26pt \"Ambient(RUS BY LYAJKA)\";" \
                              "background-color: rgba(17, 207, 0, 255); width: 50px; text-align:" \
                              "top, left; padding-left: 10px; padding-top: 5px;"

StyleSheetForLabel = "color: rgb(255, 255, 255); border: 3px solid rgb(255, 255, 255); border-radius: 7px;" \
                     "font: 30pt \"Ambient(RUS BY LYAJKA)\"; background-color: rgba(0, 0, 0, 100);"


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_Authorization()
        self.ui.setupUi(self)
        self.data_User = {'ID': 0, 'Name': "", 'Surname': "", 'Surname2': "", 'Login': "", 'Password': "",
                          'SecretWord': "",
                          'Role': ""}
        # self.dataUser = {"ID": 0, "Name": "", "Surname": "", "Surname2": "", "Login": "", "Password": "", "SecretWord": "", "Role": ""}
        QFontDatabase.addApplicationFont("Fonts\\ljk_Ambient-Medium.ttf")
        self.setCentralWidget(Window_Authorization(self.data_User, self.centralWidget()))


class Window_Authorization(QMainWindow):
    def __init__(self, data_User: dict, parent):
        super(Window_Authorization, self).__init__(parent)

        self.ui = Ui_Authorization()
        self.ui.setupUi(self)
        self.data_User = data_User

        # self.dataUser = {"ID": 0, "Name": "", "Surname": "", "Surname2": "", "Login": "", "Password": "", "SecretWord": "", "Role": ""}

        self.ui.IconFailLogin.setVisible(False)
        self.ui.IconFailPassword.setVisible(False)

        self.ui.ButtonRegistration.clicked.connect(self.pressed_button_registration)
        self.ui.ButtonAuthorization.clicked.connect(self.pressed_button_authorization)
        self.ui.ButtonProblemsWithAuthorization.clicked.connect(self.pressed_button_problems_with_authorization)

    def pressed_button_registration(self):
        self.setCentralWidget(Window_Registration(self.centralWidget(), self.data_User))

    def pressed_button_authorization(self):
        login = self.ui.Login.text()
        password = self.ui.Password.text()

        a, b = check_login_password(login, password)

        # print(output_ID(login, password))

        if a == 0:
            self.ui.IconFailLogin.setVisible(True)
        else:
            self.ui.IconFailLogin.setVisible(False)
        if b == 0:
            self.ui.IconFailPassword.setVisible(True)
        else:
            self.ui.IconFailPassword.setVisible(False)

        if a == 1 and b == 1:
            ID = output_ID(login, password)
            self.data_User = dataUser(ID)
            print(self.data_User)
            self.setCentralWidget(Window_MainWindow(self.centralWidget(), self.data_User))

    def pressed_button_problems_with_authorization(self):
        self.setCentralWidget(Window_RecoverPassword1(self.centralWidget(), self.data_User))


class Window_Registration(QMainWindow):
    def __init__(self, parent, data_User: dict):
        super(Window_Registration, self).__init__(parent)
        self.ui = Ui_Registration()
        self.ui.setupUi(self)
        self.data_User = data_User

        self.ui.IconFailSurname.setVisible(False)
        self.ui.IconFailName.setVisible(False)
        self.ui.IconFailSurname2.setVisible(False)
        self.ui.IconFailLoginNone.setVisible(False)
        self.ui.IconFailLoginBusy.setVisible(False)
        self.ui.IconFailPassword.setVisible(False)
        self.ui.IconFailPasswordText.setVisible(False)
        self.ui.IconFailPasswordText.setStyleSheet(StyleSheetForLabel)
        self.ui.IconFailSecretWord.setVisible(False)

        self.ui.ButtonBack.clicked.connect(self.pressed_button_back)
        self.ui.ButtonRegistration.clicked.connect(self.pressed_button_registration)

    def pressed_button_back(self):
        self.setCentralWidget(Window_Authorization(self.data_User, self.centralWidget()))

    def pressed_button_registration(self):
        name = self.ui.Name.text()
        surname = self.ui.Surname.text()
        surname2 = self.ui.Surname2.text()
        login = self.ui.Login.text()
        password = self.ui.Password.text()
        secret_word = self.ui.SecretWord.text()

        a, b, c, d, e, f = check_valid_input_registration(surname, name, surname2, login, password, secret_word)

        # print(a, b, c, d, e, f)

        if a == 1:
            self.ui.IconFailSurname.setVisible(True)
        else:
            self.ui.IconFailSurname.setVisible(False)

        if b == 1:
            self.ui.IconFailName.setVisible(True)
        else:
            self.ui.IconFailName.setVisible(False)

        if c == 1:
            self.ui.IconFailSurname2.setVisible(True)
        else:
            self.ui.IconFailSurname2.setVisible(False)

        if d == 1:
            self.ui.IconFailLoginNone.setVisible(True)
        elif d == 2:
            self.ui.IconFailLoginBusy.setVisible(True)
        else:
            self.ui.IconFailLoginNone.setVisible(False)
            self.ui.IconFailLoginBusy.setVisible(False)

        if e == 1:
            self.ui.IconFailPassword.setVisible(True)
            self.ui.IconFailPasswordText.setVisible(True)
        else:
            self.ui.IconFailPassword.setVisible(False)
            self.ui.IconFailPasswordText.setVisible(False)

        if f == 1:
            self.ui.IconFailSecretWord.setVisible(True)
        else:
            self.ui.IconFailSecretWord.setVisible(False)

        if not (a or b or c or d or e or f):
            self.data_User = dataUser(output_ID(login, password))
            add_statistic_test(0, 0, 0, self.data_User.get('ID'))
            self.setCentralWidget(Window_MainWindow(self.centralWidget(), self.data_User))


class Window_MainWindow(QMainWindow):
    def __init__(self, parent, data_User: dict):
        super(Window_MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.data_User = data_User

        self.countAcceptTest = False
        self.countAcceptSpeedTest = False

        self.design_window()

        self.ui.ButtonTheory.clicked.connect(self.pressed_button_theory)
        self.ui.ButtonTest.clicked.connect(self.pressed_button_test)
        self.ui.ButtonSpeedTest.clicked.connect(self.pressed_button_speed_test)
        self.ui.ButtonProfile.clicked.connect(self.pressed_button_profile)
        self.ui.ButtonAdminFunctions.clicked.connect(self.pressed_button_admin_functions)
        self.ui.ButtonCancel.clicked.connect(self.pressed_button_cancel)
        self.ui.ButtonBegin.clicked.connect(self.pressed_button_begin)

    def pressed_button_theory(self):
        if not (self.countAcceptTest or self.countAcceptSpeedTest):
            self.setCentralWidget(Window_Theory(self.centralWidget(), self.data_User))

    def pressed_button_test(self):
        if not (self.countAcceptTest or self.countAcceptSpeedTest):
            self.countAcceptTest = True
            self.design_window()

    def pressed_button_speed_test(self):
        if not (self.countAcceptTest or self.countAcceptSpeedTest):
            self.countAcceptSpeedTest = True
            self.design_window()

    def pressed_button_profile(self):
        if not (self.countAcceptTest or self.countAcceptSpeedTest):
            self.setCentralWidget(Window_Profile(self.centralWidget(), self.data_User))

    def pressed_button_admin_functions(self):
        if not (self.countAcceptTest or self.countAcceptSpeedTest):
            self.setCentralWidget(Window_MainWindowAdmin(self.centralWidget(), self.data_User))

    def pressed_button_cancel(self):
        self.countAcceptTest = False
        self.countAcceptSpeedTest = False
        self.design_window()

    def pressed_button_begin(self):
        if self.countAcceptTest:
            self.setCentralWidget(Window_Test(self.centralWidget(), self.data_User))
        if self.countAcceptSpeedTest:
            self.setCentralWidget(Window_SpeedTest(self.centralWidget(), self.data_User))

    def design_window(self):
        if self.data_User['Role'] != 1:
            self.ui.ButtonAdminFunctions.setVisible(False)

        if self.countAcceptTest:
            self.ui.ButtonTheory.setVisible(False)
            self.ui.ButtonTest.setVisible(False)
            self.ui.ButtonSpeedTest.setVisible(False)
            self.ui.ButtonProfile.setStyleSheet(StyleSheetForButtonUnavailable)
            self.ui.ButtonAdminFunctions.setStyleSheet(StyleSheetForButtonUnavailable)

            self.ui.AcceptTest.setText("Вы готовы приступить\nк тесту?\nВыйти из него будет нельзя!")

            self.ui.AcceptTest.setVisible(True)
            self.ui.ButtonCancel.setVisible(True)
            self.ui.ButtonBegin.setVisible(True)

        elif self.countAcceptSpeedTest:
            self.ui.ButtonTheory.setVisible(False)
            self.ui.ButtonTest.setVisible(False)
            self.ui.ButtonSpeedTest.setVisible(False)
            self.ui.ButtonProfile.setStyleSheet(StyleSheetForButtonUnavailable)
            self.ui.ButtonAdminFunctions.setStyleSheet(StyleSheetForButtonUnavailable)

            self.ui.AcceptTest.setText("Вы готовы приступить\nк скоростному тесту?\nВыйти из него будет нельзя!")

            self.ui.AcceptTest.setVisible(True)
            self.ui.ButtonCancel.setVisible(True)
            self.ui.ButtonBegin.setVisible(True)

        else:
            self.ui.ButtonTheory.setVisible(True)
            self.ui.ButtonTest.setVisible(True)
            self.ui.ButtonSpeedTest.setVisible(True)
            self.ui.ButtonProfile.setStyleSheet(StyleSheetForButtonAvailable)
            self.ui.ButtonAdminFunctions.setStyleSheet(StyleSheetForButtonAvailable)

            self.ui.AcceptTest.setVisible(False)
            self.ui.ButtonCancel.setVisible(False)
            self.ui.ButtonBegin.setVisible(False)


class Window_Theory(QMainWindow):
    def __init__(self, parent, data_User: dict):
        super(Window_Theory, self).__init__(parent)
        self.ui = Ui_Theory()
        self.ui.setupUi(self)
        self.data_User = data_User

        self.current_page = 0
        self.dataTheory = output_theory()
        self.count_page = len(self.dataTheory)

        self.design_button_back()
        self.design_button_forward()
        self.design_progress_bar()
        self.design_question()
        self.design_answer()

        self.ui.ButtonBack.clicked.connect(self.pressed_button_back)
        self.ui.ButtonForward.clicked.connect(self.pressed_button_forward)
        self.ui.ButtonExit.clicked.connect(self.pressed_button_exit)

    def pressed_button_forward(self):
        if self.current_page == self.count_page - 1:
            self.setCentralWidget(Window_MainWindow(self.centralWidget(), self.data_User))

        if self.current_page < self.count_page - 1:
            self.current_page += 1
            self.design_button_back()
            self.design_button_forward()
            self.design_progress_bar()
            self.design_question()
            self.design_answer()

    def pressed_button_back(self):
        if self.current_page > 0: self.current_page -= 1
        self.design_button_back()
        self.design_button_forward()
        self.design_progress_bar()
        self.design_question()
        self.design_answer()

    def pressed_button_exit(self):
        self.setCentralWidget(Window_MainWindow(self.centralWidget(), self.data_User))

    def design_button_back(self):
        if self.current_page == 0:
            self.ui.ButtonBack.setStyleSheet(StyleSheetForButtonUnavailable)
        else:
            self.ui.ButtonBack.setStyleSheet(StyleSheetForButtonAvailable)

    def design_button_forward(self):
        if self.current_page >= self.count_page - 1:
            self.ui.ButtonForward.setText('Завершить')
        else:
            self.ui.ButtonForward.setText('Далее')

    def design_progress_bar(self):
        self.ui.ProgressBar.setValue(100 * round(self.current_page / self.count_page, 2))

    def design_question(self):
        self.ui.Question.setTextInteractionFlags(Qt.TextInteractionFlag(False))
        self.ui.Question.setText(self.dataTheory[self.current_page][0])

    def design_answer(self):
        self.ui.Answer.setTextInteractionFlags(Qt.TextInteractionFlag(False))
        self.ui.Answer.setText(self.dataTheory[self.current_page][1])


class Window_Test(QMainWindow):
    def __init__(self, parent, data_User: dict):
        super(Window_Test, self).__init__(parent)
        self.ui = Ui_Test()
        self.ui.setupUi(self)
        self.data_User = data_User

        self.current_page = 0
        self.dataTest, self.trueAnswers = shuffle_answers(output_test())
        self.count_page = len(self.dataTest)
        self.count_true_answers = 0

        self.array_answers = [[False for j in range(3)] for i in range(self.count_page)]

        self.select_answer1 = False
        self.select_answer2 = False
        self.select_answer3 = False

        self.design_button_back()
        self.design_button_forward()
        self.design_progress_bar()
        self.design_question()
        self.design_button_answer1()
        self.design_button_answer2()
        self.design_button_answer3()

        self.ui.ButtonBack.clicked.connect(self.pressed_button_back)
        self.ui.ButtonForward.clicked.connect(self.pressed_button_forward)
        self.ui.ButtonAnswer1.clicked.connect(self.pressed_button_answer1)
        self.ui.ButtonAnswer2.clicked.connect(self.pressed_button_answer2)
        self.ui.ButtonAnswer3.clicked.connect(self.pressed_button_answer3)

    def pressed_button_forward(self):
        if self.current_page == self.count_page - 1:
            for i in range(0, self.count_page):
                if functools.reduce(lambda x, y: x and y, map(lambda p, q: p == q, self.array_answers[i],
                                                              self.trueAnswers[i]), True):
                    self.count_true_answers += 1
            update_statistic_test(self.count_true_answers, self.data_User.get('ID'))
            self.setCentralWidget(Window_MainWindow(self.centralWidget(), self.data_User))

        if self.current_page != self.count_page - 1:
            if self.current_page < self.count_page: self.array_answers[self.current_page] = [self.select_answer1,
                                                                                             self.select_answer2,
                                                                                             self.select_answer3]

            if (self.current_page < self.count_page) and (
                    self.select_answer1 or self.select_answer2 or self.select_answer3): self.current_page += 1

            if self.current_page < self.count_page:
                self.select_answer1 = self.array_answers[self.current_page][0]
                self.select_answer2 = self.array_answers[self.current_page][1]
                self.select_answer3 = self.array_answers[self.current_page][2]

            self.design_question()
            self.design_button_answer1()
            self.design_button_answer2()
            self.design_button_answer3()

            self.design_button_back()
            self.design_button_forward()
            self.design_progress_bar()

    def pressed_button_back(self):
        if self.current_page < self.count_page: self.array_answers[self.current_page] = [self.select_answer1,
                                                                                         self.select_answer2,
                                                                                         self.select_answer3]
        if self.current_page > 0: self.current_page -= 1

        self.select_answer1 = self.array_answers[self.current_page][0]
        self.select_answer2 = self.array_answers[self.current_page][1]
        self.select_answer3 = self.array_answers[self.current_page][2]

        self.design_question()
        self.design_button_answer1()
        self.design_button_answer2()
        self.design_button_answer3()
        self.design_button_back()
        self.design_button_forward()
        self.design_progress_bar()

    def pressed_button_answer1(self):
        self.select_answer1 = True
        self.select_answer2 = False
        self.select_answer3 = False

        self.design_button_answer1()
        self.design_button_answer2()
        self.design_button_answer3()
        self.design_button_forward()

    def pressed_button_answer2(self):
        self.select_answer1 = False
        self.select_answer2 = True
        self.select_answer3 = False

        self.design_button_answer1()
        self.design_button_answer2()
        self.design_button_answer3()
        self.design_button_forward()

    def pressed_button_answer3(self):
        self.select_answer1 = False
        self.select_answer2 = False
        self.select_answer3 = True

        self.design_button_answer1()
        self.design_button_answer2()
        self.design_button_answer3()
        self.design_button_forward()

    def design_button_back(self):
        if self.current_page == 0:
            self.ui.ButtonBack.setStyleSheet(StyleSheetForButtonUnavailable)
        else:
            self.ui.ButtonBack.setStyleSheet(StyleSheetForButtonAvailable)

    def design_button_forward(self):  # need edit!
        if self.current_page >= self.count_page - 1:
            self.ui.ButtonForward.setText('Завершить')
        else:
            self.ui.ButtonForward.setText('Далее')

        if (self.select_answer1 or self.select_answer2 or self.select_answer3) == False:
            self.ui.ButtonForward.setStyleSheet(StyleSheetForButtonUnavailable)
        else:
            self.ui.ButtonForward.setStyleSheet(StyleSheetForButtonAvailable)

    def design_progress_bar(self):
        self.ui.ProgressBar.setValue(100 * round(self.current_page / self.count_page, 2))

    def design_question(self):
        self.ui.Question.setTextInteractionFlags(Qt.TextInteractionFlag(False))
        self.ui.Question.setText(self.dataTest[self.current_page][0])

    def design_button_answer1(self):
        if (self.select_answer1):
            self.ui.ButtonAnswer1.setStyleSheet(StyleSheetForButtonSelected)
            self.ui.ButtonAnswer1.setText(self.dataTest[self.current_page][1])
        else:
            self.ui.ButtonAnswer1.setStyleSheet(StyleSheetForButtonAvailableForVariantAnswer)
            self.ui.ButtonAnswer1.setText(self.dataTest[self.current_page][1])

    def design_button_answer2(self):
        if (self.select_answer2):
            self.ui.ButtonAnswer2.setStyleSheet(StyleSheetForButtonSelected)
            self.ui.ButtonAnswer2.setText(self.dataTest[self.current_page][2])
        else:
            self.ui.ButtonAnswer2.setStyleSheet(StyleSheetForButtonAvailableForVariantAnswer)
            self.ui.ButtonAnswer2.setText(self.dataTest[self.current_page][2])

    def design_button_answer3(self):
        if (self.select_answer3):
            self.ui.ButtonAnswer3.setStyleSheet(StyleSheetForButtonSelected)
            self.ui.ButtonAnswer3.setText(self.dataTest[self.current_page][3])
        else:
            self.ui.ButtonAnswer3.setStyleSheet(StyleSheetForButtonAvailableForVariantAnswer)
            self.ui.ButtonAnswer3.setText(self.dataTest[self.current_page][3])


class Window_RecoverPassword1(QMainWindow):
    def __init__(self, parent, data_User: dict):
        super(Window_RecoverPassword1, self).__init__(parent)
        self.ui = Ui_RecoverPassword1()
        self.ui.setupUi(self)
        self.data_User = data_User

        self.ui.Error.setVisible(False)

        self.ui.ButtonBack.clicked.connect(self.pressed_button_back)
        self.ui.ButtonFurther.clicked.connect(self.pressed_button_further)

    def pressed_button_back(self):
        self.setCentralWidget(Window_Authorization(self.data_User, self.centralWidget()))

    def pressed_button_further(self):
        name = self.ui.Name.text()
        surname = self.ui.Surname.text()
        surname2 = self.ui.Surname2.text()
        login = self.ui.Login.text()
        secret_word = self.ui.SecretWord.text()
        id = recoverPassword1(name, surname, surname2, login, secret_word)
        if id == -1:
            self.ui.Error.setVisible(True)
        else:
            self.setCentralWidget(Window_RecoverPassword2(self.centralWidget(), self.data_User, id))


class Window_RecoverPassword2(QMainWindow):
    def __init__(self, parent, data_User: dict, id=None):
        super(Window_RecoverPassword2, self).__init__(parent)
        self.ui = Ui_RecoverPassword2()
        self.ui.setupUi(self)
        self.data_User = data_User
        if id != None:
            self.id = id

        self.ui.IconFailPassword.setVisible(False)

        self.ui.ButtonBack.clicked.connect(self.pressed_button_back)
        self.ui.ButtonRecoverPassword.clicked.connect(self.pressed_button_recover_password)

    def pressed_button_back(self):
        self.setCentralWidget(Window_RecoverPassword1(self.centralWidget(), self.data_User))

    def pressed_button_recover_password(self):
        password = self.ui.NewPassword.text()
        if check_valid_password(password):
            recoverPassword2(password, self.id)
            self.data_User = dataUser(self.id)
            self.setCentralWidget(Window_MainWindow(self.centralWidget(), self.data_User))
        else:
            self.ui.IconFailPassword.setVisible(True)


class Window_Profile(QMainWindow):
    def __init__(self, parent, data_User: dict):
        super(Window_Profile, self).__init__(parent)
        self.ui = Ui_Profile()
        self.ui.setupUi(self)
        self.data_User = data_User
        self.statistic_user = output_user_statistic(self.data_User.get('ID'))

        self.ui.NameSurnameUser.setTextInteractionFlags(Qt.TextInteractionFlag(False))
        self.ui.ResultsTest.setTextInteractionFlags(Qt.TextInteractionFlag(False))
        self.ui.ResultsSpeedTest.setTextInteractionFlags(Qt.TextInteractionFlag(False))

        self.ui.NameSurnameUser.setText(
            f"{self.data_User.get('Surname')}\n{self.data_User.get('Name')}\n{self.data_User.get('Surname2')}")
        self.ui.ResultsTest.setText(
            f"Результаты теста:\n{self.statistic_user[1]} из {get_number_of_questions(output_test())} правильных\nответов")
        self.ui.ResultsSpeedTest.setText(
            f"Результаты скоростного\nтеста:\n{self.statistic_user[2]} из {get_number_of_questions(output_speed_test())} правильных\nответов\n"
            f"Пройден за {self.statistic_user[0] // 60} мин. {self.statistic_user[0] % 60} с.")
        # print(f"sadasdasdasd {self.data_User['Name']}\n{self.data_User['Surname']}\n{self.data_User['Surname2']}")

        self.ui.ButtonBack.clicked.connect(self.pressed_button_back)
        self.ui.ButtonChangePassword.clicked.connect(self.pressed_button_change_password)

    def pressed_button_back(self):
        self.setCentralWidget(Window_MainWindow(self.centralWidget(), self.data_User))

    def pressed_button_change_password(self):
        self.setCentralWidget(Window_ChangePassword(self.centralWidget(), self.data_User))


class Window_ChangePassword(QMainWindow):
    def __init__(self, parent, data_User: dict):
        super(Window_ChangePassword, self).__init__(parent)
        self.ui = Ui_ChangePassword()
        self.ui.setupUi(self)
        self.data_User = data_User

        self.ui.IconFailPassword.setVisible(False)

        self.ui.ButtonBack.clicked.connect(self.pressed_button_back)
        self.ui.ButtonChangePassword.clicked.connect(self.pressed_button_change_password)

    def pressed_button_back(self):
        self.setCentralWidget(Window_Profile(self.centralWidget(), self.data_User))

    def pressed_button_change_password(self):
        password = self.ui.NewPassword.text()
        if check_valid_password(password):
            recoverPassword2(password, self.data_User['ID'])
            self.data_User = dataUser(self.data_User['ID'])
            self.setCentralWidget(Window_Profile(self.centralWidget(), self.data_User))
        else:
            self.ui.IconFailPassword.setVisible(True)


class Window_SpeedTest(QMainWindow):
    def __init__(self, parent, data_User: dict):
        super(Window_SpeedTest, self).__init__(parent)
        self.ui = Ui_SpeedTest()
        self.ui.setupUi(self)
        self.data_User = data_User
        self.time = 0

        self.current_page = 0
        self.dataTest, self.trueAnswers = shuffle_answers(output_speed_test())
        self.count_page = len(self.dataTest)
        self.count_true_answers = 0

        self.array_answers = [[False for j in range(3)] for i in range(self.count_page)]

        self.select_answer1 = False
        self.select_answer2 = False
        self.select_answer3 = False

        self.design_button_back()
        self.design_button_forward()
        self.design_progress_bar()
        self.design_question()
        self.design_button_answer1()
        self.design_button_answer2()
        self.design_button_answer3()

        self.ui.ButtonBack.clicked.connect(self.pressed_button_back)
        self.ui.ButtonForward.clicked.connect(self.pressed_button_forward)
        self.ui.ButtonAnswer1.clicked.connect(self.pressed_button_answer1)
        self.ui.ButtonAnswer2.clicked.connect(self.pressed_button_answer2)
        self.ui.ButtonAnswer3.clicked.connect(self.pressed_button_answer3)

        # Создание таймера
        self.timer = QTimer()
        # Установка интервала времени в миллисекундах
        self.timer.setInterval(1000)
        # Подключение обработчика события timeout
        self.timer.timeout.connect(self.update_timer)

        self.timer.start()

    def update_timer(self):
        self.time += 1
        # print(self.time)
        self.design_timer()

    def pressed_button_forward(self):
        if self.current_page == self.count_page - 1:
            self.timer.stop()
            for i in range(0, self.count_page):
                if functools.reduce(lambda x, y: x and y, map(lambda p, q: p == q, self.array_answers[i],
                                                              self.trueAnswers[i]), True):
                    self.count_true_answers += 1
            update_statistic_speed_test(self.time, self.count_true_answers, self.data_User.get('ID'))
            self.setCentralWidget(Window_MainWindow(self.centralWidget(), self.data_User))

        if self.current_page != self.count_page - 1:
            if self.current_page < self.count_page: self.array_answers[self.current_page] = [self.select_answer1,
                                                                                             self.select_answer2,
                                                                                             self.select_answer3]

            if (self.current_page < self.count_page) and (
                    self.select_answer1 or self.select_answer2 or self.select_answer3): self.current_page += 1

            if self.current_page < self.count_page:
                self.select_answer1 = self.array_answers[self.current_page][0]
                self.select_answer2 = self.array_answers[self.current_page][1]
                self.select_answer3 = self.array_answers[self.current_page][2]

            self.design_question()
            self.design_button_answer1()
            self.design_button_answer2()
            self.design_button_answer3()

            self.design_button_back()
            self.design_button_forward()
            self.design_progress_bar()

    def pressed_button_back(self):
        if self.current_page < self.count_page: self.array_answers[self.current_page] = [self.select_answer1,
                                                                                         self.select_answer2,
                                                                                         self.select_answer3]
        if self.current_page > 0: self.current_page -= 1

        self.select_answer1 = self.array_answers[self.current_page][0]
        self.select_answer2 = self.array_answers[self.current_page][1]
        self.select_answer3 = self.array_answers[self.current_page][2]

        self.design_button_answer1()
        self.design_button_answer2()
        self.design_button_answer3()
        self.design_button_back()
        self.design_button_forward()
        self.design_progress_bar()

    def pressed_button_answer1(self):
        self.select_answer1 = True
        self.select_answer2 = False
        self.select_answer3 = False

        self.design_button_answer1()
        self.design_button_answer2()
        self.design_button_answer3()
        self.design_button_forward()

    def pressed_button_answer2(self):
        self.select_answer1 = False
        self.select_answer2 = True
        self.select_answer3 = False

        self.design_button_answer1()
        self.design_button_answer2()
        self.design_button_answer3()
        self.design_button_forward()

    def pressed_button_answer3(self):
        self.select_answer1 = False
        self.select_answer2 = False
        self.select_answer3 = True

        self.design_button_answer1()
        self.design_button_answer2()
        self.design_button_answer3()
        self.design_button_forward()

    def design_button_back(self):
        if self.current_page == 0:
            self.ui.ButtonBack.setStyleSheet(StyleSheetForButtonUnavailable)
        else:
            self.ui.ButtonBack.setStyleSheet(StyleSheetForButtonAvailable)

    def design_button_forward(self):  # need edit!
        if self.current_page >= self.count_page - 1:
            self.ui.ButtonForward.setText('Завершить')
        else:
            self.ui.ButtonForward.setText('Далее')

        if (self.select_answer1 or self.select_answer2 or self.select_answer3) == False:
            self.ui.ButtonForward.setStyleSheet(StyleSheetForButtonUnavailable)
        else:
            self.ui.ButtonForward.setStyleSheet(StyleSheetForButtonAvailable)

    def design_progress_bar(self):
        self.ui.ProgressBar.setValue(100 * round(self.current_page / self.count_page, 2))

    def design_question(self):
        self.ui.Question.setTextInteractionFlags(Qt.TextInteractionFlag(False))
        self.ui.Question.setText(self.dataTest[self.current_page][0])

    def design_button_answer1(self):
        if (self.select_answer1):
            self.ui.ButtonAnswer1.setStyleSheet(StyleSheetForButtonSelected)
            self.ui.ButtonAnswer1.setText(self.dataTest[self.current_page][1])
        else:
            self.ui.ButtonAnswer1.setStyleSheet(StyleSheetForButtonAvailableForVariantAnswer)
            self.ui.ButtonAnswer1.setText(self.dataTest[self.current_page][1])

    def design_button_answer2(self):
        if (self.select_answer2):
            self.ui.ButtonAnswer2.setStyleSheet(StyleSheetForButtonSelected)
            self.ui.ButtonAnswer2.setText(self.dataTest[self.current_page][2])
        else:
            self.ui.ButtonAnswer2.setStyleSheet(StyleSheetForButtonAvailableForVariantAnswer)
            self.ui.ButtonAnswer2.setText(self.dataTest[self.current_page][2])

    def design_button_answer3(self):
        if (self.select_answer3):
            self.ui.ButtonAnswer3.setStyleSheet(StyleSheetForButtonSelected)
            self.ui.ButtonAnswer3.setText(self.dataTest[self.current_page][3])
        else:
            self.ui.ButtonAnswer3.setStyleSheet(StyleSheetForButtonAvailableForVariantAnswer)
            self.ui.ButtonAnswer3.setText(self.dataTest[self.current_page][3])

    def design_timer(self):
        time_text = "00:00"
        if ((self.time // 60) < 10):
            time_text = "0" + str(self.time // 60) + ":00"
        else:
            time_text = str(self.time // 60) + ":00"

        if ((self.time % 60) < 10):
            time_text = time_text[:4] + str(self.time % 60)
        else:
            time_text = time_text[:3] + str(self.time % 60)

        self.ui.Timer.setText(time_text)


class Window_MainWindowAdmin(QMainWindow):
    def __init__(self, parent, data_User: dict):
        super(Window_MainWindowAdmin, self).__init__(parent)
        self.ui = Ui_MainWindowAdmin()
        self.ui.setupUi(self)
        self.data_User = data_User

        self.ui.ButtonStatisticsUsers.clicked.connect(self.pressed_button_statistics_users)
        self.ui.ButtonTheory.clicked.connect(self.pressed_button_theory)
        self.ui.ButtonTest.clicked.connect(self.pressed_button_test)
        self.ui.ButtonSpeedTest.clicked.connect(self.pressed_button_speed_test)
        self.ui.ButtonProfile.clicked.connect(self.pressed_button_profile)
        self.ui.ButtonBack.clicked.connect(self.pressed_button_back)

    def pressed_button_statistics_users(self):
        self.setCentralWidget(Window_StatisticsUsers(self.centralWidget(), self.data_User))

    def pressed_button_back(self):
        self.setCentralWidget(Window_MainWindow(self.centralWidget(), self.data_User))

    def pressed_button_theory(self):
        return 1

    def pressed_button_test(self):
        return 1

    def pressed_button_speed_test(self):
        return 1

    def pressed_button_profile(self):
        self.setCentralWidget(Window_Profile(self.centralWidget(), self.data_User))


class Window_StatisticsUsers(QMainWindow):
    def __init__(self, parent, data_User: dict):
        super(Window_StatisticsUsers, self).__init__(parent)
        self.ui = Ui_StatisticsUsers()
        self.ui.setupUi(self)
        self.data_User = data_User

        """self.ui.tableWidget.setColumnWidth(0, 100)
        self.ui.tableWidget.setColumnWidth(1, 150)
        self.ui.tableWidget.setColumnWidth(2, 240)
        self.ui.tableWidget.setColumnWidth(3, 200)
        self.ui.tableWidget.setColumnWidth(4, 125)
        self.ui.tableWidget.setColumnWidth(5, 250)
        self.ui.tableWidget.setColumnWidth(6, 165)
"""
        self.data_statistics_users = get_data_statistics_users()

        print(self.data_statistics_users)
        print(len(self.data_statistics_users))

        self.model = QStandardItemModel(len(self.data_statistics_users), 6)

        for i in range(len(self.data_statistics_users)):
            index = self.model.index(i, 0)
            self.model.setData(index, self.data_statistics_users[i]['Surname'])
            index = self.model.index(i, 1)
            self.model.setData(index, self.data_statistics_users[i]['Name'])
            index = self.model.index(i, 2)
            self.model.setData(index, self.data_statistics_users[i]['Surname2'])
            index = self.model.index(i, 3)
            self.model.setData(index, self.data_statistics_users[i]['Test'])
            index = self.model.index(i, 4)
            self.model.setData(index, self.data_statistics_users[i]['SpeedTest'])
            index = self.model.index(i, 5)
            self.model.setData(index, self.data_statistics_users[i]['Time'])

        self.ui.tableWidget.setModel(self.model)

        self.model2 = QStandardItemModel(1, 6)
        index = self.model2.index(0, 0)
        self.model2.setData(index, "Фамилия")
        index = self.model2.index(0, 1)
        self.model2.setData(index, "Имя")
        index = self.model2.index(0, 2)
        self.model2.setData(index, "Отчество")
        index = self.model2.index(0, 3)
        self.model2.setData(index, "Тест")
        index = self.model2.index(0, 4)
        self.model2.setData(index, "Скоростной тест")
        index = self.model2.index(0, 5)
        self.model2.setData(index, "Время")
        self.ui.tableWidget.horizontalHeader().setModel(self.model2)

        for i in range(len(self.data_statistics_users)):
            self.ui.tableWidget.verticalHeader().resizeSection(i, 50)
            self.ui.tableWidget.horizontalHeader().resizeSection(0, 150)
            self.ui.tableWidget.horizontalHeader().resizeSection(1, 258)
            self.ui.tableWidget.horizontalHeader().resizeSection(2, 220)
            self.ui.tableWidget.horizontalHeader().resizeSection(3, 125)
            self.ui.tableWidget.horizontalHeader().resizeSection(4, 250)
            self.ui.tableWidget.horizontalHeader().resizeSection(5, 175)

        """
        for i in range(len(self.data_statistics_users)):
            self.ui.tableWidget.setItem(i, 0,
                                        PySide6.QtWidgets.QTableWidgetItem(self.data_statistics_users[i]['Number']))
            self.ui.tableWidget.setItem(i, 1,
                                        PySide6.QtWidgets.QTableWidgetItem(self.data_statistics_users[i]['Surname']))
            self.ui.tableWidget.setItem(i, 2, PySide6.QtWidgets.QTableWidgetItem(self.data_statistics_users[i]['Name']))
            self.ui.tableWidget.setItem(i, 3,
                                        PySide6.QtWidgets.QTableWidgetItem(self.data_statistics_users[i]['Surname2']))
            self.ui.tableWidget.setItem(i, 4, PySide6.QtWidgets.QTableWidgetItem(self.data_statistics_users[i]['Test']))
            self.ui.tableWidget.setItem(i, 5,
                                        PySide6.QtWidgets.QTableWidgetItem(self.data_statistics_users[i]['SpeedTest']))
            self.ui.tableWidget.setItem(i, 6, PySide6.QtWidgets.QTableWidgetItem(self.data_statistics_users[i]['Time']))
        """
