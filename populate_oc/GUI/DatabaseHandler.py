#!/usr/bin/env python

from tinydb import TinyDB, where

class DatabaseHandler():
	def __init__(self):
		self.db = TinyDB('database.json')
		self.admin_table = self.db.table('admin')
		self.users_table = self.db.table('users')

	def insert_admin_values(self, login, password, host):
		if (len(self.admin_table) == 0):
			self.admin_table.insert({'login': login, 'password': password, 'host': host})
		else:
			self.admin_table.update({'login': login, 'password': password, 'host': host}, eids=[1])

	def insert_user(self, login, password):
		self.users_table.insert({'login': login, 'password': password})

	def get_admin_values(self):
		if (len(self.admin_table) == 0):
			return None
		else:
			return self.admin_table.all()[0]



'''if __name__ == "__main__":
	dbhandler = DatabaseHandler()
	dbhandler.insert_admin_values('manolo', 'pp', 'localhost')'''