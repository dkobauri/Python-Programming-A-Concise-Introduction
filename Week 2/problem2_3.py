newEngland = ["Maine","New Hampshire","Vermont", "Rhode Island", 
"Massachusetts","Connecticut"]

def problem2_3(ne):
    for item in ne:
        print(str(item) + " has " + str(len(item)) + " letters.")

problem2_3(newEngland)