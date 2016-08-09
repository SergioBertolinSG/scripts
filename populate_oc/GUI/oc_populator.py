#!/usr/bin/env python

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ui_oc_populator import Ui_MainWindow
from DatabaseHandler import DatabaseHandler
from Populator import Populator

class MyApp(QMainWindow, Ui_MainWindow):
    parse_triggered = pyqtSignal()

    def __init__(self, parent=None, name=None):
        super(MyApp, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_store_credentials.clicked.connect(self.handle_button_store_credentials)
        self.pushButton_create_users.clicked.connect(self.handle_button_create_users)
        self.dbhandler = DatabaseHandler()
        #self.populator = Populator()
        self.read_database()
        self.fill_users_table()
        self.init_populator()

    def read_database(self):
        self.admin_values = self.dbhandler.get_admin_values()
        if (self.admin_values != None):
            self.lineEdit_admin_user.setText(self.admin_values['login'])
            self.lineEdit_admin_pw.setText(self.admin_values['password'])
            self.lineEdit_host.setText(self.admin_values['host'])
        self.users_values = self.dbhandler.get_users_values()

    def init_populator(self):
        if (self.admin_values != None):
            self.populator = Populator(self.admin_values['host'], 
                                       self.admin_values['login'], 
                                       self.admin_values['password'], 0, 0)

    def fill_users_table(self):
        users_number = len(self.users_values)
        for row_number in range(0,users_number):
            print (row_number)
            self.tableWidget_users.setItem(row_number, 0, QTableWidgetItem(self.users_values[row_number]['login']))
            self.tableWidget_users.setItem(row_number, 1, QTableWidgetItem(self.users_values[row_number]['password']))

    def handle_button_store_credentials(self):
        #self.label_host.setText("BUTTON CLICKED!!")
        admin_user = self.lineEdit_admin_user.text()
        admin_pw = self.lineEdit_admin_pw.text()
        host = self.lineEdit_host.text()
        self.dbhandler.insert_admin_values(admin_user, admin_pw, host)

    def handle_button_create_users(self):
        #self.label_host.setText("BUTTON CLICKED!!")
        allRows = self.tableWidget_users.rowCount()
        #print ('allRows are ' + str(allRows))
        self.dbhandler.delete_all_users()
        for row in range(0,allRows):
            twi0 = self.tableWidget_users.item(row,0)
            twi1 = self.tableWidget_users.item(row,1)
            if ((twi0 != None) and (twi1 != None)):
                self.dbhandler.insert_user(twi0.text(), twi1.text())
                #print (twi0.text()+' '+twi1.text())

        #self.dbhandler.insert_admin_values(admin_user, admin_pw, host)

if __name__ == "__main__":
    
    
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
