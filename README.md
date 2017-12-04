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
1. Copy all files into /var/www/html
1. Give permissions to files
```
sudo chmod -R 777 /var/www/html
```
1. Add www-data to sudoers
```
sudo visudo
ADD to the bottom: www-data ALL=NOPASSWD: ALL
```
1. Restart Apache2
```
sudo service apache2 restart

```

How to use
----------

1. Navigate to http://192.168.1.X
1. Click Button!


Screen Shots
------------

![Imgur Image.](https://i.imgur.com/GmDXWOI.png)
![Imgur Image.]([Imgur](https://i.imgur.com/bcKwbgJ.png)
