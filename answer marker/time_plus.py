# -*- coding: utf-8 -*-
from datetime import datetime
'''add time string by format
	paramater
	----------
	FMT : string
		the format string of time string
	time_str1 : string
	time_str2 : string
'''
def time_str_plus(FMT, time_str1, time_str2):
	time_zero = datetime.strptime('00:00:00', '%H:%M:%S')
	temp_time = datetime.strptime(time_str1, FMT)
	temp_delta = datetime.strptime(time_str2, FMT) - time_zero
	temp_time += temp_delta
	final_time_str = temp_time.strftime(FMT)

	return final_time_str
