months = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}

def problem3_4(mon, day, year):
    print(str(months[mon]) + "/" + str(day) + "/" + str(year))

problem3_4("January", 16, 1993)