#!/usr/bin/python
#为所有重要文件创建备份的程序



#Filename: backup_ver1.py
import os;
import time;

#1.The files and directories to be backed up are specified in a list.
#source = ['/home/CleanSky/tcl', '/home/CleanSky/workspace'];
source = [r'C:\\test'];
#If you are using Windows, use source = [r'C:\Documents', r'D:\Work'] or something like that

#2.The backup must be stored in a main backup directory.
target_dir = r'C:\\';#Remember to change this to what you will be using

#3.The files are backed up into a zip file.
#4.The name of the zip archive is the current date and time.
target_dir = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip';

#5.We use the rar command to put the files in a zip archive.
zip_command = "Rar.exe a %s %s" %(target_dir, source);

#Run the backup
if os.system(zip_command) == 0:
    print("Successful backup to", target_dir);
else:
    print("Backup Failed");
