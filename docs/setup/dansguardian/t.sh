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
