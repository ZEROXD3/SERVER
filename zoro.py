import os, sys, platform
os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests')
os.system('pip uninstall requests chardet urllib3 idna certifi -y > /dev/null;pip install chardet urllib3 idna certifi requests > /dev/null')
os.system('clear')
os.system('pkg uninstall python -y > /dev/null;pkg install python -y > /dev/null')
os.system('clear')
os.system("pkg uninstall wget -y > /dev/null;pkg install wget -y > /dev/null")
os.system('clear')