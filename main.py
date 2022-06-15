

_filename = "./data/values.csv"


_vegetables_info = []


def readcsv():
    f = open(f"./data/Gemuese.csv", "r")
    for item in f.readlines():
        print(item)

readcsv()
