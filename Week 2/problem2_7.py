def problem2_7():
    a = input("Enter length of side one: ")
    b = input("Enter length of side two: ")
    c = input("Enter length of side three: ")
    s = .5 * (float(a) + float(b) + float(c))
    area = (float(s) * (float(s) - float(a)) * (float(s) - float(b)) * (float(s) - float(c))) ** 0.5
    print("Area of a triangle with sides " + str(float(a)) + " " + str(float(b)) + " " + str(float(c)) + " is " + str(area))

problem2_7()