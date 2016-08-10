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
        self.pushButton_store_users.clicked.connect(self.handle_button_store_users)
        self.pushButton_create_users.clicked.connect(self.handle_button_create_users)
        self.pushButton_delete_users.clicked.connect(self.handle_button_delete_users)
        self.pushButton_new_element.clicked.connect(self.handle_button_add_row)
        self.pushButton_new_row_shares.clicked.connect(self.handle_button_new_row_shares)
        self.pushButton_check_connection.clicked.connect(self.handle_button_check_connection)
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
        self.tableWidget_users.setRowCount(users_number)
        self.tableWidget_users.setColumnCount(2)
        for row_number in range(0,users_number):
            self.tableWidget_users.setItem(row_number, 0, QTableWidgetItem(self.users_values[row_number]['login']))
            self.tableWidget_users.setItem(row_number, 1, QTableWidgetItem(self.users_values[row_number]['password']))

    def show_info(self, text, color='lightYellow'):
        destination = self.textBrowser_info
        destination.setTextColor(QColor(color))
        destination.append(text)

    def show_info_red(self, text):
        self.show_info(text, 'red')

    def show_info_green(self, text):
        self.show_info(text, 'lightGreen')

    def handle_button_store_credentials(self):
        admin_user = self.lineEdit_admin_user.text()
        admin_pw = self.lineEdit_admin_pw.text()
        host = self.lineEdit_host.text()
        self.dbhandler.insert_admin_values(admin_user, admin_pw, host)
        self.admin_values = self.dbhandler.get_admin_values()
        self.show_info(str(self.admin_values) + " Stored")
        self.init_populator()

    def handle_button_store_users(self):
        allRows = self.tableWidget_users.rowCount()
        self.dbhandler.delete_all_users()
        for row in range(0,allRows):
            twi0 = self.tableWidget_users.item(row,0)
            twi1 = self.tableWidget_users.item(row,1)
            if ((twi0 != None) and (twi1 != None)):
                if ((twi0.text() != '') and (twi1.text != '')):
                    self.dbhandler.insert_user(twi0.text(), twi1.text())
        self.show_info('Users stored in database')

    def handle_button_create_users(self):
        self.create_users()

    def handle_button_delete_users(self):
        self.delete_users()

    def create_users(self):
        self.users_values = self.dbhandler.get_users_values()
        for user in self.users_values:
            try:
                self.populator.pop_create_user(user['login'],user['password'])
            except Exception as e:
                print (str(e))
                self.show_info_red('user ' + str(user['login']) + ' creation failed')
            else:
                self.show_info_green('Created user ' + str(user['login']))

    def delete_users(self):
        self.users_values = self.dbhandler.get_users_values()
        for user in self.users_values:
            try:
                self.populator.pop_delete_user(user['login'])
            except Exception as e:
                print (str(e))
                self.show_info_red('user ' + str(user['login']) + ' deletion failed')
            else:
                self.show_info_green('Deleted user ' + str(user['login']))

    def handle_button_add_row(self):
        self.tableWidget_users.insertRow(self.tableWidget_users.rowCount())

    def handle_button_new_row_shares(self):
        self.tableWidget_shares.insertRow(self.tableWidget_users.rowCount())

    def handle_button_check_connection(self):
        try:
            self.populator.check_connection()
        except:
            self.show_info_red('Connection failed')
        else:
            self.show_info_green('Connection works!')

if __name__ == "__main__":
    
    
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
