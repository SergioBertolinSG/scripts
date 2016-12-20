sudo chown -R www-data:www-data /home/vagrant/.npm
sudo chown -R www-data:www-data /home/vagrant/.cache
sudo chown -R www-data:www-data /home/vagrant/.local
sudo chown -R www-data:www-data /home/vagrant/.config
sudo chown -R www-data:www-data /home/vagrant/.composer
sudo rm -rf core
git clone https://github.com/owncloud/core.git
cd core
fecha=`date +%d-%m-%y`
sudo cp -r core "/var/www/html/master_$fecha"
sudo chown -R www-data:www-data "/var/www/html/master_$fecha"
cd "/var/www/html/master_$fecha"
sudo -u www-data make
