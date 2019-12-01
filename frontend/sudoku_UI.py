# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sudoku.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(555, 525)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.usernameLabel = QtWidgets.QLabel(self.page)
        self.usernameLabel.setGeometry(QtCore.QRect(100, 80, 141, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usernameLabel.sizePolicy().hasHeightForWidth())
        self.usernameLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName("usernameLabel")
        self.usernameLine = QtWidgets.QLineEdit(self.page)
        self.usernameLine.setGeometry(QtCore.QRect(250, 90, 171, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usernameLine.sizePolicy().hasHeightForWidth())
        self.usernameLine.setSizePolicy(sizePolicy)
        self.usernameLine.setObjectName("usernameLine")
        self.signUpButton = QtWidgets.QPushButton(self.page)
        self.signUpButton.setGeometry(QtCore.QRect(330, 250, 89, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signUpButton.sizePolicy().hasHeightForWidth())
        self.signUpButton.setSizePolicy(sizePolicy)
        self.signUpButton.setObjectName("signUpButton")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(340, 220, 67, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(200, 10, 161, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.passwordLabel = QtWidgets.QLabel(self.page)
        self.passwordLabel.setGeometry(QtCore.QRect(100, 120, 131, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordLabel.sizePolicy().hasHeightForWidth())
        self.passwordLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")
        self.signInButton = QtWidgets.QPushButton(self.page)
        self.signInButton.setGeometry(QtCore.QRect(330, 180, 89, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signInButton.sizePolicy().hasHeightForWidth())
        self.signInButton.setSizePolicy(sizePolicy)
        self.signInButton.setObjectName("signInButton")
        self.passwordLine = QtWidgets.QLineEdit(self.page)
        self.passwordLine.setGeometry(QtCore.QRect(250, 130, 171, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordLine.sizePolicy().hasHeightForWidth())
        self.passwordLine.setSizePolicy(sizePolicy)
        self.passwordLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLine.setObjectName("passwordLine")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(170, 10, 251, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.usernameLineRegistration = QtWidgets.QLineEdit(self.page_2)
        self.usernameLineRegistration.setGeometry(QtCore.QRect(290, 100, 171, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usernameLineRegistration.sizePolicy().hasHeightForWidth())
        self.usernameLineRegistration.setSizePolicy(sizePolicy)
        self.usernameLineRegistration.setObjectName("usernameLineRegistration")
        self.passwordLabel_2 = QtWidgets.QLabel(self.page_2)
        self.passwordLabel_2.setGeometry(QtCore.QRect(120, 130, 131, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordLabel_2.sizePolicy().hasHeightForWidth())
        self.passwordLabel_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.passwordLabel_2.setFont(font)
        self.passwordLabel_2.setObjectName("passwordLabel_2")
        self.usernameLabel_2 = QtWidgets.QLabel(self.page_2)
        self.usernameLabel_2.setGeometry(QtCore.QRect(120, 90, 141, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usernameLabel_2.sizePolicy().hasHeightForWidth())
        self.usernameLabel_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.usernameLabel_2.setFont(font)
        self.usernameLabel_2.setObjectName("usernameLabel_2")
        self.passwordLineRegistration = QtWidgets.QLineEdit(self.page_2)
        self.passwordLineRegistration.setGeometry(QtCore.QRect(290, 140, 171, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordLineRegistration.sizePolicy().hasHeightForWidth())
        self.passwordLineRegistration.setSizePolicy(sizePolicy)
        self.passwordLineRegistration.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineRegistration.setObjectName("passwordLineRegistration")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(30, 180, 231, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.repeatPasswordLine = QtWidgets.QLineEdit(self.page_2)
        self.repeatPasswordLine.setGeometry(QtCore.QRect(290, 190, 171, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.repeatPasswordLine.sizePolicy().hasHeightForWidth())
        self.repeatPasswordLine.setSizePolicy(sizePolicy)
        self.repeatPasswordLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.repeatPasswordLine.setObjectName("repeatPasswordLine")
        self.registrationButton = QtWidgets.QPushButton(self.page_2)
        self.registrationButton.setGeometry(QtCore.QRect(290, 240, 89, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registrationButton.sizePolicy().hasHeightForWidth())
        self.registrationButton.setSizePolicy(sizePolicy)
        self.registrationButton.setObjectName("registrationButton")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.page_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 130, 411, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.challengeButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.challengeButton.sizePolicy().hasHeightForWidth())
        self.challengeButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.challengeButton.setFont(font)
        self.challengeButton.setObjectName("challengeButton")
        self.verticalLayout.addWidget(self.challengeButton)
        self.collaborativeButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.collaborativeButton.sizePolicy().hasHeightForWidth())
        self.collaborativeButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.collaborativeButton.setFont(font)
        self.collaborativeButton.setObjectName("collaborativeButton")
        self.verticalLayout.addWidget(self.collaborativeButton)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.page_4)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(60, 130, 431, 221))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.easyButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.easyButton.sizePolicy().hasHeightForWidth())
        self.easyButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.easyButton.setFont(font)
        self.easyButton.setObjectName("easyButton")
        self.verticalLayout_2.addWidget(self.easyButton)
        self.mediumButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mediumButton.sizePolicy().hasHeightForWidth())
        self.mediumButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.mediumButton.setFont(font)
        self.mediumButton.setObjectName("mediumButton")
        self.verticalLayout_2.addWidget(self.mediumButton)
        self.hardButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hardButton.sizePolicy().hasHeightForWidth())
        self.hardButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.hardButton.setFont(font)
        self.hardButton.setObjectName("hardButton")
        self.verticalLayout_2.addWidget(self.hardButton)
        self.stackedWidget.addWidget(self.page_4)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.stackedWidget.addWidget(self.page_6)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.page_5)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout00 = QtWidgets.QGridLayout()
        self.gridLayout00.setSpacing(0)
        self.gridLayout00.setObjectName("gridLayout00")
        self.toolButton_7 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_7.sizePolicy().hasHeightForWidth())
        self.toolButton_7.setSizePolicy(sizePolicy)
        self.toolButton_7.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-left: 4px solid #8b8f8b;    \n"
"    border-bottom: 2px solid #8b8f8b;    \n"
"}")
        self.toolButton_7.setText("")
        self.toolButton_7.setObjectName("toolButton_7")
        self.gridLayout00.addWidget(self.toolButton_7, 2, 0, 1, 1)
        self.toolButton_8 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_8.sizePolicy().hasHeightForWidth())
        self.toolButton_8.setSizePolicy(sizePolicy)
        self.toolButton_8.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-bottom: 2px solid #8b8f8b;    \n"
"}")
        self.toolButton_8.setText("")
        self.toolButton_8.setObjectName("toolButton_8")
        self.gridLayout00.addWidget(self.toolButton_8, 2, 1, 1, 1)
        self.toolButton_5 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_5.sizePolicy().hasHeightForWidth())
        self.toolButton_5.setSizePolicy(sizePolicy)
        self.toolButton_5.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"}")
        self.toolButton_5.setText("")
        self.toolButton_5.setObjectName("toolButton_5")
        self.gridLayout00.addWidget(self.toolButton_5, 1, 1, 1, 1)
        self.toolButton_9 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_9.sizePolicy().hasHeightForWidth())
        self.toolButton_9.setSizePolicy(sizePolicy)
        self.toolButton_9.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-right: 2px solid #8b8f8b;    \n"
"    border-bottom: 2px solid #8b8f8b;    \n"
"}")
        self.toolButton_9.setText("")
        self.toolButton_9.setObjectName("toolButton_9")
        self.gridLayout00.addWidget(self.toolButton_9, 2, 2, 1, 1)
        self.toolButton_1 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_1.sizePolicy().hasHeightForWidth())
        self.toolButton_1.setSizePolicy(sizePolicy)
        self.toolButton_1.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-top: 4px solid #8b8f8b;\n"
