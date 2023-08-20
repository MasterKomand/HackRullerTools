/#!/usr/bin/bash
pathFile="HackRullerTools"
cd ~/../usr/bin 
#Первая команда
touch HackerRullerTools
echo "cd ~/$pathFile/ && python HackingCam.py" >  HackerRullerTools
chmod +x HackerRullerTools
#Вторая команда
touch installTools
echo "pkg install python" > installTools
chmod +x installTools
cd ~/
#конец
