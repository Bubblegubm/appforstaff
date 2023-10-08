# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setFocusPolicy(Qt.ClickFocus)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.358, y1:0.266636, x2:1, y2:1, stop:0 rgba(163, 5, 255, 255), stop:1 rgba(92, 51, 255, 255))")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ButtonTheory = QPushButton(self.centralwidget)
        self.ButtonTheory.setObjectName(u"ButtonTheory")
        self.ButtonTheory.setEnabled(True)
        self.ButtonTheory.setGeometry(QRect(450, 235, 400, 70))
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
        self.ButtonTest.setGeometry(QRect(450, 325, 400, 70))
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
        self.ButtonSpeedTest.setGeometry(QRect(450, 415, 400, 70))
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ButtonTheory.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043e\u0440\u0438\u044f", None))
        self.ButtonTest.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0441\u0442", None))
        self.ButtonSpeedTest.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u043d\u043e\u0439 \u0442\u0435\u0441\u0442", None))
        self.ButtonProfile.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c", None))
    # retranslateUi