"    border-left: 4px solid #8b8f8b;    \n"
"}")
        self.toolButton_1.setText("")
        self.toolButton_1.setProperty("row", 1)
        self.toolButton_1.setProperty("col", 3)
        self.toolButton_1.setObjectName("toolButton_1")
        self.gridLayout00.addWidget(self.toolButton_1, 0, 0, 1, 1)
        self.toolButton_6 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_6.sizePolicy().hasHeightForWidth())
        self.toolButton_6.setSizePolicy(sizePolicy)
        self.toolButton_6.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-right: 2px solid #8b8f8b;    \n"
"}")
        self.toolButton_6.setText("")
        self.toolButton_6.setObjectName("toolButton_6")
        self.gridLayout00.addWidget(self.toolButton_6, 1, 2, 1, 1)
        self.toolButton_4 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_4.sizePolicy().hasHeightForWidth())
        self.toolButton_4.setSizePolicy(sizePolicy)
        self.toolButton_4.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-right: 2px solid #8b8f8b;    \n"
"    border-top: 4px solid #8b8f8b;    \n"
"}")
        self.toolButton_4.setText("")
        self.toolButton_4.setObjectName("toolButton_4")
        self.gridLayout00.addWidget(self.toolButton_4, 0, 2, 1, 1)
        self.toolButton_2 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_2.sizePolicy().hasHeightForWidth())
        self.toolButton_2.setSizePolicy(sizePolicy)
        self.toolButton_2.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-left: 4px solid #8b8f8b;    \n"
"}")
        self.toolButton_2.setText("")
        self.toolButton_2.setProperty("col", 1)
        self.toolButton_2.setProperty("row", 2)
        self.toolButton_2.setObjectName("toolButton_2")
        self.gridLayout00.addWidget(self.toolButton_2, 1, 0, 1, 1)
        self.toolButton_3 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_3.sizePolicy().hasHeightForWidth())
        self.toolButton_3.setSizePolicy(sizePolicy)
        self.toolButton_3.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-top: 4px solid #8b8f8b;\n"
"}")
        self.toolButton_3.setText("")
        self.toolButton_3.setObjectName("toolButton_3")
        self.gridLayout00.addWidget(self.toolButton_3, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout00, 0, 1, 1, 1)
        self.gridLayout21 = QtWidgets.QGridLayout()
        self.gridLayout21.setSpacing(0)
        self.gridLayout21.setObjectName("gridLayout21")
        self.toolButton_67 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_67.sizePolicy().hasHeightForWidth())
        self.toolButton_67.setSizePolicy(sizePolicy)
        self.toolButton_67.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-left: 2px solid #8b8f8b;    \n"
"}")
        self.toolButton_67.setText("")
        self.toolButton_67.setObjectName("toolButton_67")
        self.gridLayout21.addWidget(self.toolButton_67, 1, 0, 1, 1)
        self.toolButton_69 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_69.sizePolicy().hasHeightForWidth())
        self.toolButton_69.setSizePolicy(sizePolicy)
        self.toolButton_69.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-right: 2px solid #8b8f8b;    \n"
"}")
        self.toolButton_69.setText("")
        self.toolButton_69.setObjectName("toolButton_69")
        self.gridLayout21.addWidget(self.toolButton_69, 1, 2, 1, 1)
        self.toolButton_70 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_70.sizePolicy().hasHeightForWidth())
        self.toolButton_70.setSizePolicy(sizePolicy)
        self.toolButton_70.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-left: 2px solid #8b8f8b;    \n"
