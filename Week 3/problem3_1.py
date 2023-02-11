def problem3_1(txtfilename):
    Sum = 0
    infile = open(txtfilename)
    for line in infile:
        print(line, end="")
        Sum += len(line)
    print("")
    print("")
    print("There are " + str(Sum) + " letters in the file.")
    infile.close()

problem3_1("Week 3\HumptyDumpty.txt")