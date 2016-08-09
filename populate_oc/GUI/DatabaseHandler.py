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

	def insert_users(self, elements):
		for user,password in elements:
			self.users_table.insert({'login': login, 'password': password})

	def delete_all_users(self):
		self.users_table.purge()

	def get_users_values(self):
		if (len(self.users_table) == 0):
			return None
		else:
			return self.users_table.all()

	def get_admin_values(self):
		if (len(self.admin_table) == 0):
			return None
		else:
			return self.admin_table.all()[0]