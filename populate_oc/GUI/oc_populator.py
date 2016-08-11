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
        self.pushButton_check_connection.clicked.connect(self.handle_button_check_connection)
        self.pushButton_add_row_files.clicked.connect(lambda: self.handle_button_add_row_generico(self.tableWidget_files))
        self.pushButton_add_row_folders.clicked.connect(lambda: self.handle_button_add_row_generico(self.tableWidget_folders))
        self.pushButton_new_row_shares.clicked.connect(lambda: self.handle_button_add_row_generico(self.tableWidget_shares))
        self.pushButton_store_files.clicked.connect(self.handle_button_store_files)
        self.pushButton_store_folders.clicked.connect(self.handle_button_store_folders)
        self.pushButton_upload_files.clicked.connect(self.handle_button_upload_files)
        self.pushButton_create_folders.clicked.connect(self.handle_button_create_folders)
        self.pushButton_store_shares.clicked.connect(self.handle_button_store_shares)
        self.pushButton_create_shares.clicked.connect(self.handle_button_create_shares)
        self.dbhandler = DatabaseHandler()
        #self.populator = Populator()
        self.read_database()
        self.fill_users_table()
        self.fill_files_table()
        self.fill_folders_table()
        self.fill_shares_table()
        self.init_populator()

    def read_database(self):
        self.admin_values = self.dbhandler.get_admin_values()
        if (self.admin_values != None):
            self.lineEdit_admin_user.setText(self.admin_values['login'])
            self.lineEdit_admin_pw.setText(self.admin_values['password'])
            self.lineEdit_host.setText(self.admin_values['host'])
        self.users_values = self.dbhandler.get_users_values()
        self.files_values = self.dbhandler.get_files_values()
        self.folders_values = self.dbhandler.get_folders_values()
        self.shares_values = self.dbhandler.get_shares_values()


    def init_populator(self):
        if (self.admin_values != None):
            self.populator = Populator(self.admin_values['host'], 
                                       self.admin_values['login'], 
                                       self.admin_values['password'], 0, 0)

    def fill_users_table(self):
        try:
            users_number = len(self.users_values)
        except:
            return
        self.tableWidget_users.setRowCount(users_number)
        self.tableWidget_users.setColumnCount(2)
        for row_number in range(0,users_number):
            self.tableWidget_users.setItem(row_number, 0, QTableWidgetItem(self.users_values[row_number]['login']))
            self.tableWidget_users.setItem(row_number, 1, QTableWidgetItem(self.users_values[row_number]['password']))

    def fill_files_table(self):
        try:
            files_number = len(self.files_values)
        except:
            return
        self.tableWidget_files.setRowCount(files_number)
        self.tableWidget_files.setColumnCount(3)
        for row_number in range(0,files_number):
            self.tableWidget_files.setItem(row_number, 0, QTableWidgetItem(self.files_values[row_number]['user']))
            self.tableWidget_files.setItem(row_number, 1, QTableWidgetItem(self.files_values[row_number]['path']))
            self.tableWidget_files.setItem(row_number, 2, QTableWidgetItem(self.files_values[row_number]['destination']))

    def fill_folders_table(self):
        try:
            folders_number = len(self.folders_values)
        except:
            return
        self.tableWidget_folders.setRowCount(folders_number)
        self.tableWidget_folders.setColumnCount(2)
        for row_number in range(0,folders_number):
            self.tableWidget_folders.setItem(row_number, 0, QTableWidgetItem(self.folders_values[row_number]['user']))
            self.tableWidget_folders.setItem(row_number, 1, QTableWidgetItem(self.folders_values[row_number]['destination']))

    def fill_shares_table(self):
        try:
            shares_number = len(self.shares_values)
        except:
            return
        self.tableWidget_shares.setRowCount(shares_number)
        self.tableWidget_shares.setColumnCount(4)
        for row_number in range(0, shares_number):
            self.tableWidget_shares.setItem(row_number, 0, QTableWidgetItem(self.shares_values[row_number]['sharer']))
            self.tableWidget_shares.setItem(row_number, 1, QTableWidgetItem(self.shares_values[row_number]['sharee']))
            self.tableWidget_shares.setItem(row_number, 2, QTableWidgetItem(self.shares_values[row_number]['path']))
            self.tableWidget_shares.setItem(row_number, 3, QTableWidgetItem(self.shares_values[row_number]['share_type']))

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

    def handle_button_store_files(self):
        allRows = self.tableWidget_files.rowCount()
        self.dbhandler.delete_all_files()
        for row in range(0,allRows):
            twi0 = self.tableWidget_files.item(row,0)
            twi1 = self.tableWidget_files.item(row,1)
            twi2 = self.tableWidget_files.item(row,2)
            if ((twi0 != None) and (twi1 != None) and (twi2 != None)):
                if ((twi0.text() != '') and (twi1.text != '') and (twi2.text != '')):
                    self.dbhandler.insert_file(twi0.text(), twi1.text(), twi2.text())
        self.show_info('Files to upload stored in database')

    def handle_button_store_folders(self):
        allRows = self.tableWidget_folders.rowCount()
        self.dbhandler.delete_all_folders()
        for row in range(0,allRows):
            twi0 = self.tableWidget_folders.item(row,0)
            twi1 = self.tableWidget_folders.item(row,1)
            if ((twi0 != None) and (twi1 != None)):
                if ((twi0.text() != '') and (twi1.text != '')):
                    self.dbhandler.insert_folder(twi0.text(), twi1.text())
        self.show_info('Folders to create stored in database')

    def handle_button_store_shares(self):
        allRows = self.tableWidget_shares.rowCount()
        self.dbhandler.delete_all_shares()
        for row in range(0,allRows):
            twi0 = self.tableWidget_shares.item(row,0)
            twi1 = self.tableWidget_shares.item(row,1)
            twi2 = self.tableWidget_shares.item(row,2)
            twi3 = self.tableWidget_shares.item(row,3)
            if ((twi0 != None) and (twi1 != None) and (twi2 != None) and (twi3 != None)):
                if ((twi0.text() != '') and (twi2.text != '') and (twi3.text != '')):
                    self.dbhandler.insert_share(twi0.text(), twi1.text(), twi2.text(), twi3.text())
        self.show_info('Shares to create stored in database')

    def handle_button_upload_files(self):
        self.upload_files()

    def upload_files(self):
        self.files_values = self.dbhandler.get_files_values()
        for file in self.files_values:
            try:
                passwd = self.dbhandler.get_user_password(file['user'])
                self.populator.pop_upload_file(file['user'], passwd, file['path'], file['destination'])
            except Exception as e:
                print (str(e))
                self.show_info_red('Upload of' + str(file['path']) + ' failed')
            else:
                self.show_info_green('Upload of ' + str(file['path']) + ' succeed')

    def handle_button_create_folders(self):
        self.create_folders()

    def create_folders(self):
        self.folders_values = self.dbhandler.get_folders_values()
        for folder in self.folders_values:
            try:
                passwd = self.dbhandler.get_user_password(folder['user'])
                self.populator.pop_create_folder(folder['user'], passwd, folder['destination'])
            except Exception as e:
                print (str(e))
                self.show_info_red('Creation of ' + str(folder['destination']) + ' failed')
            else:
                self.show_info_green('Creation of ' + str(folder['destination']) + ' succeed')

    def handle_button_create_shares(self):
        self.create_shares()

    def create_shares(self):
        self.shares_values = self.dbhandler.get_shares_values()
        for share in self.shares_values:
            try:
                passwd = self.dbhandler.get_user_password(share['sharer'])
                self.populator.pop_share_file(share['sharer'],
                                              passwd,
                                              share['sharee'],
                                              share['path'],
                                              share['share_type'])
            except Exception as e:
                print (str(e))
                self.show_info_red('Sharing ' + str(share['path']) + ' failed')
            else:
                self.show_info_green('Sharing ' + str(share['path']) + ' succeed')

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

    def handle_button_add_row_generico(self, tablewidget):
        tablewidget.insertRow(tablewidget.rowCount())

    def handle_button_add_row(self):
        self.tableWidget_users.insertRow(self.tableWidget_users.rowCount())

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
