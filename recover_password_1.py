# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recover_password_1.ui'
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
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_RecoverPassword1(object):
    def setupUi(self, RecoverPassword1):
        if not RecoverPassword1.objectName():
            RecoverPassword1.setObjectName(u"RecoverPassword1")
        RecoverPassword1.resize(1280, 720)
        RecoverPassword1.setFocusPolicy(Qt.ClickFocus)
        RecoverPassword1.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.358, y1:0.266636, x2:1, y2:1, stop:0 rgba(163, 5, 255, 255), stop:1 rgba(92, 51, 255, 255))")
        self.centralwidget = QWidget(RecoverPassword1)
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
        self.ButtonFurther = QPushButton(self.centralwidget)
        self.ButtonFurther.setObjectName(u"ButtonFurther")
        self.ButtonFurther.setEnabled(True)
        self.ButtonFurther.setGeometry(QRect(440, 570, 400, 50))
        self.ButtonFurther.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Ambient(RUS BY LYAJKA)"])
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        self.ButtonFurther.setFont(font)
        self.ButtonFurther.setStyleSheet(u"QPushButton{\n"
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
        self.SecretWord = QLineEdit(self.centralwidget)
        self.SecretWord.setObjectName(u"SecretWord")
        self.SecretWord.setEnabled(True)
        self.SecretWord.setGeometry(QRect(440, 490, 400, 50))
        self.SecretWord.setMinimumSize(QSize(0, 0))
        self.SecretWord.setSizeIncrement(QSize(300, 40))
        self.SecretWord.setBaseSize(QSize(300, 40))
        self.SecretWord.setMouseTracking(True)
        self.SecretWord.setTabletTracking(False)
        self.SecretWord.setFocusPolicy(Qt.ClickFocus)
        self.SecretWord.setStyleSheet(u"QLineEdit{\n"
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
        self.SecretWord.setAlignment(Qt.AlignCenter)
        self.LabelRecoverPassword = QLabel(self.centralwidget)
        self.LabelRecoverPassword.setObjectName(u"LabelRecoverPassword")
        self.LabelRecoverPassword.setGeometry(QRect(315, 80, 650, 100))
        self.LabelRecoverPassword.setSizeIncrement(QSize(400, 100))
        self.LabelRecoverPassword.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 40pt \"Ambient(RUS BY LYAJKA)\";\n"
"background-color: rgba(255, 255, 255, 50);\n"
"border: 3px solid rgb(255, 255, 255);\n"
"border-radius: 30px;\n"
"\n"
"")
        self.LabelRecoverPassword.setAlignment(Qt.AlignCenter)
        self.ButtonBack = QPushButton(self.centralwidget)
        self.ButtonBack.setObjectName(u"ButtonBack")
        self.ButtonBack.setEnabled(True)
        self.ButtonBack.setGeometry(QRect(20, 620, 150, 80))
        self.ButtonBack.setMaximumSize(QSize(16777215, 16777215))
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
        self.Error = QTextEdit(self.centralwidget)
        self.Error.setObjectName(u"Error")
        self.Error.setGeometry(QRect(900, 320, 320, 110))
        self.Error.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"font: 26pt \"Ambient(RUS BY LYAJKA)\";\n"
"background-color: rgba(0, 0, 0, 100);\n"
"")
        RecoverPassword1.setCentralWidget(self.centralwidget)

        self.retranslateUi(RecoverPassword1)

        QMetaObject.connectSlotsByName(RecoverPassword1)
    # setupUi

    def retranslateUi(self, RecoverPassword1):
        RecoverPassword1.setWindowTitle(QCoreApplication.translate("RecoverPassword1", u"MainWindow", None))
        self.Surname.setText("")
        self.Surname.setPlaceholderText(QCoreApplication.translate("RecoverPassword1", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.ButtonFurther.setText(QCoreApplication.translate("RecoverPassword1", u"\u0414\u0430\u043b\u0435\u0435", None))
        self.Name.setText("")
        self.Name.setPlaceholderText(QCoreApplication.translate("RecoverPassword1", u"\u0418\u043c\u044f", None))
        self.Surname2.setText("")
        self.Surname2.setPlaceholderText(QCoreApplication.translate("RecoverPassword1", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.Login.setText("")
        self.Login.setPlaceholderText(QCoreApplication.translate("RecoverPassword1", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.SecretWord.setText("")
        self.SecretWord.setPlaceholderText(QCoreApplication.translate("RecoverPassword1", u"\u0421\u0435\u043a\u0440\u0435\u0442\u043d\u043e\u0435 \u0441\u043b\u043e\u0432\u043e", None))
        self.LabelRecoverPassword.setText(QCoreApplication.translate("RecoverPassword1", u"\u0412\u043e\u0441\u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435 \u043f\u0430\u0440\u043e\u043b\u044f", None))
        self.ButtonBack.setText(QCoreApplication.translate("RecoverPassword1", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.Error.setHtml(QCoreApplication.translate("RecoverPassword1", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ambient(RUS BY LYAJKA)'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0422\u0430\u043a\u0438\u0435 \u0434\u0430\u043d\u043d\u044b\u0435</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u043e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u044e\u0442</p></body></html>", None))
    # retranslateUi

