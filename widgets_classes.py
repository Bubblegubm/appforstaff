from PySide6.QtCore import Qt
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QApplication, QMainWindow

from authorization import Ui_Authorization
from registration import Ui_Registration
from main_window import Ui_MainWindow
from theory import Ui_Theory
from test import Ui_Test
from recover_password_1 import Ui_RecoverPassword1
from recover_password_2 import Ui_RecoverPassword2

from functions import check_valid_input_registration

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_Authorization()
        self.ui.setupUi(self)

        self.setCentralWidget(Window_Authorization(self.centralWidget()))

class Window_Authorization(QMainWindow):
    def __init__(self, parent = None):
        super(Window_Authorization, self).__init__(parent)

        self.ui = Ui_Authorization()
        self.ui.setupUi(self)

        self.ui.IconFailLogin.setVisible(False)
        self.ui.IconFailPassword.setVisible(False)

        self.ui.ButtonRegistration.clicked.connect(self.pressed_button_registration)
        self.ui.ButtonAuthorization.clicked.connect(self.pressed_button_authorization)

    def pressed_button_registration(self):
        self.setCentralWidget(Window_Registration(self.centralWidget()))

    def pressed_button_authorization(self):
        self.setCentralWidget(Window_MainWindow(self.centralWidget()))

class Window_Registration(QMainWindow):
    def __init__(self, parent):
        super(Window_Registration, self).__init__(parent)
        self.ui = Ui_Registration()
        self.ui.setupUi(self)

        self.ui.IconFailSurname.setVisible(False)
        self.ui.IconFailName.setVisible(False)
        self.ui.IconFailSurname2.setVisible(False)
        self.ui.IconFailLoginNone.setVisible(False)
        self.ui.IconFailLoginBusy.setVisible(False)
        self.ui.IconFailPassword.setVisible(False)
        self.ui.IconFailSecretWord.setVisible(False)

        self.ui.ButtonBack.clicked.connect(self.pressed_button_back)
        self.ui.ButtonRegistration.clicked.connect(self.pressed_button_registration)

    def pressed_button_back(self):
        self.setCentralWidget(Window_Authorization(self.centralWidget()))

    def pressed_button_registration(self):
        a, b, c, d, e, f = check_valid_input_registration(self.ui.Surname.text(), self.ui.Name.text(),
                                          self.ui.Surname2.text(), self.ui.Login.text(),
                                          self.ui.Password.text(), self.ui.SecretWord.text())
        #print(a, b, c, d, e, f)

        if a == 1: self.ui.IconFailSurname.setVisible(True)
        else: self.ui.IconFailSurname.setVisible(False)

        if b == 1: self.ui.IconFailName.setVisible(True)
        else: self.ui.IconFailName.setVisible(False)

        if c == 1: self.ui.IconFailSurname2.setVisible(True)
        else: self.ui.IconFailSurname2.setVisible(False)

        if d == 1: self.ui.IconFailLoginNone.setVisible(True)
        elif d == 2: self.ui.IconFailLoginBusy.setVisible(True)
        else:
            self.ui.IconFailLoginNone.setVisible(False)
            self.ui.IconFailLoginBusy.setVisible(False)

        if e == 1: self.ui.IconFailPassword.setVisible(True)
        else: self.ui.IconFailPassword.setVisible(False)

        if f == 1: self.ui.IconFailSecretWord.setVisible(True)
        else: self.ui.IconFailSecretWord.setVisible(False)

        if not (a or b or c or d or e or f): self.setCentralWidget(Window_MainWindow(self.centralWidget()))