"    border-bottom: 4px solid #8b8f8b;    \n"
"}")
        self.toolButton_70.setText("")
        self.toolButton_70.setObjectName("toolButton_70")
        self.gridLayout21.addWidget(self.toolButton_70, 2, 0, 1, 1)
        self.toolButton_65 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_65.sizePolicy().hasHeightForWidth())
        self.toolButton_65.setSizePolicy(sizePolicy)
        self.toolButton_65.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-top: 2px solid #8b8f8b;    \n"
"}\n"
"\n"
"")
        self.toolButton_65.setText("")
        self.toolButton_65.setObjectName("toolButton_65")
        self.gridLayout21.addWidget(self.toolButton_65, 0, 1, 1, 1)
        self.toolButton_66 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_66.sizePolicy().hasHeightForWidth())
        self.toolButton_66.setSizePolicy(sizePolicy)
        self.toolButton_66.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-right: 2px solid #8b8f8b;    \n"
"    border-top: 2px solid #8b8f8b;    \n"
"}")
        self.toolButton_66.setText("")
        self.toolButton_66.setObjectName("toolButton_66")
        self.gridLayout21.addWidget(self.toolButton_66, 0, 2, 1, 1)
        self.toolButton_68 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_68.sizePolicy().hasHeightForWidth())
        self.toolButton_68.setSizePolicy(sizePolicy)
        self.toolButton_68.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"}")
        self.toolButton_68.setText("")
        self.toolButton_68.setObjectName("toolButton_68")
        self.gridLayout21.addWidget(self.toolButton_68, 1, 1, 1, 1)
        self.toolButton_71 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_71.sizePolicy().hasHeightForWidth())
        self.toolButton_71.setSizePolicy(sizePolicy)
        self.toolButton_71.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-bottom: 4px solid #8b8f8b;    \n"
"}")
        self.toolButton_71.setText("")
        self.toolButton_71.setObjectName("toolButton_71")
        self.gridLayout21.addWidget(self.toolButton_71, 2, 1, 1, 1)
        self.toolButton_64 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_64.sizePolicy().hasHeightForWidth())
        self.toolButton_64.setSizePolicy(sizePolicy)
        self.toolButton_64.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-left: 2px solid #8b8f8b;    \n"
"    border-top: 2px solid #8b8f8b;    \n"
"}")
        self.toolButton_64.setText("")
        self.toolButton_64.setObjectName("toolButton_64")
        self.gridLayout21.addWidget(self.toolButton_64, 0, 0, 1, 1)
        self.toolButton_72 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_72.sizePolicy().hasHeightForWidth())
        self.toolButton_72.setSizePolicy(sizePolicy)
        self.toolButton_72.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-right: 2px solid #8b8f8b;    \n"
"    border-bottom: 4px solid #8b8f8b;    \n"
"}")
        self.toolButton_72.setText("")
        self.toolButton_72.setObjectName("toolButton_72")
        self.gridLayout21.addWidget(self.toolButton_72, 2, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout21, 2, 2, 1, 1)
        self.gridLayout10 = QtWidgets.QGridLayout()
        self.gridLayout10.setSpacing(0)
        self.gridLayout10.setObjectName("gridLayout10")
        self.toolButton_30 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_30.sizePolicy().hasHeightForWidth())
        self.toolButton_30.setSizePolicy(sizePolicy)
        self.toolButton_30.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-top: 2px solid #8b8f8b;    \n"
"}\n"
"\n"
"")
        self.toolButton_30.setText("")
        self.toolButton_30.setObjectName("toolButton_30")
        self.gridLayout10.addWidget(self.toolButton_30, 0, 1, 1, 1)
        self.toolButton_28 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_28.sizePolicy().hasHeightForWidth())
        self.toolButton_28.setSizePolicy(sizePolicy)
        self.toolButton_28.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-left: 4px solid #8b8f8b;    \n"
"    border-top: 2px solid #8b8f8b;    \n"
"}")
        self.toolButton_28.setText("")
        self.toolButton_28.setObjectName("toolButton_28")
        self.gridLayout10.addWidget(self.toolButton_28, 0, 0, 1, 1)
        self.toolButton_29 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_29.sizePolicy().hasHeightForWidth())
        self.toolButton_29.setSizePolicy(sizePolicy)
        self.toolButton_29.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-right: 2px solid #8b8f8b;    \n"
"    border-top: 2px solid #8b8f8b;    \n"
"}")
        self.toolButton_29.setText("")
        self.toolButton_29.setObjectName("toolButton_29")
        self.gridLayout10.addWidget(self.toolButton_29, 0, 2, 1, 1)
        self.toolButton_32 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_32.sizePolicy().hasHeightForWidth())
        self.toolButton_32.setSizePolicy(sizePolicy)
        self.toolButton_32.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"}")
        self.toolButton_32.setText("")
        self.toolButton_32.setObjectName("toolButton_32")
        self.gridLayout10.addWidget(self.toolButton_32, 1, 1, 1, 1)
        self.toolButton_31 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_31.sizePolicy().hasHeightForWidth())
        self.toolButton_31.setSizePolicy(sizePolicy)
        self.toolButton_31.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-left: 4px solid #8b8f8b;    \n"
"}")
        self.toolButton_31.setText("")
        self.toolButton_31.setObjectName("toolButton_31")
        self.gridLayout10.addWidget(self.toolButton_31, 1, 0, 1, 1)
        self.toolButton_33 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_33.sizePolicy().hasHeightForWidth())
        self.toolButton_33.setSizePolicy(sizePolicy)
        self.toolButton_33.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-right: 2px solid #8b8f8b;    \n"
"}")
        self.toolButton_33.setText("")
        self.toolButton_33.setObjectName("toolButton_33")
        self.gridLayout10.addWidget(self.toolButton_33, 1, 2, 1, 1)
        self.toolButton_34 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_34.sizePolicy().hasHeightForWidth())
        self.toolButton_34.setSizePolicy(sizePolicy)
        self.toolButton_34.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-left: 4px solid #8b8f8b;    \n"
