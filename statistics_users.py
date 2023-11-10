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
                               QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)


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
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(False)
        self.tableWidget.setGeometry(QRect(20, 20, 1240, 580))
        font1 = QFont()
        font1.setFamilies([u"Ambient(RUS BY LYAJKA)"])
        font1.setPointSize(26)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setKerning(True)
        self.tableWidget.setFont(font1)
        self.tableWidget.setFocusPolicy(Qt.StrongFocus)
        self.tableWidget.setStyleSheet(u"color: rgba(255, 255, 255, 255);\n"
                                       "border: 3px solid rgb(255, 255, 255);\n"
                                       "font: 26pt \"Ambient(RUS BY LYAJKA)\";\n"
                                       "background-color: rgba(0, 0, 0, 100);\n"
                                       "alternate-background-color: rgb(170, 170, 127);\n"
                                       "header-color: rgba(0, 0, 0, 100);\n"
                                       "gridline-color: rgb(255, 255, 255);\n"
                                       "\n"
                                       "QTableWidget::horizontalHeader{\n"
                                       "color: rgba(255, 255, 255, 255);\n"
                                       "border: 3px solid rgb(255, 255, 255);\n"
                                       "font: 26pt \"Ambient(RUS BY LYAJKA)\";\n"
                                       "background-color: rgba(0, 0, 0, 100);\n"
                                       "alternate-background-color: rgb(170, 170, 127);\n"
                                       "}\n"
                                       "")
        self.tableWidget.setTextElideMode(Qt.ElideRight)
        StatisticsUsers.setCentralWidget(self.centralwidget)

        self.retranslateUi(StatisticsUsers)

        QMetaObject.connectSlotsByName(StatisticsUsers)

    # setupUi

    def retranslateUi(self, StatisticsUsers):
        StatisticsUsers.setWindowTitle(QCoreApplication.translate("StatisticsUsers", u"MainWindow", None))
        self.ButtonProfile.setText(
            QCoreApplication.translate("StatisticsUsers", u"\u041d\u0430\u0437\u0430\u0434", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("StatisticsUsers", u"\u041d\u043e\u043c\u0435\u0440", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("StatisticsUsers", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("StatisticsUsers", u"\u0418\u043c\u044f", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate("StatisticsUsers", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("StatisticsUsers", u"\u0422\u0435\u0441\u0442", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("StatisticsUsers",
                                                                u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u043d\u043e\u0439 \u0442\u0435\u0441\u0442",
                                                                None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(
            QCoreApplication.translate("StatisticsUsers", u"\u0412\u0440\u0435\u043c\u044f", None));
    # retranslateUi
