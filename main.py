
_filename = "./data/values.csv"

def readcsv():
    f = open(f"{_filename}", "r")
    for item in f.readlines():
        print(item)

readcsv()