"    border-bottom: 2px solid #8b8f8b;    \n"
"}")
        self.toolButton_34.setText("")
        self.toolButton_34.setObjectName("toolButton_34")
        self.gridLayout10.addWidget(self.toolButton_34, 2, 0, 1, 1)
        self.toolButton_35 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_35.sizePolicy().hasHeightForWidth())
        self.toolButton_35.setSizePolicy(sizePolicy)
        self.toolButton_35.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-bottom: 2px solid #8b8f8b;    \n"
"}")
        self.toolButton_35.setText("")
        self.toolButton_35.setObjectName("toolButton_35")
        self.gridLayout10.addWidget(self.toolButton_35, 2, 1, 1, 1)
        self.toolButton_36 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_36.sizePolicy().hasHeightForWidth())
        self.toolButton_36.setSizePolicy(sizePolicy)
        self.toolButton_36.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-right: 2px solid #8b8f8b;    \n"
"    border-bottom: 2px solid #8b8f8b;    \n"
"}")
        self.toolButton_36.setText("")
        self.toolButton_36.setObjectName("toolButton_36")
        self.gridLayout10.addWidget(self.toolButton_36, 2, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout10, 1, 1, 1, 1)
        self.gridLayout12 = QtWidgets.QGridLayout()
        self.gridLayout12.setSpacing(0)
        self.gridLayout12.setObjectName("gridLayout12")
        self.toolButton_47 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_47.sizePolicy().hasHeightForWidth())
        self.toolButton_47.setSizePolicy(sizePolicy)
        self.toolButton_47.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-left: 2px solid #8b8f8b;    \n"
"}")
        self.toolButton_47.setText("")
        self.toolButton_47.setObjectName("toolButton_47")
        self.gridLayout12.addWidget(self.toolButton_47, 1, 0, 1, 1)
        self.toolButton_49 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_49.sizePolicy().hasHeightForWidth())
        self.toolButton_49.setSizePolicy(sizePolicy)
        self.toolButton_49.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-top: 2px solid #8b8f8b;    \n"
"}\n"
"\n"
"")
        self.toolButton_49.setText("")
        self.toolButton_49.setObjectName("toolButton_49")
        self.gridLayout12.addWidget(self.toolButton_49, 0, 1, 1, 1)
        self.toolButton_46 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_46.sizePolicy().hasHeightForWidth())
        self.toolButton_46.setSizePolicy(sizePolicy)
        self.toolButton_46.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-left: 2px solid #8b8f8b;    \n"
"    border-top: 2px solid #8b8f8b;    \n"
"}")
        self.toolButton_46.setText("")
        self.toolButton_46.setObjectName("toolButton_46")
        self.gridLayout12.addWidget(self.toolButton_46, 0, 0, 1, 1)
        self.toolButton_50 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_50.sizePolicy().hasHeightForWidth())
        self.toolButton_50.setSizePolicy(sizePolicy)
        self.toolButton_50.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"}")
        self.toolButton_50.setText("")
        self.toolButton_50.setObjectName("toolButton_50")
        self.gridLayout12.addWidget(self.toolButton_50, 1, 1, 1, 1)
        self.toolButton_48 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_48.sizePolicy().hasHeightForWidth())
        self.toolButton_48.setSizePolicy(sizePolicy)
        self.toolButton_48.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-left: 2px solid #8b8f8b;    \n"
"    border-bottom: 2px solid #8b8f8b;    \n"
"}")
        self.toolButton_48.setText("")
        self.toolButton_48.setObjectName("toolButton_48")
        self.gridLayout12.addWidget(self.toolButton_48, 2, 0, 1, 1)
        self.toolButton_51 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_51.sizePolicy().hasHeightForWidth())
        self.toolButton_51.setSizePolicy(sizePolicy)
        self.toolButton_51.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-bottom: 2px solid #8b8f8b;    \n"
"}")
        self.toolButton_51.setText("")
        self.toolButton_51.setObjectName("toolButton_51")
        self.gridLayout12.addWidget(self.toolButton_51, 2, 1, 1, 1)
        self.toolButton_52 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_52.sizePolicy().hasHeightForWidth())
        self.toolButton_52.setSizePolicy(sizePolicy)
        self.toolButton_52.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-right: 4px solid #8b8f8b;    \n"
"    border-top: 2px solid #8b8f8b;    \n"
"}")
        self.toolButton_52.setText("")
        self.toolButton_52.setObjectName("toolButton_52")
        self.gridLayout12.addWidget(self.toolButton_52, 0, 2, 1, 1)
        self.toolButton_53 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_53.sizePolicy().hasHeightForWidth())
        self.toolButton_53.setSizePolicy(sizePolicy)
        self.toolButton_53.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-right: 4px solid #8b8f8b;    \n"
"}")
        self.toolButton_53.setText("")
        self.toolButton_53.setObjectName("toolButton_53")
        self.gridLayout12.addWidget(self.toolButton_53, 1, 2, 1, 1)
        self.toolButton_54 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_54.sizePolicy().hasHeightForWidth())
        self.toolButton_54.setSizePolicy(sizePolicy)
        self.toolButton_54.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-right: 4px solid #8b8f8b;    \n"
"    border-bottom: 2px solid #8b8f8b;    \n"
"}")
        self.toolButton_54.setText("")
        self.toolButton_54.setObjectName("toolButton_54")
        self.gridLayout12.addWidget(self.toolButton_54, 2, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout12, 1, 3, 1, 1)
        self.gridLayout20 = QtWidgets.QGridLayout()
        self.gridLayout20.setSpacing(0)
        self.gridLayout20.setObjectName("gridLayout20")
        self.toolButton_57 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_57.sizePolicy().hasHeightForWidth())
        self.toolButton_57.setSizePolicy(sizePolicy)
        self.toolButton_57.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-right: 2px solid #8b8f8b;    \n"
