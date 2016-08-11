#!/usr/bin/env python

from tinydb import TinyDB, where

class DatabaseHandler():
	def __init__(self):
		self.db = TinyDB('database.json')
		self.admin_table = self.db.table('admin')
		self.users_table = self.db.table('users')
		self.files_table = self.db.table('files')
		self.folders_table = self.db.table('folders')
		self.shares_table = self.db.table('shares')

	def insert_admin_values(self, login, password, host):
		if (len(self.admin_table) == 0):
			self.admin_table.insert({'login': login, 'password': password, 'host': host})
		else:
			self.admin_table.update({'login': login, 'password': password, 'host': host}, eids=[1])

	def insert_user(self, login, password):
		self.users_table.insert({'login': login, 'password': password})

	def get_user_password(self, login):
		return self.users_table.search(where('login') == login)[0]['password']

	def insert_users(self, elements):
		for user,password in elements:
			self.users_table.insert({'login': login, 'password': password})

	def insert_file(self, user, path, destination):
		self.files_table.insert({'user': user, 'path':path, 'destination':destination})

	def insert_files(self, elements):
		for user, path, destination in elements:
			self.files_table.insert({'user': user, 'path':path, 'destination':destination})

	def insert_folder(self, user, destination):
		self.folders_table.insert({'user': user, 'destination': destination})

	def insert_folders(self, elements):
		for user, path, destination in elements:
			self.folders_table.insert({'user': user, 'destination': destination})

	def insert_share(self, sharer, sharee, path, share_type):
		self.shares_table.insert({'sharer': sharer, 'sharee': sharee, 'path':path, 'share_type':share_type })

	def delete_all_users(self):
		self.users_table.purge()

	def delete_all_files(self):
		self.files_table.purge()

	def delete_all_folders(self):
		self.folders_table.purge()

	def delete_all_shares(self):
		self.shares_table.purge()

	def get_users_values(self):
		if (len(self.users_table) == 0):
			return None
		else:
			return self.users_table.all()

	def get_files_values(self):
		if (len(self.files_table) == 0):
			return None
		else:
			return self.files_table.all()

	def get_folders_values(self):
		if (len(self.folders_table) == 0):
			return None
		else:
			return self.folders_table.all()

	def get_shares_values(self):
		if (len(self.shares_table) == 0):
			return None
		else:
			return self.shares_table.all()

	def get_admin_values(self):
		if (len(self.admin_table) == 0):
			return None
		else:
			return self.admin_table.all()[0]