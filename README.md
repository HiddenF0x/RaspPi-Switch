# RaspPi-Switch
Simple code for Pi home automation (web based)

Requirements
------------

1. This requires a <b>Raspberry Pi</b> with networking
1. Apache2 w/ php
1. A relay board

Installation
------------

1. Install Apache2 with PHP support
```
sudo apt-get install Apache2 php libapache2-mod-php
```
2. Copy all files into /var/www/html
3. Give permissions to files
```
sudo chmod -R 777 /var/www/html
```
4. Add www-data to sudoers
```
sudo visudo
ADD to the bottom: www-data ALL=NOPASSWD: ALL
```
5. Restart Apache2
```
sudo service apache2 restart
```

How to use
----------

1. Navigate to http://192.168.1.X
1. Click Button! (Triggers GPIO 17 and 18)


Screen Shots
------------
<p align="center">
   <img src="https://i.imgur.com/GmDXWOI.png">
</p>

<p algi="center">
   <img src="https://i.imgur.com/bcKwbgJ.png" width="50%" height="50%">
</p>