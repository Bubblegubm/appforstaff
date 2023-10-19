# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
                               QSizePolicy, QWidget)


class Ui_Profile(object):
    def setupUi(self, Profile):
        if not Profile.objectName():
            Profile.setObjectName(u"Profile")
        Profile.resize(1280, 720)
        Profile.setFocusPolicy(Qt.ClickFocus)
        Profile.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0.358, y1:0.266636, x2:1, y2:1, stop:0 rgba(163, 5, 255, 255), stop:1 rgba(92, 51, 255, 255))")
        self.centralwidget = QWidget(Profile)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ButtonBack = QPushButton(self.centralwidget)
        self.ButtonBack.setObjectName(u"ButtonBack")
        self.ButtonBack.setEnabled(True)
        self.ButtonBack.setGeometry(QRect(550, 620, 200, 80))
        self.ButtonBack.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Ambient(RUS BY LYAJKA)"])
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        self.ButtonBack.setFont(font)
        self.ButtonBack.setStyleSheet(u"QPushButton{\n"
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
        self.ButtonChangePassword = QPushButton(self.centralwidget)
        self.ButtonChangePassword.setObjectName(u"ButtonChangePassword")
        self.ButtonChangePassword.setEnabled(True)
        self.ButtonChangePassword.setGeometry(QRect(120, 440, 410, 80))
        self.ButtonChangePassword.setMaximumSize(QSize(16777215, 16777215))
        self.ButtonChangePassword.setFont(font)
        self.ButtonChangePassword.setStyleSheet(u"QPushButton{\n"
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
        self.ResultsTest = QLabel(self.centralwidget)
        self.ResultsTest.setObjectName(u"ResultsTest")
        self.ResultsTest.setGeometry(QRect(650, 20, 610, 220))
        self.ResultsTest.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                       "border: 3px solid rgb(255, 255, 255);\n"
                                       "border-radius: 7px;\n"
                                       "font: 36pt \"Ambient(RUS BY LYAJKA)\";\n"
                                       "background-color: rgba(0, 0, 0, 100);\n"
                                       "padding-left: 10px;")
        self.ResultsTest.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.ResultsSpeedTest = QLabel(self.centralwidget)
        self.ResultsSpeedTest.setObjectName(u"ResultsSpeedTest")
        self.ResultsSpeedTest.setGeometry(QRect(650, 260, 610, 340))
        self.ResultsSpeedTest.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                            "border: 3px solid rgb(255, 255, 255);\n"
                                            "border-radius: 7px;\n"
                                            "font: 36pt \"Ambient(RUS BY LYAJKA)\";\n"
                                            "background-color: rgba(0, 0, 0, 100);\n"
                                            "padding-left: 10px;")
        self.ResultsSpeedTest.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.NameSurnameUser = QLabel(self.centralwidget)
        self.NameSurnameUser.setObjectName(u"NameSurnameUser")
        self.NameSurnameUser.setGeometry(QRect(20, 200, 610, 220))
        self.NameSurnameUser.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                           "border: 3px solid rgb(255, 255, 255);\n"
                                           "border-radius: 7px;\n"
                                           "font: 36pt \"Ambient(RUS BY LYAJKA)\";\n"
                                           "background-color: rgba(0, 0, 0, 100);\n"
                                           "padding-left: 10px;")
        self.NameSurnameUser.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.LableProfile = QLabel(self.centralwidget)
        self.LableProfile.setObjectName(u"LableProfile")
        self.LableProfile.setGeometry(QRect(120, 60, 410, 100))
        self.LableProfile.setSizeIncrement(QSize(400, 100))
        self.LableProfile.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                        "font: 40pt \"Ambient(RUS BY LYAJKA)\";\n"
                                        "background-color: rgba(255, 255, 255, 50);\n"
                                        "border: 3px solid rgb(255, 255, 255);\n"
                                        "border-radius: 30px;\n"
                                        "\n"
                                        "")
        self.LableProfile.setAlignment(Qt.AlignCenter)
        Profile.setCentralWidget(self.centralwidget)

        self.retranslateUi(Profile)

        QMetaObject.connectSlotsByName(Profile)

    # setupUi

    def retranslateUi(self, Profile):
        Profile.setWindowTitle(QCoreApplication.translate("Profile", u"MainWindow", None))
        self.ButtonBack.setText(QCoreApplication.translate("Profile", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.ButtonChangePassword.setText(QCoreApplication.translate("Profile",
                                                                     u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c",
                                                                     None))
        self.ResultsTest.setText(QCoreApplication.translate("Profile",
                                                            u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u0442\u0435\u0441\u0442\u0430:\n"
                                                            "10 \u0438\u0437 20 \u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u044b\u0445\n"
                                                            "\u043e\u0442\u0432\u0435\u0442\u043e\u0432", None))
        self.ResultsSpeedTest.setText(QCoreApplication.translate("Profile",
                                                                 u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u043d\u043e\u0433\u043e\n"
                                                                 "\u0442\u0435\u0441\u0442\u0430:\n"
                                                                 "15 \u0438\u0437 20 \u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u044b\u0445\n"
                                                                 "\u043e\u0442\u0432\u0435\u0442\u043e\u0432\n"
                                                                 "\u041f\u0440\u043e\u0439\u0434\u0435\u043d \u0437\u0430 2 \u043c\u0438\u043d. 10 \u0441.",
                                                                 None))
        self.NameSurnameUser.setText(
            QCoreApplication.translate("Profile", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f\n"
                                                  "\u0418\u043c\u044f\n"
                                                  "\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.LableProfile.setText(
            QCoreApplication.translate("Profile", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c", None))
    # retranslateUi
