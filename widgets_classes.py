import sys
import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow

from entrance import Ui_Antrance
from registration import Ui_Registration
from main_window import Ui_MainWindow

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

        self.ui.ButtonBack.clicked.connect(self.open_window_entrance)

    def open_window_entrance(self):
        self.setCentralWidget(Window_Antrance(self.centralWidget()))

class Window_MainWindow(QMainWindow):
    def __init__(self, parent):
        super(Window_MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

class Window_Test(QMainWindow):
    def __init__(self, parent):
        super(Window_Test, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

class Window_Theory(QMainWindow):
    def __init__(self, parent):
        super(Window_Theory, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)