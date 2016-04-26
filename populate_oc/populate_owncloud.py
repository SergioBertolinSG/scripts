#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""Usage:
  populate_owncloud.py [--host=<host>] [--user=<user>] [--password=<password>] 
                       [--deep-structure=<deep-length>] [--assign-group-to-users] [--create-users] 
                       [--create-groups] [--check-connection]
  populate_owncloud.py -h | --help

  Options:
    -h --help                   Show this help message and exit.
    --host=<host>               OwnCloud server, include the port
    --user=<user>               OwnCloud server admin user
    --password=<password>       OwnCloud server admin password
    --check-connection          Checks the connection with the server.
    --create-users              Create users.
    --create-groups             Create groups.
    --assign-group-to-users     Assign a group to every user.
    --deep-structure=N          How deep will be the deepest folder of user0.

"""
from docopt import docopt
from termcolor import colored
import sys
sys.path.append('pyocclient')
import owncloud
import datetime
import random
import shutil
import os
import logging

FOLDER = 'testdir'
LOCALFILE = 'localfile.txt'
REMOTEFILE = 'remotefile.txt'

class Populator:
    """It populates owncloud"""

    def __init__(self, host, oc_user, oc_password, number_users, number_groups):
        logging.basicConfig(level=logging.ERROR)
        self.logger = logging.getLogger(__name__)
        self.oc = owncloud.Client(host)
        self.users = {}
        self.groups = []
        self.users_groups = {}
        self.oc_user = oc_user
        self.oc_password = oc_password
        self.fill_users_array(number_users)
        self.fill_groups_array(number_groups)
  
    def check_connection(self):
        try:
            self.oc.login(self.oc_user, self.oc_password)
            self.oc.mkdir('testdir')
            self.oc.put_file('testdir/remotefile.txt', 'localfile.txt')
            link_info = self.oc.share_file_with_link('testdir/remotefile.txt')
            print colored("Here is your link: " + link_info.get_link(), 'green')
            self.oc.delete('testdir')
            self.oc.logout()
        except:
            print colored("Connection failed", 'red')

    def fill_users_array(self, number):
        for i in xrange(number):
            current_user = 'user' + str(i)
            self.users[current_user] = current_user
            
    def fill_groups_array(self, number):
        for i in xrange(number):
            current_group = 'group' + str(i)
            self.groups.append(current_group)

    def create_users(self):
        try:
            self.oc.login(self.oc_user, self.oc_password)
            for user in self.users:
                self.oc.create_user(user, self.users[user])
                self.logger.info('Creating user ' + user)
            self.oc.logout()
            print colored("Created users", 'green')
        except:
            print colored("Users couln't be created", 'red')


    def remove_users(self):
        try:
            self.oc.login(self.oc_user, self.oc_password)
            for user in self.users:
                self.oc.delete_user(user)
            self.oc.logout()
            print colored("Users removed", 'green')
        except:
            print colored("Users couln't be removed", 'red')

    def remove_groups(self):
        try:
            self.oc.login(self.oc_user, self.oc_password)
            for group in self.groups:
                self.oc.delete_group(group)
            self.oc.logout()
            print colored("Groups removed", 'green')
        except:
            print colored("Groups couln't be removed", 'red')

    def create_groups(self):
        try:
            self.oc.login(self.oc_user, self.oc_password)
            for group in self.groups:
                self.oc.create_group(group)
                self.logger.info('Creating group ' + group)
            self.oc.logout()
            print colored("Groups created", 'green')
        except:
            print colored("Groups couln't be created", 'red')

    def assign_group_to_users(self):
        try:
            self.oc.login(self.oc_user, self.oc_password)
            for user in self.users:
                self.users_groups[user] = random.choice(self.groups) 
                self.oc.add_user_to_group(user, self.users_groups[user])
            self.oc.logout()
            print colored("Every user assigned to a group", 'green')
        except:
            print colored("Groups couln't be assigned to users", 'red')

    def name_generator(self):
        #r = random.Random(500)
        one = ['AA', 'BB', 'CC', 'DD']
        two = ['ZZ', 'YY', 'XX', 'WW']
        return str(random.choice(one)) + str(random.choice(one)) +str(random.randint(1,999999))

    
    def create_deep_structure(self, user, password, depth):
        self.logger.info('Creating deep structure for ' + user)
        self.oc.login(user, password)
        current_path = ''
        for i in xrange(depth):
            current_path = current_path + '/' + self.name_generator() 
            self.oc.mkdir(current_path)
            self.oc.put_file(current_path + '/' + REMOTEFILE, LOCALFILE)
        self.oc.logout()

    def create_modified_textfile(self):
        new_name = self.name_generator() + '.txt'
        shutil.copy2(LOCALFILE, new_name)
        modified_localfile = open (new_name, 'w')
        with open(new_name, "a") as modified_localfile:
            modified_localfile.write(new_name)
        return new_name

    def remove_modified_textfile(self, filename):
        if os.path.isfile(filename):
            os.remove(filename)
        else:    
            print("Error: %s file not found" % filename)

    def upload_many_textfiles(self, user, password, number):
        self.oc.login(user, password)
        self.oc.mkdir(FOLDER)
        for i in xrange(number):
            current_filename = self.create_modified_textfile()
            self.oc.put_file(FOLDER + '/' + current_filename, current_filename)
            self.remove_modified_textfile(current_filename)
        self.oc.logout()

def populate_oc_real(host, 
                     user, 
                     password, 
                     create_deep_structure, 
                     create_users, 
                     create_groups, 
                     assign_group_to_users,
                     check_connection):
    p = Populator(host, user, password, 100, 10)
    if check_connection == True:
        p.check_connection()
    if create_users == True:
        p.remove_users()
        p.create_users()
    if create_groups == True:
        p.remove_groups()
        p.create_groups()
    if assign_group_to_users == True:
        p.assign_group_to_users()
    if create_deep_structure > 1:
        p.create_deep_structure('user0','user0',12)

if __name__ == '__main__':
    arguments = docopt(__doc__, version='populate_owncloud 0')
    host = arguments['--host']
    user = arguments['--user']
    password = arguments['--password']
    create_deep_structure = arguments['--deep-structure']
    create_users = arguments['--create-users']
    create_groups = arguments['--create-groups']
    assign_group_to_users = arguments['--assign-group-to-users']
    check_connection = arguments['--check-connection']
    if (host == None) or (user == None) or (password == None):
         sys.exit()
    populate_oc_real(host,
                     user,
                     password, 
                     create_deep_structure, 
                     create_users, 
                     create_groups, 
                     assign_group_to_users,
                     check_connection)