"    border-top: 2px solid #8b8f8b;    \n"
"}")
        self.toolButton_57.setText("")
        self.toolButton_57.setObjectName("toolButton_57")
        self.gridLayout20.addWidget(self.toolButton_57, 0, 2, 1, 1)
        self.toolButton_58 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_58.sizePolicy().hasHeightForWidth())
        self.toolButton_58.setSizePolicy(sizePolicy)
        self.toolButton_58.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-left: 4px solid #8b8f8b;    \n"
"}")
        self.toolButton_58.setText("")
        self.toolButton_58.setObjectName("toolButton_58")
        self.gridLayout20.addWidget(self.toolButton_58, 1, 0, 1, 1)
        self.toolButton_59 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_59.sizePolicy().hasHeightForWidth())
        self.toolButton_59.setSizePolicy(sizePolicy)
        self.toolButton_59.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"}")
        self.toolButton_59.setText("")
        self.toolButton_59.setObjectName("toolButton_59")
        self.gridLayout20.addWidget(self.toolButton_59, 1, 1, 1, 1)
        self.toolButton_55 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_55.sizePolicy().hasHeightForWidth())
        self.toolButton_55.setSizePolicy(sizePolicy)
        self.toolButton_55.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-left: 4px solid #8b8f8b;    \n"
"    border-top: 2px solid #8b8f8b;    \n"
"}")
        self.toolButton_55.setText("")
        self.toolButton_55.setObjectName("toolButton_55")
        self.gridLayout20.addWidget(self.toolButton_55, 0, 0, 1, 1)
        self.toolButton_60 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_60.sizePolicy().hasHeightForWidth())
        self.toolButton_60.setSizePolicy(sizePolicy)
        self.toolButton_60.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-right: 2px solid #8b8f8b;    \n"
"}")
        self.toolButton_60.setText("")
        self.toolButton_60.setObjectName("toolButton_60")
        self.gridLayout20.addWidget(self.toolButton_60, 1, 2, 1, 1)
        self.toolButton_56 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_56.sizePolicy().hasHeightForWidth())
        self.toolButton_56.setSizePolicy(sizePolicy)
        self.toolButton_56.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-top: 2px solid #8b8f8b;    \n"
"}\n"
"\n"
"")
        self.toolButton_56.setText("")
        self.toolButton_56.setObjectName("toolButton_56")
        self.gridLayout20.addWidget(self.toolButton_56, 0, 1, 1, 1)
        self.toolButton_61 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_61.sizePolicy().hasHeightForWidth())
        self.toolButton_61.setSizePolicy(sizePolicy)
        self.toolButton_61.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-left: 4px solid #8b8f8b;    \n"
"    border-bottom: 4px solid #8b8f8b;    \n"
"}")
        self.toolButton_61.setText("")
        self.toolButton_61.setObjectName("toolButton_61")
        self.gridLayout20.addWidget(self.toolButton_61, 2, 0, 1, 1)
        self.toolButton_62 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_62.sizePolicy().hasHeightForWidth())
        self.toolButton_62.setSizePolicy(sizePolicy)
        self.toolButton_62.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-bottom: 4px solid #8b8f8b;    \n"
"}")
        self.toolButton_62.setText("")
        self.toolButton_62.setObjectName("toolButton_62")
        self.gridLayout20.addWidget(self.toolButton_62, 2, 1, 1, 1)
        self.toolButton_63 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_63.sizePolicy().hasHeightForWidth())
        self.toolButton_63.setSizePolicy(sizePolicy)
        self.toolButton_63.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-right: 2px solid #8b8f8b;    \n"
"    border-bottom: 4px solid #8b8f8b;    \n"
"}")
        self.toolButton_63.setText("")
        self.toolButton_63.setObjectName("toolButton_63")
        self.gridLayout20.addWidget(self.toolButton_63, 2, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout20, 2, 1, 1, 1)
        self.gridLayout22 = QtWidgets.QGridLayout()
        self.gridLayout22.setSpacing(0)
        self.gridLayout22.setObjectName("gridLayout22")
        self.toolButton_80 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_80.sizePolicy().hasHeightForWidth())
        self.toolButton_80.setSizePolicy(sizePolicy)
        self.toolButton_80.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-bottom: 4px solid #8b8f8b;    \n"
"}")
        self.toolButton_80.setText("")
        self.toolButton_80.setObjectName("toolButton_80")
        self.gridLayout22.addWidget(self.toolButton_80, 2, 1, 1, 1)
        self.toolButton_81 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_81.sizePolicy().hasHeightForWidth())
        self.toolButton_81.setSizePolicy(sizePolicy)
        self.toolButton_81.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-bottom: 4px solid #8b8f8b;    \n"
"    border-right: 4px solid #8b8f8b;    \n"
"}")
        self.toolButton_81.setText("")
        self.toolButton_81.setObjectName("toolButton_81")
        self.gridLayout22.addWidget(self.toolButton_81, 2, 2, 1, 1)
        self.toolButton_78 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_78.sizePolicy().hasHeightForWidth())
        self.toolButton_78.setSizePolicy(sizePolicy)
        self.toolButton_78.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-right: 4px solid #8b8f8b;    \n"
"}")
        self.toolButton_78.setText("")
        self.toolButton_78.setObjectName("toolButton_78")
        self.gridLayout22.addWidget(self.toolButton_78, 1, 2, 1, 1)
        self.toolButton_79 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_79.sizePolicy().hasHeightForWidth())
        self.toolButton_79.setSizePolicy(sizePolicy)
        self.toolButton_79.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-left: 2px solid #8b8f8b;    \n"
