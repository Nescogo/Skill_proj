#!/bin/bash/

echo "Start Backup"
cd /
sudo tar -czpvf /archive/backup_date_`+%Y-%m-%d`.tar.gz /home /var/log /etc/vsftpd.conf /etc/ssh/sshd_config /etc/xrdp/xrdp.ini
