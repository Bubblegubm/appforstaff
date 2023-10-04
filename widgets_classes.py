import sys
import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow

from entrance import Ui_Antrance
from registration import Ui_Registration
from main_window import Ui_MainWindow

from functions import check_valid_input

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_Antrance()
        self.ui.setupUi(self)

        self.setCentralWidget(Window_Antrance(self.centralWidget()))

class Window_Antrance(QMainWindow):
    def __init__(self, parent = None):
        super(Window_Antrance, self).__init__(parent)

        self.ui = Ui_Antrance()
        self.ui.setupUi(self)

        self.ui.IconFailLogin.setVisible(False)
        self.ui.IconFailPassword.setVisible(False)

        self.ui.ButtonRegistration.clicked.connect(self.open_window_registration)
        self.ui.ButtonAntrance.clicked.connect(self.pressed_button_antrance)

    def open_window_registration(self):
        self.setCentralWidget(Window_Registration(self.centralWidget()))

    def pressed_button_antrance(self):
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

        self.ui.ButtonBack.clicked.connect(self.open_window_entrance)
        self.ui.ButtonRegistration.clicked.connect(self.pressed_button_registration)

    def open_window_entrance(self):
        self.setCentralWidget(Window_Antrance(self.centralWidget()))

    def pressed_button_registration(self):
        a, b, c, d, e = check_valid_input(self.ui.Surname.text(), self.ui.Name.text(),
                                          self.ui.Surname2.text(), self.ui.Login.text(),
                                          self.ui.Password.text())
        print(a, b, c, d, e)

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

        if not (a or b or c or d or e): self.setCentralWidget(Window_MainWindow(self.centralWidget()))

class Window_MainWindow(QMainWindow):
    def __init__(self, parent):
        super(Window_MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def open_window_theory(self):
        self.setCentralWidget(Window_Theory(self.centralWidget()))

    def open_window_test(self):
        self.setCentralWidget(Window_Test(self.centralWidget()))

    def open_window_KVIZ(self):
        return 1

    def open_window_competition(self):
        return 1

    def open_window_statistics(self):
        return 1

class Window_Theory(QMainWindow):
    def __init__(self, parent):
        super(Window_Theory, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.current_page = 1
        self.count_page = None

    def pressed_button_forward(self):
        return 1

    def pressed_button_back(self):
        return 1

class Window_Test(QMainWindow):
    def __init__(self, parent):
        super(Window_Test, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def pressed_button_forward(self):
        return 1

    def pressed_button_back(self):
        return 1

    def pressed_button_answer1(self):
        return 1

    def pressed_button_answer2(self):
        return 1

    def pressed_button_answer3(self):
        return 1

