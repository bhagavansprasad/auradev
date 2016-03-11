#!/bin/sh
set -v

echo "Installing clamav-freshclam..."
sudo apt-get -y install clamav-freshclam 
if [ "$?" != "0" ]; then
    echo "[Error] Installing package 'clamav-freshclam'!" 1>&2
    exit 1
fi

echo "\nInstalling iptables..."
sudo apt-get -y install iptables
if [ "$?" != "0" ]; then
    echo "[Error] Installing package 'iptables'!" 1>&2
    exit 1
fi


echo "\nInstalling privoxy..."
sudo apt-get -y install privoxy
if [ "$?" != "0" ]; then
    echo "[Error] Installing package 'privoxy'!" 1>&2
    exit 1
fi

echo "\nInstalling dansguardian..."
sudo apt-get -y install dansguardian
if [ "$?" != "0" ]; then
    echo "[Error] Installing package 'dansguardian'!" 1>&2
    exit 1
fi

echo "Configuring  privoxy.../etc/privoxy/config"
sudo cp /etc/privoxy/config /etc/privoxy/config-bak
if [ "$?" != "0" ]; then
    echo "[Error] cp /etc/privoxy/config /etc/privoxy/config-bak'!" 1>&2
    exit 1
fi

sudo sed -i 's/listen-address localhost:8118/listen-address 127.0.0.1:8118/g' /etc/privoxy/config
if [ "$?" != "0" ]; then
    echo "[Error] sed -i 's/listen-address localhost:8118/listen-address 127.0.0.1:8118/g' /etc/privoxy/config'!" 1>&2
    exit 1
fi
echo "Finishded configuring  privoxy..."
echo "\nRestarting privoxy"
sudo service privoxy force-reload
if [ "$?" != "0" ]; then
    echo "[Error] In reloading privoxy!" 1>&2
    exit 1
fi

echo "Configuring  dansguardian /etc/dansguardian/dansguardian.conf"
sudo cp /etc/dansguardian/dansguardian.conf /etc/dansguardian/dansguardian.conf-bak
if [ "$?" != "0" ]; then
    echo "[Error] In configuring  /etc/dansguardian/dansguardian.conf!" 1>&2
    exit 1
fi

sudo sed -i 's/UNCONFIGURED - Please remove this line after configuration/#UNCONFIGURED - Please remove this line after configuration/g' /etc/dansguardian/dansguardian.conf
sudo sed -i 's/proxyport = 3128/proxyport = 8118/g' /etc/dansguardian/dansguardian.conf
echo "Finishded configuring  dansguardian..."
echo "\nRestarting dansguardian"
sudo service dansguardian start
if [ "$?" != "0" ]; then
    echo "[Error] In restarting service dansguardian!" 1>&2
    exit 1
fi

sudo echo "\nSettingup iptables"
sudo iptables -A OUTPUT -m owner --uid-owner root -j ACCEPT
sudo iptables -A OUTPUT -p tcp -m multiport --dports 80,443 -m owner --uid-owner privoxy -j ACCEPT
sudo iptables -A OUTPUT -p tcp -m multiport --dports 80,443 -j DROP
sudo iptables -A OUTPUT -o lo -p tcp --dport 8118 -m owner --uid-owner dansguardian -j ACCEPT
sudo iptables -A OUTPUT -o lo -p tcp --dport 8118 -m owner --uid-owner pi -j ACCEPT
sudo iptables -A OUTPUT -o lo -p tcp --dport 8118 -j DROP
sudo bash -c "sudo iptables-save > /etc/dansguardian/iptables.save"
echo "\nSaved iptables to /etc/dansguardian/iptables.save"

sudo cp /etc/rc.local /etc/rc.local-bak
sudo sed -i "/exit 0/d" /etc/rc.local

sudo sh -c "echo iptables-restore /etc/dansguardian/iptables.save >> /etc/rc.local"
sudo sh -c "echo exit 0 >> /etc/rc.local"

sudo echo "# Rules for Dansguardian

-A ufw-before-output -m owner --uid-owner root -j ACCEPT
-A ufw-before-output -p tcp -m multiport --dports 80,443 -m owner --uid-owner privoxy -j ACCEPT
-A ufw-before-output -p tcp -m multiport --dports 80,443 -j DROP
-A ufw-before-output -o lo -p tcp -m tcp --dport 8118 -m owner --uid-owner dansguardian -j ACCEPT
-A ufw-before-output -o lo -p tcp -m tcp --dport 8118 -m owner --uid-owner USER -j ACCEPT
-A ufw-before-output -o lo -p tcp -m tcp --dport 8118 -j DROP
-A ufw-before-output -o lo -j ACCEPT

# don't delete the 'COMMIT' line or these rules won't be processed
COMMIT
" >> /etc/ufw/before.rules

sudo echo "# Archives & packages
.bz2
.gz
.tbz2
.tar
.deb
.gpg" >>  /etc/dansguardian/lists/exceptionextensionlist

