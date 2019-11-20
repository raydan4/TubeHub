#!/bin/bash

# Set default mysql stuff
mysql -uroot -p$MYSQL_ROOT_PASSWORD -e "GRANT ALL PRIVILEGES ON *.* to 'root'@'%' IDENTIFIED BY '$MYSQL_ROOT_PASSWORD' with GRANT OPTION; FLUSH PRIVILEGES;"
mysql -uroot -p$MYSQL_ROOT_PASSWORD -e "CREATE DATABASE tubehub; GRANT ALL PRIVILEGES ON tubehub.* to 'tubehub'@'localhost' IDENTIFIED BY '$MYSQL_ROOT_PASSWORD'; FLUSH PRIVILEGES;"

