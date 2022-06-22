from _vegInfo import _vegInfo

_vegetables_info = []

def readcsv():
    f = open(f"./data/Gemuese.csv", "r")
    next(f)
    for line in f.readlines():
        veggieInfo = line.split(';')
        tempVeggie = _vegInfo(veggieInfo[0], veggieInfo[1], veggieInfo[2].split(','), veggieInfo[3].strip('\n').split(','))
        _vegetables_info.append(tempVeggie)
readcsv()
print(_vegetables_info[8].gdNeighboridx)