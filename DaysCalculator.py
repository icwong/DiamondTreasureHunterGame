###### DESCRIPTION: This program will help calculate the how many days has passed between the two dates.

print "Please provide the first (earliest) date:" #FIRST DATE
print
year = int(raw_input("State a year (between 1901 and 2099 inclusive): "))
month = int(raw_input("State a month (between 1 and 12 inclusive): "))
day = int(raw_input("State a day (between 1 and 30 inclusive): "))

firstdate = str(year) + "," + str(month) + "," + str(day) #YEAR,MONTH,DAY
print firstdate
print

print "Plese provide the second (latest) date:" #SECOND DATE
yearr = int(raw_input("State a year (between 1901 and 2099 inclusive): "))
monthh = int(raw_input("State a month (between 1 and 12 inclusive): "))
dayy = int(raw_input("State a day (between 1 and 30 inclusive): "))

seconddate = str(yearr) + "," + str(monthh) + "," + str(dayy) #YEAR,MONTH,DAY (2)
print seconddate
print
print "First Result"
print "*" * 15
print
print "The number of days since 1901,1,1 to... :"
           
calc = 360 * (year - 1901) + 30 * (month - 1) + day - 1 #YEAR TO DAY
calcc = 360 * (yearr - 1901) + 30 * (monthh - 1) + dayy - 1 #YEAR TO DAY (2)
cc = calcc - calc #DIFF. BETWEEN TWO DATES

print firstdate,
print "is:", calc

print seconddate,
print "is:", calcc
print
print "Second Result"
print "*" * 15
print
print "The difference in days is:", cc
print    
print "Third and (and last) result"
print "*" * 15
print

diff_years= cc/ 360
months = cc % 360
diff_months = months / 30
diff_days = months % 30

print "The difference in days is expressible also as:",
print diff_years,
print "years,",
print diff_months,
print "months,",
print diff_days,
print "days",



           

