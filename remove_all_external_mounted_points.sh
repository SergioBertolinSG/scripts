#!/bin/bash

if [ $# -ne 1 ];
then
   echo "Introduce the installation path as parameter"
   exit
fi

installation_path=$1


sudo -u www-data $installation_path/occ app:enable files_external
sudo -u www-data $installation_path/occ app:enable windows_network_drive

mysql -u root -h localhost -D owncloud --skip-column-names -s -e "select mount_id from oc_external_mounts;" | xargs -I xxx sudo -u www-data $installation_path/occ files_external:delete -y xxx
