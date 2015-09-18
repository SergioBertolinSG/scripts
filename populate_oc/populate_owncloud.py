#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('pyocclient')
import owncloud
import datetime
import random
import shutil
import os
import logging


usage = '''
        Execute the script with this parameters.
        host(with port if needed) user password
        '''

if len(sys.argv) < 3:
    print usage
    sys.exit()


HOST = str(sys.argv[1]) 
USER = str(sys.argv[2])
PASSWORD = str(sys.argv[3])

FOLDER = 'testdir'
LOCALFILE = 'localfile.txt'
REMOTEFILE = 'remotefile.txt'




#import ipdb; ipdb.set_trace()


class Populator:
    """It populates owncloud"""

    def __init__(self, host, oc_user, oc_password, number_users, number_groups):
        logging.basicConfig(level=logging.INFO)
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
        self.oc.login(self.oc_user, self.oc_password)
        self.oc.mkdir('testdir')
        self.oc.put_file('testdir/remotefile.txt', 'localfile.txt')
        link_info = self.oc.share_file_with_link('testdir/remotefile.txt')
        print "Here is your link: http://domain.tld/owncloud/" + link_info.link
        self.oc.logout()
         

    def fill_users_array(self, number):
        for i in xrange(number):
            current_user = 'user' + str(i)
            self.users[current_user] = current_user
            
    def fill_groups_array(self, number):
        for i in xrange(number):
            current_group = 'group' + str(i)
            self.groups.append(current_group)
            


    def create_users(self):
        self.oc.login(self.oc_user, self.oc_password)
        for user in self.users:
            self.oc.create_user(user, self.users[user])
            self.logger.info('Creating user ' + user)
        self.oc.logout()

    def remove_users(self):
        self.oc.login(self.oc_user, self.oc_password)
        for user in self.users:
            self.oc.delete_user(user)
        self.oc.logout()

    def remove_groups(self):
        self.oc.login(self.oc_user, self.oc_password)
        for group in self.groups:
            self.oc.delete_group(group)
        self.oc.logout()


    def create_groups(self):
        self.oc.login(self.oc_user, self.oc_password)
        for group in self.groups:
            self.oc.create_group(group)
            self.logger.info('Creating group ' + group)
        self.oc.logout()

    def assign_group_to_users(self):
        self.oc.login(self.oc_user, self.oc_password)
        for user in self.users:
            self.users_groups[user] = random.choice(self.groups) 
            self.oc.add_user_to_group(user, self.users_groups[user])
        self.oc.logout()

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






def populate_oc_real():
    p = Populator(HOST, USER, PASSWORD, 100, 10)
    #p.check_connection()
    p.remove_users()
    p.remove_groups()
    p.create_users()
    p.create_groups()
    p.assign_group_to_users()
    p.create_deep_structure('user0','user0',12)



populate_oc_real()

