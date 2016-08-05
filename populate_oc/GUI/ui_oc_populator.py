# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'oc_populator.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 771, 521))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(79, 56, 251, 141))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_host = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_host.setObjectName("label_host")
        self.verticalLayout_2.addWidget(self.label_host)
        self.label_admin_user = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_admin_user.setObjectName("label_admin_user")
        self.verticalLayout_2.addWidget(self.label_admin_user)
        self.label_admin_pw = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_admin_pw.setObjectName("label_admin_pw")
        self.verticalLayout_2.addWidget(self.label_admin_pw)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_host = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_host.setObjectName("lineEdit_host")
        self.verticalLayout.addWidget(self.lineEdit_host)
        self.lineEdit_admin_user = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_admin_user.setObjectName("lineEdit_admin_user")
        self.verticalLayout.addWidget(self.lineEdit_admin_user)
        self.lineEdit_admin_pw = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_admin_pw.setObjectName("lineEdit_admin_pw")
        self.verticalLayout.addWidget(self.lineEdit_admin_pw)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.pushButton_store_credentials = QtWidgets.QPushButton(self.tab)
        self.pushButton_store_credentials.setGeometry(QtCore.QRect(50, 220, 171, 51))
        self.pushButton_store_credentials.setObjectName("pushButton_store_credentials")
        self.pushButton_check_connection = QtWidgets.QPushButton(self.tab)
        self.pushButton_check_connection.setGeometry(QtCore.QRect(220, 220, 171, 51))
        self.pushButton_check_connection.setToolTipDuration(9)
        self.pushButton_check_connection.setObjectName("pushButton_check_connection")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_host.setText(_translate("MainWindow", "Host"))
        self.label_admin_user.setText(_translate("MainWindow", "Admin User"))
        self.label_admin_pw.setText(_translate("MainWindow", "Admin Password"))
        self.pushButton_store_credentials.setText(_translate("MainWindow", "Store Credentials"))
        self.pushButton_check_connection.setText(_translate("MainWindow", "Check connection"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))

