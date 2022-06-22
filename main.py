def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return
    
    print("Happy New Year!")

happy_new_year()

def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
#
# Your code from LAB 4.3.1.6.
#
print(is_year_leap(1900)==True)



def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
#
# Your code from LAB 4.3.1.6.
#
d_31 = [1,3,5,7,8,10,12]
d_30 = [4,6,9,11]

def days_in_month(year, month):
    if is_year_leap(year) == True and month <= 12:
        if month == 2:
            return 29
        elif month in d_31:
            return 31
        else:
            return 30
    elif month in d_31 and month <= 12:
        return 31
    elif month in d_30 and month <= 12:
        return 30
    elif is_year_leap(year) == False and month <= 12:
        if month == 2:
            return 28
    
def day_of_year(year, month, day):
    days_of_week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    for d in days_of_week:
        d[0] = day
    return d

def is_year_leap(year):
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True

def days_in_month(year, month):
	if year < 1582 or month < 1 or month > 12:
		return None
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = days[month - 1]
	if month == 2 and is_year_leap(year):
		res = 29
	return res

def day_of_year(year, month, day):
	days = 0
	for m in range(1, month):
		md = days_in_month(year, m)
		if md == None:
			return None
		days += md
	md = days_in_month(year, month)
	if day >= 1 and day <= md:
		return days + day
	else:
		return None

print(day_of_year(2016, 7, 31))


def liters_100km_to_miles_gallon(liters):
    gal = liters / 3.785411784
    miles = (100 * 1000)/ 1609.344
    total = miles / gal
    return total

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))

def miles_gallon_to_liters_100km(miles):
    km100 = miles * 1609.344 / 1000 / 100
    litres = 3.785411784
    return litres / km100
    

print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))

