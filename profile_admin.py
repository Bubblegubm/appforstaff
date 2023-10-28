# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile_admin.ui'
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


class Ui_ProfileAdmin(object):
    def setupUi(self, ProfileAdmin):
        if not ProfileAdmin.objectName():
            ProfileAdmin.setObjectName(u"ProfileAdmin")
        ProfileAdmin.resize(1280, 720)
        ProfileAdmin.setFocusPolicy(Qt.ClickFocus)
        ProfileAdmin.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0.358, y1:0.266636, x2:1, y2:1, stop:0\n"
            "                rgba(163, 5, 255, 255), stop:1 rgba(92, 51, 255, 255))\n"
            "            ")
        self.centralwidget = QWidget(ProfileAdmin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ButtonBack = QPushButton(self.centralwidget)
        self.ButtonBack.setObjectName(u"ButtonBack")
        self.ButtonBack.setEnabled(True)
        self.ButtonBack.setGeometry(QRect(540, 620, 200, 80))
        self.ButtonBack.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Ambient(RUS BY LYAJKA)"])
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        self.ButtonBack.setFont(font)
        self.ButtonBack.setStyleSheet(u"QPushButton{\n"
                                      "                        color: rgb(255, 255, 255);\n"
                                      "                        border: 3px solid rgb(255, 255, 255);\n"
                                      "                        border-radius: 7px;\n"
                                      "                        font: 26pt \"Ambient(RUS BY LYAJKA)\";\n"
                                      "                        background-color: rgba(0, 0, 0, 100);\n"
                                      "                        width: 50px;\n"
                                      "                        }\n"
                                      "\n"
                                      "                        QPushButton::hover{\n"
                                      "                        background-color: rgba(0, 0, 0, 150);\n"
                                      "                        }\n"
                                      "\n"
                                      "                        QPushButton::pressed{\n"
                                      "                        background-color: rgba(0, 0, 0, 200);\n"
                                      "                        }\n"
                                      "                    ")
        self.ButtonChangePassword = QPushButton(self.centralwidget)
        self.ButtonChangePassword.setObjectName(u"ButtonChangePassword")
        self.ButtonChangePassword.setEnabled(True)
        self.ButtonChangePassword.setGeometry(QRect(440, 450, 400, 80))
        self.ButtonChangePassword.setMaximumSize(QSize(16777215, 16777215))
        self.ButtonChangePassword.setFont(font)
        self.ButtonChangePassword.setStyleSheet(u"QPushButton{\n"
                                                "                        color: rgb(255, 255, 255);\n"
                                                "                        border: 3px solid rgb(255, 255, 255);\n"
                                                "                        border-radius: 7px;\n"
                                                "                        font: 26pt \"Ambient(RUS BY LYAJKA)\";\n"
                                                "                        background-color: rgba(0, 0, 0, 100);\n"
                                                "                        width: 50px;\n"
                                                "                        }\n"
                                                "\n"
                                                "                        QPushButton::hover{\n"
                                                "                        background-color: rgba(0, 0, 0, 150);\n"
                                                "                        }\n"
                                                "\n"
                                                "                        QPushButton::pressed{\n"
                                                "                        background-color: rgba(0, 0, 0, 200);\n"
                                                "                        }\n"
                                                "                    ")
        self.NameSurnameAdmin = QLabel(self.centralwidget)
        self.NameSurnameAdmin.setObjectName(u"NameSurnameAdmin")
        self.NameSurnameAdmin.setGeometry(QRect(340, 200, 600, 220))
        self.NameSurnameAdmin.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                            "                        border: 3px solid rgb(255, 255, 255);\n"
                                            "                        border-radius: 7px;\n"
                                            "                        font: 36pt \"Ambient(RUS BY LYAJKA)\";\n"
                                            "                        background-color: rgba(0, 0, 0, 100);\n"
                                            "                        padding-left: 10px;\n"
                                            "                    ")
        self.NameSurnameAdmin.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.LableProfile = QLabel(self.centralwidget)
        self.LableProfile.setObjectName(u"LableProfile")
        self.LableProfile.setGeometry(QRect(440, 50, 400, 100))
        self.LableProfile.setSizeIncrement(QSize(400, 100))
        self.LableProfile.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                        "                        font: 40pt \"Ambient(RUS BY LYAJKA)\";\n"
                                        "                        background-color: rgba(255, 255, 255, 50);\n"
                                        "                        border: 3px solid rgb(255, 255, 255);\n"
                                        "                        border-radius: 30px;\n"
                                        "\n"
                                        "                    ")
        self.LableProfile.setAlignment(Qt.AlignCenter)
        ProfileAdmin.setCentralWidget(self.centralwidget)

        self.retranslateUi(ProfileAdmin)

        QMetaObject.connectSlotsByName(ProfileAdmin)

    # setupUi

    def retranslateUi(self, ProfileAdmin):
        ProfileAdmin.setWindowTitle(QCoreApplication.translate("ProfileAdmin", u"MainWindow", None))
        self.ButtonBack.setText(QCoreApplication.translate("ProfileAdmin", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.ButtonChangePassword.setText(QCoreApplication.translate("ProfileAdmin",
                                                                     u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c",
                                                                     None))
        self.NameSurnameAdmin.setText(
            QCoreApplication.translate("ProfileAdmin", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f\n"
                                                       "\u0418\u043c\u044f\n"
                                                       "\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.LableProfile.setText(
            QCoreApplication.translate("ProfileAdmin", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c", None))
    # retranslateUi
