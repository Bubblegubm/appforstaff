# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'entrance.ui'
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

class Ui_Antrance(object):
    def setupUi(self, Antrance):
        if not Antrance.objectName():
            Antrance.setObjectName(u"Antrance")
        Antrance.resize(1280, 720)
        Antrance.setFocusPolicy(Qt.ClickFocus)
        Antrance.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.358, y1:0.266636, x2:1, y2:1, stop:0 rgba(163, 5, 255, 255), stop:1 rgba(92, 51, 255, 255))")
        self.centralwidget = QWidget(Antrance)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Login = QLineEdit(self.centralwidget)
        self.Login.setObjectName(u"Login")
        self.Login.setEnabled(True)
        self.Login.setGeometry(QRect(770, 280, 400, 50))
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
        self.ButtonAntrance = QPushButton(self.centralwidget)
        self.ButtonAntrance.setObjectName(u"ButtonAntrance")
        self.ButtonAntrance.setEnabled(True)
        self.ButtonAntrance.setGeometry(QRect(770, 420, 130, 50))
        self.ButtonAntrance.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Ambient(RUS BY LYAJKA)"])
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        self.ButtonAntrance.setFont(font)
        self.ButtonAntrance.setStyleSheet(u"QPushButton{\n"
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
        self.ButtonRegistration = QPushButton(self.centralwidget)
        self.ButtonRegistration.setObjectName(u"ButtonRegistration")
        self.ButtonRegistration.setEnabled(True)
        self.ButtonRegistration.setGeometry(QRect(920, 420, 250, 50))
        self.ButtonRegistration.setMinimumSize(QSize(0, 0))
        self.ButtonRegistration.setMaximumSize(QSize(800, 100))
        self.ButtonRegistration.setSizeIncrement(QSize(300, 100))
        self.ButtonRegistration.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"font: 26pt \"Ambient(RUS BY LYAJKA)\";\n"
"background-color: rgba(0, 0, 0, 100);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgba(0, 0, 0, 150);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgba(0, 0, 0, 200);\n"
"}")
        self.Password = QLineEdit(self.centralwidget)
        self.Password.setObjectName(u"Password")
        self.Password.setEnabled(True)
        self.Password.setGeometry(QRect(770, 350, 400, 50))
        self.Password.setMinimumSize(QSize(0, 0))
        self.Password.setSizeIncrement(QSize(300, 40))
        self.Password.setBaseSize(QSize(300, 40))
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
        self.ButtonProblemsWithAntrance = QPushButton(self.centralwidget)
        self.ButtonProblemsWithAntrance.setObjectName(u"ButtonProblemsWithAntrance")
        self.ButtonProblemsWithAntrance.setEnabled(True)
        self.ButtonProblemsWithAntrance.setGeometry(QRect(770, 490, 400, 50))
        self.ButtonProblemsWithAntrance.setMinimumSize(QSize(0, 0))
        self.ButtonProblemsWithAntrance.setMaximumSize(QSize(800, 100))
        self.ButtonProblemsWithAntrance.setSizeIncrement(QSize(300, 100))
        self.ButtonProblemsWithAntrance.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"font: 26pt \"Ambient(RUS BY LYAJKA)\";\n"
"background-color: rgba(0, 0, 0, 100);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgba(0, 0, 0, 150);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgba(0, 0, 0, 200);\n"
"}")
        self.LableAntrance = QLabel(self.centralwidget)
        self.LableAntrance.setObjectName(u"LableAntrance")
        self.LableAntrance.setGeometry(QRect(770, 150, 400, 100))
        self.LableAntrance.setSizeIncrement(QSize(400, 100))
        self.LableAntrance.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 40pt \"Ambient(RUS BY LYAJKA)\";\n"
"background-color: rgba(255, 255, 255, 50);\n"
"border: 3px solid rgb(255, 255, 255);\n"
"border-radius: 30px;\n"
"\n"
"")
        self.LableAntrance.setAlignment(Qt.AlignCenter)
        Antrance.setCentralWidget(self.centralwidget)

        self.retranslateUi(Antrance)

        QMetaObject.connectSlotsByName(Antrance)
    # setupUi

    def retranslateUi(self, Antrance):
        Antrance.setWindowTitle(QCoreApplication.translate("Antrance", u"MainWindow", None))
        self.Login.setText("")
        self.Login.setPlaceholderText(QCoreApplication.translate("Antrance", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.ButtonAntrance.setText(QCoreApplication.translate("Antrance", u"\u0412\u0445\u043e\u0434", None))
        self.ButtonRegistration.setText(QCoreApplication.translate("Antrance", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.Password.setText("")
        self.Password.setPlaceholderText(QCoreApplication.translate("Antrance", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.ButtonProblemsWithAntrance.setText(QCoreApplication.translate("Antrance", u"\u041f\u0440\u043e\u0431\u043b\u0435\u043c\u044b \u0441\u043e \u0432\u0445\u043e\u0434\u043e\u043c", None))
        self.LableAntrance.setText(QCoreApplication.translate("Antrance", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
    # retranslateUi

