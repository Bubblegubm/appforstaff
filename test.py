# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_Test(object):
    def setupUi(self, Test):
        if not Test.objectName():
            Test.setObjectName(u"Test")
        Test.resize(1280, 720)
        Test.setFocusPolicy(Qt.ClickFocus)
        Test.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.358, y1:0.266636, x2:1, y2:1, stop:0 rgba(163, 5, 255, 255), stop:1 rgba(92, 51, 255, 255))")
        self.centralwidget = QWidget(Test)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Question = QTextEdit(self.centralwidget)
        self.Question.setObjectName(u"Question")
        self.Question.setEnabled(True)
        self.Question.setGeometry(QRect(20, 20, 1240, 200))
        self.Question.setFocusPolicy(Qt.NoFocus)
        self.Question.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"font: 26pt \"Ambient(RUS BY LYAJKA)\";\n"
"background-color: rgba(0, 0, 0, 100);\n"
"padding-left: 10px;")
        self.ProgressBar = QProgressBar(self.centralwidget)
        self.ProgressBar.setObjectName(u"ProgressBar")
        self.ProgressBar.setGeometry(QRect(400, 625, 480, 50))
        self.ProgressBar.setStyleSheet(u"QProgressBar{\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"font: 16pt \"Ambient(RUS BY LYAJKA)\";\n"
"background-color: rgba(0, 0, 0, 100);\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.500318, x2:1, y2:0.506, stop:0 rgba(131, 27, 175, 255), stop:1 rgba(195, 42, 255, 255));\n"
"border-top-right-radius: 7px;\n"
"border-bottom-right-radius: 7px;\n"
"font: 16pt \"Ambient(RUS BY LYAJKA)\";\n"
"}")
        self.ProgressBar.setValue(70)
        self.ProgressBar.setAlignment(Qt.AlignCenter)
        self.ButtonBack = QPushButton(self.centralwidget)
        self.ButtonBack.setObjectName(u"ButtonBack")
        self.ButtonBack.setEnabled(True)
        self.ButtonBack.setGeometry(QRect(160, 610, 200, 80))
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
        self.ButtonForward = QPushButton(self.centralwidget)
        self.ButtonForward.setObjectName(u"ButtonForward")
        self.ButtonForward.setEnabled(True)
        self.ButtonForward.setGeometry(QRect(920, 610, 200, 80))
        self.ButtonForward.setMaximumSize(QSize(16777215, 16777215))
        self.ButtonForward.setFont(font)
        self.ButtonForward.setStyleSheet(u"QPushButton{\n"
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
        self.ButtonAnswer1 = QPushButton(self.centralwidget)
        self.ButtonAnswer1.setObjectName(u"ButtonAnswer1")
        self.ButtonAnswer1.setGeometry(QRect(20, 240, 1240, 100))
        self.ButtonAnswer1.setLayoutDirection(Qt.LeftToRight)
        self.ButtonAnswer1.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"font: 26pt \"Ambient(RUS BY LYAJKA)\";\n"
"background-color: rgba(0, 0, 0, 100);\n"
"width: 50px;\n"
"text-align: top, left;\n"
"padding-left: 10px;\n"
"padding-top: 5px;\n"
"}")
        self.ButtonAnswer2 = QPushButton(self.centralwidget)
        self.ButtonAnswer2.setObjectName(u"ButtonAnswer2")
        self.ButtonAnswer2.setGeometry(QRect(20, 360, 1240, 100))
        self.ButtonAnswer2.setLayoutDirection(Qt.LeftToRight)
        self.ButtonAnswer2.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"font: 26pt \"Ambient(RUS BY LYAJKA)\";\n"
"background-color: rgba(0, 0, 0, 100);\n"
"width: 50px;\n"
"text-align: top, left;\n"
"padding-left: 10px;\n"
"padding-top: 5px;\n"
"}")
        self.ButtonAnswer3 = QPushButton(self.centralwidget)
        self.ButtonAnswer3.setObjectName(u"ButtonAnswer3")
        self.ButtonAnswer3.setGeometry(QRect(20, 480, 1240, 100))
        self.ButtonAnswer3.setLayoutDirection(Qt.LeftToRight)
        self.ButtonAnswer3.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"font: 26pt \"Ambient(RUS BY LYAJKA)\";\n"
"background-color: rgba(0, 0, 0, 100);\n"
"width: 50px;\n"
"text-align: top, left;\n"
"padding-left: 10px;\n"
"padding-top: 5px;\n"
"}")
        Test.setCentralWidget(self.centralwidget)

        self.retranslateUi(Test)

        QMetaObject.connectSlotsByName(Test)
    # setupUi

    def retranslateUi(self, Test):
        Test.setWindowTitle(QCoreApplication.translate("Test", u"MainWindow", None))
        self.Question.setHtml(QCoreApplication.translate("Test", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ambient(RUS BY LYAJKA)'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 \u0441\u0442\u0440\u043e\u0447\u043a\u0430 \u0432\u043e\u043f\u0440\u043e\u0441\u0430</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 \u0441\u0442\u0440\u043e\u0447\u043a\u0430 \u0432\u043e\u043f\u0440\u043e\u0441\u0430</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3 \u0441\u0442\u0440\u043e\u0447\u043a\u0430 \u0432\u043e\u043f\u0440\u043e\u0441\u0430</p>\n"
"<p style=\" margin-top:0"
                        "px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4 \u0441\u0442\u0440\u043e\u0447\u043a\u0430 \u0432\u043e\u043f\u0440\u043e\u0441\u0430</p></body></html>", None))
        self.ButtonBack.setText(QCoreApplication.translate("Test", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.ButtonForward.setText(QCoreApplication.translate("Test", u"\u0412\u043f\u0435\u0440\u0451\u0434", None))
        self.ButtonAnswer1.setText(QCoreApplication.translate("Test", u"PushButton", None))
        self.ButtonAnswer2.setText(QCoreApplication.translate("Test", u"PushButton", None))
        self.ButtonAnswer3.setText(QCoreApplication.translate("Test", u"PushButton", None))
    # retranslateUi

