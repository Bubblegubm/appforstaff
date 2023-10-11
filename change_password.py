# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'change_password.ui'
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

class Ui_ChangePassword(object):
    def setupUi(self, ChangePassword):
        if not ChangePassword.objectName():
            ChangePassword.setObjectName(u"ChangePassword")
        ChangePassword.resize(1280, 720)
        ChangePassword.setFocusPolicy(Qt.ClickFocus)
        ChangePassword.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.358, y1:0.266636, x2:1, y2:1, stop:0 rgba(163, 5, 255, 255), stop:1 rgba(92, 51, 255, 255))")
        self.centralwidget = QWidget(ChangePassword)
        self.centralwidget.setObjectName(u"centralwidget")
        self.NewPassword = QLineEdit(self.centralwidget)
        self.NewPassword.setObjectName(u"NewPassword")
        self.NewPassword.setEnabled(True)
        self.NewPassword.setGeometry(QRect(440, 310, 400, 50))
        self.NewPassword.setMinimumSize(QSize(0, 0))
        self.NewPassword.setSizeIncrement(QSize(300, 40))
        self.NewPassword.setBaseSize(QSize(300, 40))
        self.NewPassword.setMouseTracking(True)
        self.NewPassword.setTabletTracking(False)
        self.NewPassword.setFocusPolicy(Qt.ClickFocus)
        self.NewPassword.setStyleSheet(u"QLineEdit{\n"
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
        self.NewPassword.setAlignment(Qt.AlignCenter)
        self.ButtonChangePassword = QPushButton(self.centralwidget)
        self.ButtonChangePassword.setObjectName(u"ButtonChangePassword")
        self.ButtonChangePassword.setEnabled(True)
        self.ButtonChangePassword.setGeometry(QRect(440, 570, 400, 50))
        self.ButtonChangePassword.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Ambient(RUS BY LYAJKA)"])
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
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
        self.LabelChangePassword = QLabel(self.centralwidget)
        self.LabelChangePassword.setObjectName(u"LabelChangePassword")
        self.LabelChangePassword.setGeometry(QRect(315, 80, 650, 100))
        self.LabelChangePassword.setSizeIncrement(QSize(400, 100))
        self.LabelChangePassword.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 40pt \"Ambient(RUS BY LYAJKA)\";\n"
"background-color: rgba(255, 255, 255, 50);\n"
"border: 3px solid rgb(255, 255, 255);\n"
"border-radius: 30px;\n"
"\n"
"")
        self.LabelChangePassword.setAlignment(Qt.AlignCenter)
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
        self.IconFailPassword = QLabel(self.centralwidget)
        self.IconFailPassword.setObjectName(u"IconFailPassword")
        self.IconFailPassword.setGeometry(QRect(860, 310, 50, 50))
        self.IconFailPassword.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"font: 26pt \"Ambient(RUS BY LYAJKA)\";\n"
"background-color: rgba(0, 0, 0, 100);")
        self.IconFailPassword.setAlignment(Qt.AlignCenter)
        ChangePassword.setCentralWidget(self.centralwidget)

        self.retranslateUi(ChangePassword)

        QMetaObject.connectSlotsByName(ChangePassword)
    # setupUi

    def retranslateUi(self, ChangePassword):
        ChangePassword.setWindowTitle(QCoreApplication.translate("ChangePassword", u"MainWindow", None))
        self.NewPassword.setText("")
        self.NewPassword.setPlaceholderText(QCoreApplication.translate("ChangePassword", u"\u041d\u043e\u0432\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.ButtonChangePassword.setText(QCoreApplication.translate("ChangePassword", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.LabelChangePassword.setText(QCoreApplication.translate("ChangePassword", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u043f\u0430\u0440\u043e\u043b\u044f", None))
        self.ButtonBack.setText(QCoreApplication.translate("ChangePassword", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.IconFailPassword.setText(QCoreApplication.translate("ChangePassword", u"!", None))
    # retranslateUi

