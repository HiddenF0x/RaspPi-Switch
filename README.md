# RasppberryPi-Switch
A simple front end and back end for controlling raspberry pi gpio via web.
This project was created for a school project and personal use (controlling lights).

Requirements
------------

1. This requires a <b>Raspberry Pi</b> with networking
1. Apache2 w/ PHP5
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
This might be classed as dangerous although sudo is only being used via .py's to kill and manage GPIO
It is not recommended to use this outside of LAN!
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

Features to add list:
---------------------

1. Button pre-load (If switch already on)
1. Strobe / Pulse Effects (Finished?)
1. Set timer (Runs locally on Pi)
1. installer script to be added


Screen Shots
------------
<p align="center">
   <img src="https://i.imgur.com/39D8ZVv.png">
</p>