class Window_MainWindow(QMainWindow):
    def __init__(self, parent):
        super(Window_MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.ButtonTheory.clicked.connect(self.pressed_button_theory)
        self.ui.ButtonTest.clicked.connect(self.pressed_button_test)
        self.ui.ButtonCompetition.clicked.connect(self.pressed_button_competition)

    def pressed_button_theory(self):
        self.setCentralWidget(Window_Theory(self.centralWidget()))

    def pressed_button_test(self):
        self.setCentralWidget(Window_Test(self.centralWidget()))

    def pressed_button_competition(self):
        return 1


class Window_Theory(QMainWindow):
    def __init__(self, parent):
        super(Window_Theory, self).__init__(parent)
        self.ui = Ui_Theory()
        self.ui.setupUi(self)

        self.current_page = 0
        self.count_page = 5
        self.design_button_back()
        self.design_button_forward()
        self.design_progress_bar()
        self.design_question()
        self.design_answer()

        self.ui.ButtonBack.clicked.connect(self.pressed_button_back)
        self.ui.ButtonForward.clicked.connect(self.pressed_button_forward)

    def pressed_button_forward(self):
        if self.current_page < self.count_page: self.current_page += 1
        self.design_button_back()
        self.design_button_forward()
        self.design_progress_bar()

    def pressed_button_back(self):
        if self.current_page > 0: self.current_page -= 1
        self.design_button_back()
        self.design_button_forward()
        self.design_progress_bar()

    def design_button_back(self):
        if self.current_page == 0: self.ui.ButtonBack.setStyleSheet(u"color: rgba(255, 255, 255, 100);\n"
            "border: 3px solid rgb(255, 255, 255);\n"
            "border-radius: 7px;\n"
            "font: 26pt \"Ambient(RUS BY LYAJKA)\";\n"
            "background-color: rgba(0, 0, 0, 100);\n"
            "width: 50px;\n")
        else: self.ui.ButtonBack.setStyleSheet(u"QPushButton{\n"
            "color: rgba(255, 255, 255, 255);\n"
            "border: 3px solid rgb(255, 255, 255);\n"
            "border-radius: 7px;\n"
            "font: 26pt \"Ambient(RUS BY LYAJKA)\";\n"
            "background-color: rgba(0, 0, 0, 100);\n"
            "width: 50px;\n"
            "}\n"
            "\n"
            "QPushButton::hover{\n"
            "background-color: rgba(0, 0, 0, 150);\n"
            "}\n"
            "\n"
            "QPushButton::pressed{\n"
            "background-color: rgba(0, 0, 0, 200);\n"
            "}")

    def design_button_forward(self):
        if self.current_page >= self.count_page - 1:
            self.ui.ButtonForward.setText('Завершить')
        else:
            self.ui.ButtonForward.setText('Далее')

    def design_progress_bar(self):
        self.ui.ProgressBar.setValue(100 * round(self.current_page / self.count_page, 2))

    def design_question(self):
        self.ui.Question.setTextInteractionFlags(Qt.TextInteractionFlag(False))

    def design_answer(self):
        self.ui.Answer.setTextInteractionFlags(Qt.TextInteractionFlag(False))


class Window_Test(QMainWindow):
    def __init__(self, parent):
        super(Window_Test, self).__init__(parent)
        self.ui = Ui_Test()
        self.ui.setupUi(self)
        self.current_page = 0
        self.count_page = 3

        self.design_button_back()
        self.design_button_forward()
        self.design_progress_bar()
        self.design_question()

        self.ui.ButtonBack.clicked.connect(self.pressed_button_back)
        self.ui.ButtonForward.clicked.connect(self.pressed_button_forward)

    def pressed_button_forward(self):
        if self.current_page < self.count_page: self.current_page += 1
        self.design_button_back()
        self.design_button_forward()
        self.design_progress_bar()

    def pressed_button_back(self):
        if self.current_page > 0: self.current_page -= 1
        self.design_button_back()
        self.design_button_forward()
        self.design_progress_bar()

    def pressed_button_answer1(self):
        return 1

    def pressed_button_answer2(self):
        return 1

    def pressed_button_answer3(self):
        return 1

    def design_button_back(self):
        if self.current_page == 0: self.ui.ButtonBack.setStyleSheet(u"color: rgba(255, 255, 255, 100);\n"
            "border: 3px solid rgb(255, 255, 255);\n"
            "border-radius: 7px;\n"
            "font: 26pt \"Ambient(RUS BY LYAJKA)\";\n"
            "background-color: rgba(0, 0, 0, 100);\n"
            "width: 50px;\n")
        else: self.ui.ButtonBack.setStyleSheet(u"QPushButton{\n"
            "color: rgba(255, 255, 255, 255);\n"
            "border: 3px solid rgb(255, 255, 255);\n"
            "border-radius: 7px;\n"
            "font: 26pt \"Ambient(RUS BY LYAJKA)\";\n"
            "background-color: rgba(0, 0, 0, 100);\n"
            "width: 50px;\n"
            "}\n"
            "\n"
            "QPushButton::hover{\n"
            "background-color: rgba(0, 0, 0, 150);\n"
            "}\n"
            "\n"
            "QPushButton::pressed{\n"
            "background-color: rgba(0, 0, 0, 200);\n"
            "}")

    def design_button_forward(self):
        if self.current_page >= self.count_page - 1:
            self.ui.ButtonForward.setText('Завершить')
        else: self.ui.ButtonForward.setText('Далее')

    def design_progress_bar(self):
        self.ui.ProgressBar.setValue(100 * round(self.current_page / self.count_page, 2))

    def design_question(self):
        self.ui.Question.setTextInteractionFlags(Qt.TextInteractionFlag(False))


class Window_RecoverPassword1(QMainWindow):
    def __init__(self, parent):
        super(Window_RecoverPassword1, self).__init__(parent)
        self.ui = Ui_RecoverPassword1()
        self.ui.setupUi(self)

class Window_RecoverPassword2(QMainWindow):
    def __init__(self, parent):
        super(Window_RecoverPassword2, self).__init__(parent)
        self.ui = Ui_RecoverPassword2()
        self.ui.setupUi(self)