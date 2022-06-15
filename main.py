
def readcsv():
    f = open(f"./data/Gemuese.csv", "r")
    for item in f.readlines():
        print(item)

readcsv()
