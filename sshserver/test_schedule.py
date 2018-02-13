import schedule
import time
import os
import datetime

password = "'jchie4445'"

def job():

	timestamp = datetime.datetime.utcnow()
	backupdatabase = 'backup_'+str(timestamp)
	targetdatabase = 'employees'
	newschema = backupdatabase+'.sql'
	os.system('mysqldump '+targetdatabase+' > dump.sql  -u root -p'+password)
	os.system('mysqladmin create '+ backupdatabase +'-u root -p'+password)
	os.system('mysql '+backupdatabase+' < dump.sql -u root -p'+password)

schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)