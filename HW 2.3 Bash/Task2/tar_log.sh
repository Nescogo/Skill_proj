#!/bin/bash/

echo "Start Backup"

cd /
echo "-------------------------------------------"
sudo tar cpNf /archive/home_backup "created on `date '+%d-%B-%Y'`.tar" /home
wait
echo "-------------------------------------------"
sudo tar cpNf /archive/var_log_backup "created on `date '+%d-%B-%Y'`.tar" /var/log
wait
echo "--------------------------------------------"
sudo tar cpNf /archive/ftp_backup "created on `date '+d%-%B-%Y'`.tar" /etc/vsftpd.conf
wait
echo "-------------------------------------------"
sudo tar cpNf /archive/ssh_backup "created on `date '+d%-%B-%Y'`.tar" /etc/ssh/sshd_config
wait
echo "-------------------------------------------"
sudo tar cpNf /archive/rdp_backup "created on `date '+d%-%B-%Y'`.tar" /etc/xrdp/xrdp.ini
