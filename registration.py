# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registration.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setFocusPolicy(Qt.ClickFocus)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.358, y1:0.266636, x2:1, y2:1, stop:0 rgba(163, 5, 255, 255), stop:1 rgba(92, 51, 255, 255))")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Surname = QLineEdit(self.centralwidget)
        self.Surname.setObjectName(u"Surname")
        self.Surname.setEnabled(True)
        self.Surname.setGeometry(QRect(440, 210, 400, 50))
        self.Surname.setMinimumSize(QSize(0, 0))
        self.Surname.setSizeIncrement(QSize(300, 40))
        self.Surname.setBaseSize(QSize(300, 40))
        self.Surname.setMouseTracking(True)
        self.Surname.setTabletTracking(False)
        self.Surname.setFocusPolicy(Qt.ClickFocus)
        self.Surname.setStyleSheet(u"QLineEdit{\n"
"color: rgb(255, 255, 255);\n"
"font: 20pt \"Ambient(RUS BY LYAJKA)\";\n"
"background-color: rgba(0, 0, 0, 150);\n"
"border: 3px solid rgba(255, 255, 255, 255);\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"}\n"
"QLineEdit::hover{\n"
"background-color: rgba(0, 0, 0, 100);\n"
"}\n"
"QLineEdit::focus{\n"
"background-color: rgba(0, 0, 0, 200)\n"
"}")
        self.Surname.setAlignment(Qt.AlignCenter)
        self.ButtonRegistration = QPushButton(self.centralwidget)
        self.ButtonRegistration.setObjectName(u"ButtonRegistration")
        self.ButtonRegistration.setEnabled(True)
        self.ButtonRegistration.setGeometry(QRect(440, 570, 400, 50))
        self.ButtonRegistration.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Ambient(RUS BY LYAJKA)"])
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        self.ButtonRegistration.setFont(font)
        self.ButtonRegistration.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
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
        self.Name = QLineEdit(self.centralwidget)
        self.Name.setObjectName(u"Name")
        self.Name.setEnabled(True)
        self.Name.setGeometry(QRect(440, 280, 400, 50))
        self.Name.setMinimumSize(QSize(0, 0))
        self.Name.setSizeIncrement(QSize(300, 40))
        self.Name.setBaseSize(QSize(300, 40))
        self.Name.setMouseTracking(True)
        self.Name.setTabletTracking(False)
        self.Name.setFocusPolicy(Qt.ClickFocus)
        self.Name.setStyleSheet(u"QLineEdit{\n"
"color: rgb(255, 255, 255);\n"
"font: 20pt \"Ambient(RUS BY LYAJKA)\";\n"
"background-color: rgba(0, 0, 0, 150);\n"
"border: 3px solid rgba(255, 255, 255, 255);\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"}\n"
"QLineEdit::hover{\n"
"background-color: rgba(0, 0, 0, 100);\n"
"}\n"
"QLineEdit::focus{\n"
"background-color: rgba(0, 0, 0, 200)\n"
"}")
        self.Name.setAlignment(Qt.AlignCenter)
        self.Surname2 = QLineEdit(self.centralwidget)
        self.Surname2.setObjectName(u"Surname2")
        self.Surname2.setEnabled(True)
        self.Surname2.setGeometry(QRect(440, 350, 400, 50))
        self.Surname2.setMinimumSize(QSize(0, 0))
        self.Surname2.setSizeIncrement(QSize(300, 40))
        self.Surname2.setBaseSize(QSize(300, 40))
        self.Surname2.setMouseTracking(True)
        self.Surname2.setTabletTracking(False)
        self.Surname2.setFocusPolicy(Qt.ClickFocus)
        self.Surname2.setStyleSheet(u"QLineEdit{\n"
"color: rgb(255, 255, 255);\n"
"font: 20pt \"Ambient(RUS BY LYAJKA)\";\n"
"background-color: rgba(0, 0, 0, 150);\n"
"border: 3px solid rgba(255, 255, 255, 255);\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"}\n"
"QLineEdit::hover{\n"
"background-color: rgba(0, 0, 0, 100);\n"
"}\n"
"QLineEdit::focus{\n"
"background-color: rgba(0, 0, 0, 200)\n"
"}")
        self.Surname2.setAlignment(Qt.AlignCenter)
        self.Login = QLineEdit(self.centralwidget)
        self.Login.setObjectName(u"Login")
        self.Login.setEnabled(True)
        self.Login.setGeometry(QRect(440, 420, 400, 50))
        self.Login.setMinimumSize(QSize(0, 0))
        self.Login.setSizeIncrement(QSize(300, 40))
        self.Login.setBaseSize(QSize(300, 40))
        self.Login.setMouseTracking(True)
        self.Login.setTabletTracking(False)
        self.Login.setFocusPolicy(Qt.ClickFocus)
        self.Login.setStyleSheet(u"QLineEdit{\n"
"color: rgb(255, 255, 255);\n"
"font: 20pt \"Ambient(RUS BY LYAJKA)\";\n"
"background-color: rgba(0, 0, 0, 150);\n"
"border: 3px solid rgba(255, 255, 255, 255);\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"}\n"
"QLineEdit::hover{\n"
"background-color: rgba(0, 0, 0, 100);\n"
"}\n"
"QLineEdit::focus{\n"
"background-color: rgba(0, 0, 0, 200)\n"
"}")
        self.Login.setAlignment(Qt.AlignCenter)
        self.Password = QLineEdit(self.centralwidget)
        self.Password.setObjectName(u"Password")
        self.Password.setEnabled(True)
        self.Password.setGeometry(QRect(440, 490, 400, 50))
        self.Password.setMinimumSize(QSize(0, 0))
        self.Password.setSizeIncrement(QSize(300, 40))
        self.Password.setBaseSize(QSize(300, 40))
        self.Password.setMouseTracking(True)
        self.Password.setTabletTracking(False)
        self.Password.setFocusPolicy(Qt.ClickFocus)
        self.Password.setStyleSheet(u"QLineEdit{\n"
"color: rgb(255, 255, 255);\n"
"font: 20pt \"Ambient(RUS BY LYAJKA)\";\n"
"background-color: rgba(0, 0, 0, 150);\n"
"border: 3px solid rgba(255, 255, 255, 255);\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"}\n"
"QLineEdit::hover{\n"
"background-color: rgba(0, 0, 0, 100);\n"
"}\n"
"QLineEdit::focus{\n"
"background-color: rgba(0, 0, 0, 200)\n"
"}")
        self.Password.setAlignment(Qt.AlignCenter)
        self.LabelRegistration = QLabel(self.centralwidget)
        self.LabelRegistration.setObjectName(u"LabelRegistration")
        self.LabelRegistration.setGeometry(QRect(440, 80, 400, 100))
        self.LabelRegistration.setSizeIncrement(QSize(400, 100))
        self.LabelRegistration.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 40pt \"Ambient(RUS BY LYAJKA)\";\n"
"background-color: rgba(255, 255, 255, 50);\n"
"border: 3px solid rgb(255, 255, 255);\n"
"border-radius: 30px;\n"
"\n"
"")
        self.LabelRegistration.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Surname.setText("")
        self.Surname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.ButtonRegistration.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
        self.Name.setText("")
        self.Name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.Surname2.setText("")
        self.Surname2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.Login.setText("")
        self.Login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.Password.setText("")
        self.Password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.LabelRegistration.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
    # retranslateUi

