import os
import sys
password=sys.argv[1]
os.popen("mysqldump -u root --password="+password+" --databases employees > dump.sql")
os.popen("pscp -pw "+password+" dump.sql facjcadmin@192.168.1.21:/home/facjcadmin/class")
os.popen("plink -pw "+password+" facjcadmin@192.168.1.21 /home/facjcadmin/class/backup "+password)