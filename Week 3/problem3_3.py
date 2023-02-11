months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

def problem3_3(month, day, year):
    print(months[month-1] + " " + str(day) + ", " + str(year))

problem3_3(1, 16, 1993)