#!/usr/bin/python

import os
import sys

password=sys.argv[1]

os.open("mysqldump -u root --password="Waterbotle3" --databases users > backup.sql")
