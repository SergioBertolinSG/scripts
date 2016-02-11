#!/bin/bash

if [ $# -ne 1 ];
then
   echo "First parameter is the location of the path of the owncloud code for making the upgrade"
   exit
fi


PATH_ORIGIN=$1
PATH_DESTINATION=/opt/owncloud

mkdir /tmp/owncloud_tmp

mv $PATH_DESTINATION/config /tmp/owncloud_tmp
cp -r $PATH_DESTINATION/data /tmp/owncloud_tmp

rm -rf $PATH_DESTINATION/*

mv /tmp/owncloud_tmp/config $PATH_DESTINATION
mv /tmp/owncloud_tmp/data $PATH_DESTINATION

cp -r $PATH_ORIGIN/* $PATH_DESTINATION
cp $PATH_ORIGIN/.user.ini $PATH_DESTINATION
cp $PATH_ORIGIN/.htaccess $PATH_DESTINATION

chown -R www-data:www-data "$PATH_DESTINATION"
chmod a+x "$PATH_DESTINATION/occ"
sudo -u www-data $PATH_DESTINATION/occ upgrade
