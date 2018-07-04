#Allows root (needed for apt-get …)
sudo iptables -A OUTPUT -m owner --uid-owner root -j ACCEPT

#Allows privoxy to connect to ports 80 and 443 
sudo iptables -A OUTPUT -p tcp -m multiport --dports 80,443 -m owner --uid-owner privoxy -j ACCEPT

#Blocks everyone but privoxy 
sudo iptables -A OUTPUT -p tcp -m multiport --dports 80,443 -j DROP

#Allows dansguardian to connect to privoxy.
sudo iptables -A OUTPUT -o lo -p tcp --dport 8118 -m owner --uid-owner dansguardian -j ACCEPT

#Allows USER (parents) to connect to privoxy thus circumventing dansguardian.
#don't use if shared computer. Change to “USER” to your log in name, and add
#additional users if needed, one per line, before you add the last “DROP” line.
sudo iptables -A OUTPUT -o lo -p tcp --dport 8118 -m owner --uid-owner bhagavan -j ACCEPT

#Blocks all other connections to privoxy. 
sudo iptables -A OUTPUT -o lo -p tcp --dport 8118 -j DROP

#Bhagavan
#Add rule to drop google play app to go out
#Google Play uses TCP and UDP 5228 port
sudo iptables -A OUTPUT -p tcp -m multiport --dports 80,443 -j DROP