"    border-bottom: 4px solid #8b8f8b;    \n"
"}")
        self.toolButton_79.setText("")
        self.toolButton_79.setObjectName("toolButton_79")
        self.gridLayout22.addWidget(self.toolButton_79, 2, 0, 1, 1)
        self.toolButton_73 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_73.sizePolicy().hasHeightForWidth())
        self.toolButton_73.setSizePolicy(sizePolicy)
        self.toolButton_73.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-left: 2px solid #8b8f8b;    \n"
"    border-top: 2px solid #8b8f8b;    \n"
"}")
        self.toolButton_73.setText("")
        self.toolButton_73.setObjectName("toolButton_73")
        self.gridLayout22.addWidget(self.toolButton_73, 0, 0, 1, 1)
        self.toolButton_75 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_75.sizePolicy().hasHeightForWidth())
        self.toolButton_75.setSizePolicy(sizePolicy)
        self.toolButton_75.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-right: 4px solid #8b8f8b;    \n"
"    border-top: 2px solid #8b8f8b;    \n"
"}")
        self.toolButton_75.setText("")
        self.toolButton_75.setObjectName("toolButton_75")
        self.gridLayout22.addWidget(self.toolButton_75, 0, 2, 1, 1)
        self.toolButton_74 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_74.sizePolicy().hasHeightForWidth())
        self.toolButton_74.setSizePolicy(sizePolicy)
        self.toolButton_74.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-top: 2px solid #8b8f8b;    \n"
"}\n"
"\n"
"")
        self.toolButton_74.setText("")
        self.toolButton_74.setObjectName("toolButton_74")
        self.gridLayout22.addWidget(self.toolButton_74, 0, 1, 1, 1)
        self.toolButton_77 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_77.sizePolicy().hasHeightForWidth())
        self.toolButton_77.setSizePolicy(sizePolicy)
        self.toolButton_77.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"}")
        self.toolButton_77.setText("")
        self.toolButton_77.setObjectName("toolButton_77")
        self.gridLayout22.addWidget(self.toolButton_77, 1, 1, 1, 1)
        self.toolButton_76 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_76.sizePolicy().hasHeightForWidth())
        self.toolButton_76.setSizePolicy(sizePolicy)
        self.toolButton_76.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-left: 2px solid #8b8f8b;    \n"
"}")
        self.toolButton_76.setText("")
        self.toolButton_76.setObjectName("toolButton_76")
        self.gridLayout22.addWidget(self.toolButton_76, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout22, 2, 3, 1, 1)
        self.gridLayout11 = QtWidgets.QGridLayout()
        self.gridLayout11.setSpacing(0)
        self.gridLayout11.setObjectName("gridLayout11")
        self.toolButton_39 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_39.sizePolicy().hasHeightForWidth())
        self.toolButton_39.setSizePolicy(sizePolicy)
        self.toolButton_39.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-top: 2px solid #8b8f8b;    \n"
"}\n"
"\n"
"")
        self.toolButton_39.setText("")
        self.toolButton_39.setObjectName("toolButton_39")
        self.gridLayout11.addWidget(self.toolButton_39, 0, 1, 1, 1)
        self.toolButton_38 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_38.sizePolicy().hasHeightForWidth())
        self.toolButton_38.setSizePolicy(sizePolicy)
        self.toolButton_38.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-right: 2px solid #8b8f8b;    \n"
"    border-top: 2px solid #8b8f8b;    \n"
"}")
        self.toolButton_38.setText("")
        self.toolButton_38.setObjectName("toolButton_38")
        self.gridLayout11.addWidget(self.toolButton_38, 0, 2, 1, 1)
        self.toolButton_41 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_41.sizePolicy().hasHeightForWidth())
        self.toolButton_41.setSizePolicy(sizePolicy)
        self.toolButton_41.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"}")
        self.toolButton_41.setText("")
        self.toolButton_41.setObjectName("toolButton_41")
        self.gridLayout11.addWidget(self.toolButton_41, 1, 1, 1, 1)
        self.toolButton_40 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_40.sizePolicy().hasHeightForWidth())
        self.toolButton_40.setSizePolicy(sizePolicy)
        self.toolButton_40.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-left: 2px solid #8b8f8b;    \n"
"}")
        self.toolButton_40.setText("")
        self.toolButton_40.setObjectName("toolButton_40")
        self.gridLayout11.addWidget(self.toolButton_40, 1, 0, 1, 1)
        self.toolButton_42 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_42.sizePolicy().hasHeightForWidth())
        self.toolButton_42.setSizePolicy(sizePolicy)
        self.toolButton_42.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-right: 2px solid #8b8f8b;    \n"
"}")
        self.toolButton_42.setText("")
        self.toolButton_42.setObjectName("toolButton_42")
        self.gridLayout11.addWidget(self.toolButton_42, 1, 2, 1, 1)
        self.toolButton_37 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_37.sizePolicy().hasHeightForWidth())
        self.toolButton_37.setSizePolicy(sizePolicy)
        self.toolButton_37.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-left: 2px solid #8b8f8b;    \n"
"    border-top: 2px solid #8b8f8b;    \n"
"}")
        self.toolButton_37.setText("")
        self.toolButton_37.setObjectName("toolButton_37")
        self.gridLayout11.addWidget(self.toolButton_37, 0, 0, 1, 1)
        self.toolButton_43 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_43.sizePolicy().hasHeightForWidth())
        self.toolButton_43.setSizePolicy(sizePolicy)
        self.toolButton_43.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-left: 2px solid #8b8f8b;    \n"
"    border-bottom: 2px solid #8b8f8b;    \n"
"}")
        self.toolButton_43.setText("")
        self.toolButton_43.setObjectName("toolButton_43")
        self.gridLayout11.addWidget(self.toolButton_43, 2, 0, 1, 1)
        self.toolButton_44 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_44.sizePolicy().hasHeightForWidth())
        self.toolButton_44.setSizePolicy(sizePolicy)
        self.toolButton_44.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-bottom: 2px solid #8b8f8b;    \n"
