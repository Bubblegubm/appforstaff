# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'statistics_users.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QPushButton,
                               QSizePolicy, QTableView, QWidget)


class Ui_StatisticsUsers(object):
    def setupUi(self, StatisticsUsers):
        if not StatisticsUsers.objectName():
            StatisticsUsers.setObjectName(u"StatisticsUsers")
        StatisticsUsers.resize(1280, 720)
        StatisticsUsers.setFocusPolicy(Qt.StrongFocus)
        StatisticsUsers.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0.358, y1:0.266636, x2:1, y2:1, stop:0\n"
            "                rgba(163, 5, 255, 255), stop:1 rgba(92, 51, 255, 255))\n"
            "            ")
        self.centralwidget = QWidget(StatisticsUsers)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ButtonProfile = QPushButton(self.centralwidget)
        self.ButtonProfile.setObjectName(u"ButtonProfile")
        self.ButtonProfile.setEnabled(True)
        self.ButtonProfile.setGeometry(QRect(20, 620, 180, 80))
        self.ButtonProfile.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Ambient(RUS BY LYAJKA)"])
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        self.ButtonProfile.setFont(font)
        self.ButtonProfile.setStyleSheet(u"QPushButton{\n"
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
        self.tableWidget = QTableView(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 20, 1240, 580))
        self.tableWidget.setStyleSheet(u"QTableView{\n"
                                       "color: white;\n"
                                       "border: 3px solid rgb(255, 255, 255);\n"
                                       "background-color: rgba(255, 255, 255, 50);\n"
                                       "font: 26pt \"Ambient(RUS BY LYAJKA)\";\n"
                                       "}\n"
                                       "QHeaderView::section{\n"
                                       "color: white;\n"
                                       "background-color: rgba(0, 0, 0, 100);\n"
                                       "alternate-background-color: rgba(0, 0, 0, 0);\n"
                                       "border: 3px solid rgb(255, 255, 255);\n"
                                       "height: 50px;\n"
                                       "width: 50 px;\n"
                                       "font: 26pt \"Ambient(RUS BY LYAJKA)\";\n"
                                       "}\n"
                                       "QTableWidget::item{\n"
                                       "background-color: rgba(0, 0, 0, 100);\n"
                                       "border: border: 3px solid rgb(255, 255, 255);\n"
                                       "font: 26pt \"Ambient(RUS BY LYAJKA)\";\n"
                                       "}\n"
                                       "")
        StatisticsUsers.setCentralWidget(self.centralwidget)

        self.retranslateUi(StatisticsUsers)

        QMetaObject.connectSlotsByName(StatisticsUsers)

    # setupUi

    def retranslateUi(self, StatisticsUsers):
        StatisticsUsers.setWindowTitle(QCoreApplication.translate("StatisticsUsers", u"MainWindow", None))
        self.ButtonProfile.setText(
            QCoreApplication.translate("StatisticsUsers", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi
