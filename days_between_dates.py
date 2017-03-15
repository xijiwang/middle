#input  : year1, month1, day1, year2, month2, day2
#output : Number of days between the two dates
def is_leap_year(y):
	if y % 4 == 0:
		return True
	else:
		return False

days_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
days_in_month_of_leap_year = [0,31,29,31,30,31,30,31,31,30,31,30,31]

def days_between_dates(y1,m1,d1,y2,m2,d2):
	temp = 0
	yrs = 0
	temp_year = 0
	if y1 != y2:
		if is_leap_year(y1) == True:
			temp = days_in_month_of_leap_year[m1] - d1 + 1
			i = m1 + 1
			while i < 13:
				temp += days_in_month_of_leap_year[i]
				i += 1
		else:
			temp = days_in_month[m1] - d1 + 1
			i = m1 + 1
			while i < 13:
				temp += days_in_month[i]
				i += 1
		yrs = y2 - y1 - 1
		temp_year = y1 + 1
		while temp_year < y2:
			if is_leap_year(temp_year) == True:
				temp += 366
			else:
				temp += 365
			temp_year += 1
		i = 1
		while i < m2:
			if is_leap_year(y2) == True:
				temp += days_in_month_of_leap_year[i]
			else:
				temp += days_in_month[i]
			i += 1
		temp += d2
	else:
		if m1 == m2:
			temp += d2 - d1
		else:
			if is_leap_year(y1) == True:
				temp += days_in_month_of_leap_year[m1] - d1 + 1
			else:
				temp += days_in_month[m1] - d1 + 1
		j = m1 + 1
		while j < m2:
			if is_leap_year(y2) == True:
				temp += days_in_month_of_leap_year[j]
			else:
				temp += days_in_month[j]
			j += 1
		





	return (temp,yrs)

# print days_between_dates(2006,5,19,2009,3,30)

# print days_between_dates(2010,6,11,2012,4,18)
#>> 677
print days_between_dates(1999,3,9,1999,12,5)
#>> 271
# print days_between_dates(2010,7,9,2033,5,4)
#>> 8335
# print days_between_dates(2004,5,19,2005,4,17)
#>> 333
# print days_between_dates(2012,6,2,2012,6,25)
#>> 23