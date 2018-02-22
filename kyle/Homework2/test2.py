import os
import schedule
import time


def job():
	os.system("echo 'Hello World\n'")

schedule.every(1).minutes.do(job)

while True:
	schedule.run_pending()
	time.sleep(1)
