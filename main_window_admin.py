# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_admin.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
                               QWidget)


class Ui_MainWindowAdmin(object):
    def setupUi(self, MainWindowAdmin):
        if not MainWindowAdmin.objectName():
            MainWindowAdmin.setObjectName(u"MainWindowAdmin")
        MainWindowAdmin.resize(1280, 720)
        MainWindowAdmin.setFocusPolicy(Qt.ClickFocus)
        MainWindowAdmin.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0.358, y1:0.266636, x2:1, y2:1, stop:0 rgba(163, 5, 255, 255), stop:1 rgba(92, 51, 255, 255))")
        self.centralwidget = QWidget(MainWindowAdmin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ButtonTheory = QPushButton(self.centralwidget)
        self.ButtonTheory.setObjectName(u"ButtonTheory")
        self.ButtonTheory.setEnabled(True)
        self.ButtonTheory.setGeometry(QRect(390, 270, 500, 80))
        self.ButtonTheory.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Ambient(RUS BY LYAJKA)"])
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        self.ButtonTheory.setFont(font)
        self.ButtonTheory.setStyleSheet(u"QPushButton{\n"
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
        self.ButtonTest = QPushButton(self.centralwidget)
        self.ButtonTest.setObjectName(u"ButtonTest")
        self.ButtonTest.setEnabled(True)
        self.ButtonTest.setGeometry(QRect(390, 370, 500, 80))
        self.ButtonTest.setMaximumSize(QSize(16777215, 16777215))
        self.ButtonTest.setFont(font)
        self.ButtonTest.setStyleSheet(u"QPushButton{\n"
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
        self.ButtonSpeedTest = QPushButton(self.centralwidget)
        self.ButtonSpeedTest.setObjectName(u"ButtonSpeedTest")
        self.ButtonSpeedTest.setEnabled(True)
        self.ButtonSpeedTest.setGeometry(QRect(390, 470, 500, 80))
        self.ButtonSpeedTest.setMaximumSize(QSize(16777215, 16777215))
        self.ButtonSpeedTest.setFont(font)
        self.ButtonSpeedTest.setStyleSheet(u"QPushButton{\n"
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
        self.ButtonProfile = QPushButton(self.centralwidget)
        self.ButtonProfile.setObjectName(u"ButtonProfile")
        self.ButtonProfile.setEnabled(True)
        self.ButtonProfile.setGeometry(QRect(1060, 20, 200, 100))
        self.ButtonProfile.setMaximumSize(QSize(16777215, 16777215))
        self.ButtonProfile.setFont(font)
        self.ButtonProfile.setStyleSheet(u"QPushButton{\n"
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
        self.ButtonStatisticsUsers = QPushButton(self.centralwidget)
        self.ButtonStatisticsUsers.setObjectName(u"ButtonStatisticsUsers")
        self.ButtonStatisticsUsers.setEnabled(True)
        self.ButtonStatisticsUsers.setGeometry(QRect(390, 170, 500, 80))
        self.ButtonStatisticsUsers.setMaximumSize(QSize(16777215, 16777215))
        self.ButtonStatisticsUsers.setFont(font)
        self.ButtonStatisticsUsers.setStyleSheet(u"QPushButton{\n"
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
        MainWindowAdmin.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindowAdmin)

        QMetaObject.connectSlotsByName(MainWindowAdmin)

    # setupUi

    def retranslateUi(self, MainWindowAdmin):
        MainWindowAdmin.setWindowTitle(QCoreApplication.translate("MainWindowAdmin", u"MainWindow", None))
        self.ButtonTheory.setText(QCoreApplication.translate("MainWindowAdmin",
                                                             u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0442\u0435\u043e\u0440\u0438\u044e",
                                                             None))
        self.ButtonTest.setText(QCoreApplication.translate("MainWindowAdmin",
                                                           u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0442\u0435\u0441\u0442",
                                                           None))
        self.ButtonSpeedTest.setText(QCoreApplication.translate("MainWindowAdmin",
                                                                u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u043d\u043e\u0439 \u0442\u0435\u0441\u0442",
                                                                None))
        self.ButtonProfile.setText(
            QCoreApplication.translate("MainWindowAdmin", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.ButtonStatisticsUsers.setText(QCoreApplication.translate("MainWindowAdmin",
                                                                      u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439",
                                                                      None))
    # retranslateUi
