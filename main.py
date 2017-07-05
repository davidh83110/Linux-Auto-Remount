"""
Auto Remount S3_Shopping & S3_Web when mount point critical.

@author David
Version 1.0 , 2017-06-30

"""
#!/usr/bin/env python3
import os
import re

check_shopping = os.popen('/opt/Servers/nagios/libexec/check_file_age -w 650 -c 700 -f /S3Shopping_Content/check_mount').readlines()
check_shopping = "".join(check_shopping)

check_web = os.popen('/opt/Servers/nagios/libexec/check_file_age -w 650 -c 700 -f /S3/Web_Content/check_mount').readlines()
check_web = "".join(check_web)



status_shopping = re.findall('FILE_AGE.{5}',check_shopping)
status_web = re.findall('FILE_AGE.{5}',check_web)



status_ok = list()
status_ok = "FILE_AGE OK: "

status_critical = list()
status_critical = "FILE_AGE CRIT"



if "status_shopping".join(status_shopping) == status_ok:
    print("ok")
elif "status_shopping".join(status_shopping) == status_critical:
    umount_shopping = os.popen('umount /S3/Shopping_Content')
    mount_shopping = os.popen('mount /S3/Shopping_Content')
    mail_shopping = os.popen('echo -e "Auto mount S3_Shopping_Content Sucessfully\n`date`\n`df -kh | grep S3`" | mail -s "`hostname`:Auto mount S3_Shopping_Content Sucessfully" davidh83110@gmail.com')
else:
    mail_error = os.popen('echo -e "Program ERROR\n`date`\ndf -kh | grep S3" | mail -s "`hostname`:S3 Auto mount Program ERROR" davidh83110@gmail.com')

    
    
if "status_web".join(status_web) == status_ok:
    print("ok")
elif "status_web".join(status_web) == status_critical:
    umount_shopping = os.popen('umount /S3/Web_Content')
    mount_shopping = os.popen('mount /S3/Web_Content')
    mail_shopping = os.popen('echo -e "Auto mount S3_Web_Content Sucessfully\n`date`\n`df -kh | grep S3`" | mail -s "`hostname`:Auto mount S3_Web_Content Sucessfully" davidh83110@gmail.com')
else:
    mail_error = os.popen('echo -e "Program ERROR\n`date`\ndf -kh | grep S3" | mail -s "`hostname`:S3 Auto mount Program ERROR" davidh83110@gmail.com')