"}")
        self.toolButton_44.setText("")
        self.toolButton_44.setObjectName("toolButton_44")
        self.gridLayout11.addWidget(self.toolButton_44, 2, 1, 1, 1)
        self.toolButton_45 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_45.sizePolicy().hasHeightForWidth())
        self.toolButton_45.setSizePolicy(sizePolicy)
        self.toolButton_45.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-right: 2px solid #8b8f8b;    \n"
"    border-bottom: 2px solid #8b8f8b;    \n"
"}")
        self.toolButton_45.setText("")
        self.toolButton_45.setObjectName("toolButton_45")
        self.gridLayout11.addWidget(self.toolButton_45, 2, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout11, 1, 2, 1, 1)
        self.gridLayout02 = QtWidgets.QGridLayout()
        self.gridLayout02.setSpacing(0)
        self.gridLayout02.setObjectName("gridLayout02")
        self.toolButton_21 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_21.sizePolicy().hasHeightForWidth())
        self.toolButton_21.setSizePolicy(sizePolicy)
        self.toolButton_21.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-top: 4px solid #8b8f8b;\n"
"    border-right: 4px solid #8b8f8b;    \n"
"}")
        self.toolButton_21.setText("")
        self.toolButton_21.setObjectName("toolButton_21")
        self.gridLayout02.addWidget(self.toolButton_21, 0, 2, 1, 1)
        self.toolButton_22 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_22.sizePolicy().hasHeightForWidth())
        self.toolButton_22.setSizePolicy(sizePolicy)
        self.toolButton_22.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-left: 2px solid #8b8f8b;    \n"
"}")
        self.toolButton_22.setText("")
        self.toolButton_22.setObjectName("toolButton_22")
        self.gridLayout02.addWidget(self.toolButton_22, 1, 0, 1, 1)
        self.toolButton_24 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_24.sizePolicy().hasHeightForWidth())
        self.toolButton_24.setSizePolicy(sizePolicy)
        self.toolButton_24.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-right: 4px solid #8b8f8b;    \n"
"}")
        self.toolButton_24.setText("")
        self.toolButton_24.setObjectName("toolButton_24")
        self.gridLayout02.addWidget(self.toolButton_24, 1, 2, 1, 1)
        self.toolButton_25 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_25.sizePolicy().hasHeightForWidth())
        self.toolButton_25.setSizePolicy(sizePolicy)
        self.toolButton_25.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-left: 2px solid #8b8f8b;    \n"
"    border-bottom: 2px solid #8b8f8b;    \n"
"}")
        self.toolButton_25.setText("")
        self.toolButton_25.setObjectName("toolButton_25")
        self.gridLayout02.addWidget(self.toolButton_25, 2, 0, 1, 1)
        self.toolButton_23 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_23.sizePolicy().hasHeightForWidth())
        self.toolButton_23.setSizePolicy(sizePolicy)
        self.toolButton_23.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"}")
        self.toolButton_23.setText("")
        self.toolButton_23.setObjectName("toolButton_23")
        self.gridLayout02.addWidget(self.toolButton_23, 1, 1, 1, 1)
        self.toolButton_27 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_27.sizePolicy().hasHeightForWidth())
        self.toolButton_27.setSizePolicy(sizePolicy)
        self.toolButton_27.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-right: 4px solid #8b8f8b;    \n"
"    border-bottom: 2px solid #8b8f8b;    \n"
"}")
        self.toolButton_27.setText("")
        self.toolButton_27.setObjectName("toolButton_27")
        self.gridLayout02.addWidget(self.toolButton_27, 2, 2, 1, 1)
        self.toolButton_20 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_20.sizePolicy().hasHeightForWidth())
        self.toolButton_20.setSizePolicy(sizePolicy)
        self.toolButton_20.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-top: 4px solid #8b8f8b;\n"
"}")
        self.toolButton_20.setText("")
        self.toolButton_20.setObjectName("toolButton_20")
        self.gridLayout02.addWidget(self.toolButton_20, 0, 1, 1, 1)
        self.toolButton_19 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_19.sizePolicy().hasHeightForWidth())
        self.toolButton_19.setSizePolicy(sizePolicy)
        self.toolButton_19.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-left: 2px solid #8b8f8b;    \n"
