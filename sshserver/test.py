import schedule
import time
import os
import datetime

password = ""

timestamp = datetime.datetime.utcnow()
backupdatabase = 'backup_'+str(timestamp)
targetdatabase = 'employees'
newschema = backupdatabase+'.sql'
os.system('mysqldump '+targetdatabase+' > dump.sql  -u root -p'+password)
os.system('mysqladmin create '+ backupdatabase +' -u root -p'+password)
os.system('mysql '+backupdatabase+' < dump.sql -u root -p'+password)