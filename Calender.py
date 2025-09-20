import calendar

y = int(input("Enter the Year: "))
m = 1
print("******Calendar******")
cal = calendar.TextCalendar(calendar.SUNDAY)
i = 1
while i <= 12:
    cal.prmonth(y, i)
    i += 1
    print("--------------------")