"    border-top: 4px solid #8b8f8b;    \n"
"}")
        self.toolButton_19.setText("")
        self.toolButton_19.setObjectName("toolButton_19")
        self.gridLayout02.addWidget(self.toolButton_19, 0, 0, 1, 1)
        self.toolButton_26 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_26.sizePolicy().hasHeightForWidth())
        self.toolButton_26.setSizePolicy(sizePolicy)
        self.toolButton_26.setText("")
        self.toolButton_26.setObjectName("toolButton_26")
        self.gridLayout02.addWidget(self.toolButton_26, 2, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout02, 0, 3, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.toolButton_10 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_10.sizePolicy().hasHeightForWidth())
        self.toolButton_10.setSizePolicy(sizePolicy)
        self.toolButton_10.setStyleSheet("QToolButton {\n"
"background-color: white;\n"
"border: 1px solid #c8ccc8;    \n"
"    border-left: 2px solid #8b8f8b;    \n"
"    border-top: 4px solid #8b8f8b;\n"
"\n"
"\n"
"}")
        self.toolButton_10.setText("")
        self.toolButton_10.setObjectName("toolButton_10")
        self.gridLayout_2.addWidget(self.toolButton_10, 0, 0, 1, 1)
        self.toolButton_12 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_12.sizePolicy().hasHeightForWidth())
        self.toolButton_12.setSizePolicy(sizePolicy)
        self.toolButton_12.setStyleSheet("QToolButton {\n"
"background-color: white;\n"
"border: 1px solid #c8ccc8;    \n"
"    border-top: 4px solid #8b8f8b;\n"
"\n"
"}")
        self.toolButton_12.setText("")
        self.toolButton_12.setObjectName("toolButton_12")
        self.gridLayout_2.addWidget(self.toolButton_12, 0, 1, 1, 1)
        self.toolButton_11 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_11.sizePolicy().hasHeightForWidth())
        self.toolButton_11.setSizePolicy(sizePolicy)
        self.toolButton_11.setStyleSheet("QToolButton {\n"
"background-color: white;\n"
"border: 1px solid #c8ccc8;    \n"
"    border-left: 2px solid #8b8f8b;    \n"
"\n"
"}")
        self.toolButton_11.setText("")
        self.toolButton_11.setObjectName("toolButton_11")
        self.gridLayout_2.addWidget(self.toolButton_11, 1, 0, 1, 1)
        self.toolButton_14 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_14.sizePolicy().hasHeightForWidth())
        self.toolButton_14.setSizePolicy(sizePolicy)
        self.toolButton_14.setStyleSheet("QToolButton {\n"
"background-color: white;\n"
"border: 1px solid #c8ccc8;    \n"
"    border-right: 2px solid #8b8f8b;    \n"
"    border-top: 4px solid #8b8f8b;\n"
"\n"
"\n"
"}")
        self.toolButton_14.setText("")
        self.toolButton_14.setObjectName("toolButton_14")
        self.gridLayout_2.addWidget(self.toolButton_14, 0, 2, 1, 1)
        self.toolButton_15 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_15.sizePolicy().hasHeightForWidth())
        self.toolButton_15.setSizePolicy(sizePolicy)
        self.toolButton_15.setStyleSheet("QToolButton {\n"
"background-color: white;\n"
"border: 1px solid #c8ccc8;    \n"
"    border-right: 2px solid #8b8f8b;    \n"
"\n"
"}")
        self.toolButton_15.setText("")
        self.toolButton_15.setObjectName("toolButton_15")
        self.gridLayout_2.addWidget(self.toolButton_15, 1, 2, 1, 1)
        self.toolButton_13 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_13.sizePolicy().hasHeightForWidth())
        self.toolButton_13.setSizePolicy(sizePolicy)
        self.toolButton_13.setStyleSheet("QToolButton {\n"
"background-color: white;\n"
"border: 1px solid #c8ccc8;    \n"
"}")
        self.toolButton_13.setText("")
        self.toolButton_13.setObjectName("toolButton_13")
        self.gridLayout_2.addWidget(self.toolButton_13, 1, 1, 1, 1)
        self.toolButton_16 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_16.sizePolicy().hasHeightForWidth())
        self.toolButton_16.setSizePolicy(sizePolicy)
        self.toolButton_16.setStyleSheet("QToolButton {\n"
"background-color: white;\n"
"border: 1px solid #c8ccc8;    \n"
"    border-left: 2px solid #8b8f8b;    \n"
"    border-bottom: 2px solid #8b8f8b;    \n"
"\n"
"}")
        self.toolButton_16.setText("")
        self.toolButton_16.setObjectName("toolButton_16")
        self.gridLayout_2.addWidget(self.toolButton_16, 2, 0, 1, 1)
        self.toolButton_17 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_17.sizePolicy().hasHeightForWidth())
        self.toolButton_17.setSizePolicy(sizePolicy)
        self.toolButton_17.setStyleSheet("QToolButton {\n"
"background-color: white;\n"
"border: 1px solid #c8ccc8;    \n"
"    border-bottom: 2px solid #8b8f8b;    \n"
"\n"
"}")
        self.toolButton_17.setText("")
        self.toolButton_17.setObjectName("toolButton_17")
        self.gridLayout_2.addWidget(self.toolButton_17, 2, 1, 1, 1)
        self.toolButton_18 = QtWidgets.QToolButton(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_18.sizePolicy().hasHeightForWidth())
        self.toolButton_18.setSizePolicy(sizePolicy)
        self.toolButton_18.setStyleSheet("QToolButton {\n"
"background-color: white;\n"
"border: 1px solid #c8ccc8;    \n"
"    border-right: 2px solid #8b8f8b;    \n"
"    border-bottom: 2px solid #8b8f8b;    \n"
"\n"
"}")
        self.toolButton_18.setText("")
        self.toolButton_18.setObjectName("toolButton_18")
        self.gridLayout_2.addWidget(self.toolButton_18, 2, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 2, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_5)
        self.gridLayout_3.addWidget(self.stackedWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.usernameLabel.setText(_translate("MainWindow", "username:"))
        self.signUpButton.setText(_translate("MainWindow", "Sign Up"))
        self.label_4.setText(_translate("MainWindow", "or"))
        self.label.setText(_translate("MainWindow", "Sudo-ku"))
        self.passwordLabel.setText(_translate("MainWindow", "password:"))
        self.signInButton.setText(_translate("MainWindow", "Sign In"))
        self.label_2.setText(_translate("MainWindow", "Registration"))
        self.passwordLabel_2.setText(_translate("MainWindow", "password:"))
        self.usernameLabel_2.setText(_translate("MainWindow", "username:"))
        self.label_3.setText(_translate("MainWindow", "repeat password:"))
        self.registrationButton.setText(_translate("MainWindow", "Sign Up"))
        self.challengeButton.setText(_translate("MainWindow", "Challenge"))
        self.collaborativeButton.setText(_translate("MainWindow", "Collaborative"))
        self.easyButton.setText(_translate("MainWindow", "Easy"))
        self.mediumButton.setText(_translate("MainWindow", "Medium"))
        self.hardButton.setText(_translate("MainWindow", "Hard"))
        self.toolButton_26.setStyleSheet(_translate("MainWindow", "QToolButton {\n"
"    background-color: white;\n"
"    border: 1px solid #c8ccc8;    \n"
"    border-bottom: 2px solid #8b8f8b;    \n"
"}"))
