#!/bin/bash
#1
read -p "Enter your name: " answer
echo "Hello, $answer! Let's start our journey"
echo "------------------------------------------------------------"
#2
sudo apt-get install sl
sl
wait
#3
string1=`sudo apt-cache -qq pkgnames ruby-backports | awk '{print $1}' | head -1`
#4
sudo apt-get update && apt-get upgrade
#package install
for iteration in  apache2 python3 openssh-server 
do sudo apt-get install $iteration; done
echo "------------------------------------------------------------"
#5
if [ $string1 != 'ruby-backports' ] 
then sudo apt-get install ruby-backports 
else echo "Backports already installed"; fi
#6
echo "------------------------------------------------------------"
echo "Apache start"
sudo systemctl enable --now apache2
#7
echo "------------------------------------------------------------"
echo "Openssh start"
sudo systemctl enable --now ssh
#8
echo "------------------------------------------------------------"
echo "System info"
sudo lshw -short
echo "------------------------------------------------------------"
#9
while true; do
	read -p  "Do you want to see the weather forecast? Y/N " answer
	case $answer in
		[Yy]* )	read -p "Write City name:"  answer1
			curl -H "Accept-Language:ru" ?0 wttr.in/$answer1
			break;;
		[Nn]* ) echo "You choose NO"; break;;
		* ) echo "Please answer yes or no";;
	esac
done
#10
echo "-----------------------------------------------------------"
while true; do
	read -p "Do you want to know the current exchange rate to RUB? Y/N "  answer
	case $answer in
		[Yy]* ) read -p  "Write currency code: " answer1
			curl 'https://www.cbr-xml-daily.ru/daily_json.js' > curr
			cat curr | jq .Valute.$answer1.Value
			break;;
		[Nn]* ) echo "You choose NO"; break;;
		* ) echo "Please answer yes or no";;
	esac
done

