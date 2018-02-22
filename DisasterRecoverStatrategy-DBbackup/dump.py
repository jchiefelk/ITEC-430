import os
import sys
password=sys.argv[1]
os.popen("mysqldump -u root --password="+password+" --databases employees > dump.sql")
