

_filename = "./data/values.csv"


_vegetables_info = []


def readcsv():
    f = open(f"{_filename}", "r")
    for item in f.readlines():
        print(item)

readcsv()
