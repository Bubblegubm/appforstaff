# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'authorization.ui'
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
import logo_rc


class Ui_Authorization(object):
    def setupUi(self, Authorization):
        if not Authorization.objectName():
            Authorization.setObjectName(u"Authorization")
        Authorization.resize(1280, 720)
        Authorization.setFocusPolicy(Qt.ClickFocus)
        Authorization.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0.358, y1:0.266636, x2:1, y2:1, stop:0 rgba(163, 5, 255, 255), stop:1 rgba(92, 51, 255, 255))")
        self.centralwidget = QWidget(Authorization)
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
        self.ButtonAuthorization = QPushButton(self.centralwidget)
        self.ButtonAuthorization.setObjectName(u"ButtonAuthorization")
        self.ButtonAuthorization.setEnabled(True)
        self.ButtonAuthorization.setGeometry(QRect(770, 420, 130, 50))
        self.ButtonAuthorization.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Ambient(RUS BY LYAJKA)"])
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        self.ButtonAuthorization.setFont(font)
        self.ButtonAuthorization.setStyleSheet(u"QPushButton{\n"
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
        self.ButtonProblemsWithAuthorization = QPushButton(self.centralwidget)
        self.ButtonProblemsWithAuthorization.setObjectName(u"ButtonProblemsWithAuthorization")
        self.ButtonProblemsWithAuthorization.setEnabled(True)
        self.ButtonProblemsWithAuthorization.setGeometry(QRect(770, 490, 400, 50))
        self.ButtonProblemsWithAuthorization.setMinimumSize(QSize(0, 0))
        self.ButtonProblemsWithAuthorization.setMaximumSize(QSize(800, 100))
        self.ButtonProblemsWithAuthorization.setSizeIncrement(QSize(300, 100))
        self.ButtonProblemsWithAuthorization.setStyleSheet(u"QPushButton{\n"
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
        self.LableAuthorization = QLabel(self.centralwidget)
        self.LableAuthorization.setObjectName(u"LableAuthorization")
        self.LableAuthorization.setGeometry(QRect(770, 150, 400, 100))
        self.LableAuthorization.setSizeIncrement(QSize(400, 100))
        self.LableAuthorization.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                              "font: 40pt \"Ambient(RUS BY LYAJKA)\";\n"
                                              "background-color: rgba(255, 255, 255, 50);\n"
                                              "border: 3px solid rgb(255, 255, 255);\n"
                                              "border-radius: 30px;\n"
                                              "\n"
                                              "")
        self.LableAuthorization.setAlignment(Qt.AlignCenter)
        self.IconFailLogin = QLabel(self.centralwidget)
        self.IconFailLogin.setObjectName(u"IconFailLogin")
        self.IconFailLogin.setGeometry(QRect(1180, 280, 50, 50))
        self.IconFailLogin.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                         "border: 3px solid rgb(255, 255, 255);\n"
                                         "border-radius: 7px;\n"
                                         "font: 26pt \"Ambient(RUS BY LYAJKA)\";\n"
                                         "background-color: rgba(0, 0, 0, 100);")
        self.IconFailLogin.setAlignment(Qt.AlignCenter)
        self.IconFailPassword = QLabel(self.centralwidget)
        self.IconFailPassword.setObjectName(u"IconFailPassword")
        self.IconFailPassword.setGeometry(QRect(1180, 350, 50, 50))
        self.IconFailPassword.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                            "border: 3px solid rgb(255, 255, 255);\n"
                                            "border-radius: 7px;\n"
                                            "font: 26pt \"Ambient(RUS BY LYAJKA)\";\n"
                                            "background-color: rgba(0, 0, 0, 100);")
        self.IconFailPassword.setAlignment(Qt.AlignCenter)
        self.Logo = QLabel(self.centralwidget)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setGeometry(QRect(146, 96, 478, 528))
        self.Logo.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.Logo.setPixmap(QPixmap(u":/logo/images/without back 478x528.png"))
        Authorization.setCentralWidget(self.centralwidget)

        self.retranslateUi(Authorization)

        QMetaObject.connectSlotsByName(Authorization)

    # setupUi

    def retranslateUi(self, Authorization):
        Authorization.setWindowTitle(QCoreApplication.translate("Authorization", u"MainWindow", None))
        self.Login.setText("")
        self.Login.setPlaceholderText(
            QCoreApplication.translate("Authorization", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.ButtonAuthorization.setText(QCoreApplication.translate("Authorization", u"\u0412\u0445\u043e\u0434", None))
        self.ButtonRegistration.setText(QCoreApplication.translate("Authorization",
                                                                   u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f",
                                                                   None))
        self.Password.setText("")
        self.Password.setPlaceholderText(
            QCoreApplication.translate("Authorization", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.ButtonProblemsWithAuthorization.setText(QCoreApplication.translate("Authorization",
                                                                                u"\u041f\u0440\u043e\u0431\u043b\u0435\u043c\u044b \u0441\u043e \u0432\u0445\u043e\u0434\u043e\u043c",
                                                                                None))
        self.LableAuthorization.setText(QCoreApplication.translate("Authorization",
                                                                   u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f",
                                                                   None))
        self.IconFailLogin.setText(QCoreApplication.translate("Authorization", u"!", None))
        self.IconFailPassword.setText(QCoreApplication.translate("Authorization", u"!", None))
        self.Logo.setText("")
    # retranslateUi
