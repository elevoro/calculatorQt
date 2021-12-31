# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(338, 539)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.lineEdit)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.percent = QPushButton(self.centralwidget)
        self.percent.setObjectName(u"percent")
        self.percent.setMinimumSize(QSize(75, 65))
        font1 = QFont()
        font1.setPointSize(14)
        self.percent.setFont(font1)

        self.horizontalLayout_7.addWidget(self.percent)

        self.CE = QPushButton(self.centralwidget)
        self.CE.setObjectName(u"CE")
        self.CE.setMinimumSize(QSize(75, 65))
        self.CE.setFont(font1)

        self.horizontalLayout_7.addWidget(self.CE)

        self.C = QPushButton(self.centralwidget)
        self.C.setObjectName(u"C")
        self.C.setMinimumSize(QSize(75, 65))
        self.C.setFont(font1)

        self.horizontalLayout_7.addWidget(self.C)

        self.backspace = QPushButton(self.centralwidget)
        self.backspace.setObjectName(u"backspace")
        self.backspace.setMinimumSize(QSize(75, 65))
        self.backspace.setFont(font1)

        self.horizontalLayout_7.addWidget(self.backspace)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.oneDelX = QPushButton(self.centralwidget)
        self.oneDelX.setObjectName(u"oneDelX")
        self.oneDelX.setMinimumSize(QSize(75, 65))
        self.oneDelX.setFont(font1)

        self.horizontalLayout_6.addWidget(self.oneDelX)

        self.degree = QPushButton(self.centralwidget)
        self.degree.setObjectName(u"degree")
        self.degree.setMinimumSize(QSize(75, 65))
        self.degree.setFont(font1)

        self.horizontalLayout_6.addWidget(self.degree)

        self.square = QPushButton(self.centralwidget)
        self.square.setObjectName(u"square")
        self.square.setMinimumSize(QSize(75, 65))
        self.square.setFont(font1)

        self.horizontalLayout_6.addWidget(self.square)

        self.divide = QPushButton(self.centralwidget)
        self.divide.setObjectName(u"divide")
        self.divide.setMinimumSize(QSize(75, 65))
        self.divide.setFont(font1)

        self.horizontalLayout_6.addWidget(self.divide)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.seven = QPushButton(self.centralwidget)
        self.seven.setObjectName(u"seven")
        self.seven.setMinimumSize(QSize(75, 65))
        self.seven.setFont(font1)

        self.horizontalLayout_5.addWidget(self.seven)

        self.eight = QPushButton(self.centralwidget)
        self.eight.setObjectName(u"eight")
        self.eight.setMinimumSize(QSize(75, 65))
        self.eight.setFont(font1)

        self.horizontalLayout_5.addWidget(self.eight)

        self.nine = QPushButton(self.centralwidget)
        self.nine.setObjectName(u"nine")
        self.nine.setMinimumSize(QSize(75, 65))
        self.nine.setFont(font1)

        self.horizontalLayout_5.addWidget(self.nine)

        self.mult = QPushButton(self.centralwidget)
        self.mult.setObjectName(u"mult")
        self.mult.setMinimumSize(QSize(75, 65))
        self.mult.setFont(font1)

        self.horizontalLayout_5.addWidget(self.mult)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.four = QPushButton(self.centralwidget)
        self.four.setObjectName(u"four")
        self.four.setMinimumSize(QSize(75, 65))
        self.four.setFont(font1)

        self.horizontalLayout_4.addWidget(self.four)

        self.five = QPushButton(self.centralwidget)
        self.five.setObjectName(u"five")
        self.five.setMinimumSize(QSize(75, 65))
        self.five.setFont(font1)

        self.horizontalLayout_4.addWidget(self.five)

        self.six = QPushButton(self.centralwidget)
        self.six.setObjectName(u"six")
        self.six.setMinimumSize(QSize(75, 65))
        self.six.setFont(font1)

        self.horizontalLayout_4.addWidget(self.six)

        self.minus = QPushButton(self.centralwidget)
        self.minus.setObjectName(u"minus")
        self.minus.setMinimumSize(QSize(75, 65))
        self.minus.setFont(font1)

        self.horizontalLayout_4.addWidget(self.minus)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.one = QPushButton(self.centralwidget)
        self.one.setObjectName(u"one")
        self.one.setMinimumSize(QSize(75, 65))
        self.one.setFont(font1)

        self.horizontalLayout_3.addWidget(self.one)

        self.two = QPushButton(self.centralwidget)
        self.two.setObjectName(u"two")
        self.two.setMinimumSize(QSize(75, 65))
        self.two.setFont(font1)

        self.horizontalLayout_3.addWidget(self.two)

        self.three = QPushButton(self.centralwidget)
        self.three.setObjectName(u"three")
        self.three.setMinimumSize(QSize(75, 65))
        self.three.setFont(font1)

        self.horizontalLayout_3.addWidget(self.three)

        self.plus = QPushButton(self.centralwidget)
        self.plus.setObjectName(u"plus")
        self.plus.setMinimumSize(QSize(75, 65))
        self.plus.setFont(font1)

        self.horizontalLayout_3.addWidget(self.plus)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.plusAndMinus = QPushButton(self.centralwidget)
        self.plusAndMinus.setObjectName(u"plusAndMinus")
        self.plusAndMinus.setMinimumSize(QSize(75, 65))
        self.plusAndMinus.setFont(font1)

        self.horizontalLayout_2.addWidget(self.plusAndMinus)

        self.zero = QPushButton(self.centralwidget)
        self.zero.setObjectName(u"zero")
        self.zero.setMinimumSize(QSize(75, 65))
        self.zero.setFont(font1)

        self.horizontalLayout_2.addWidget(self.zero)

        self.point = QPushButton(self.centralwidget)
        self.point.setObjectName(u"point")
        self.point.setMinimumSize(QSize(75, 65))
        self.point.setFont(font1)

        self.horizontalLayout_2.addWidget(self.point)

        self.equal = QPushButton(self.centralwidget)
        self.equal.setObjectName(u"equal")
        self.equal.setMinimumSize(QSize(75, 65))
        self.equal.setFont(font1)

        self.horizontalLayout_2.addWidget(self.equal)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 338, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.percent.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.CE.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        self.C.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.backspace.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.oneDelX.setText(QCoreApplication.translate("MainWindow", u"1/x", None))
        self.degree.setText(QCoreApplication.translate("MainWindow", u"X^2", None))
        self.square.setText(QCoreApplication.translate("MainWindow", u"X^(1/2)", None))
        self.divide.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.seven.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.eight.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.nine.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.mult.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.four.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.five.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.six.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.one.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.two.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.three.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.plusAndMinus.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.zero.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.point.setText(QCoreApplication.translate("MainWindow", u",", None))
        self.equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
    # retranslateUi

