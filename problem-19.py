def is_century(year):
	return year % 100 == 0

def is_leap_year(year):
	if is_century(year):
		return year % 400 == 0 
	else:
		return year % 4 == 0

def get_day_count(year, month):
	if month == 2 and is_leap_year(year):
		return 29
	elif month == 2:
		return 28
	elif month in [4, 6, 9, 11]:
		return 30
	else:
		return 31

def solution(start_day, start_month, start_year, end_day, end_month, end_year):
	current_day, current_month, current_year = start_day, start_month, start_year
	days = 0
	sundays = 0
	
	while current_day != end_day or current_month != end_month or current_year != end_year:
		if days % 7 == 0 and current_day == 1:
			sundays += 1

		days += 1

		if current_day == get_day_count(current_year, current_month):
			current_day = 1
			if current_month == 12:
				current_month = 1
				current_year += 1
			else:
				current_month += 1
		else:
			current_day += 1
	
	return sundays

print(solution(1, 1, 1901, 31, 12, 2000))
