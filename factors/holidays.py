from datetime import date
import holidays
import time

def get_holidays(date):
	us_holidays = holidays.get_holidays()
	for i in range(int(time.strftime("%d")), date):
		if(date(2017, 1, 1) in us_holidays):
			print 'holiday'

get_holidays(31)