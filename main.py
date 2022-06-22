from _vegInfo import _vegInfo

_filename = "./data/values.csv"
_years = 4
_vegetables_info = []


def readcsv():
    f = open(f"./data/Gemuese.csv", "r")
    next(f)
    for line in f.readlines():
        veggieInfo = line.split(';')
        tempVeggie = _vegInfo(veggieInfo[0], veggieInfo[1], veggieInfo[2].split(','), veggieInfo[3].strip('\n').split(','))
        _vegetables_info.append(tempVeggie)

def createField():
    _field = []
    _file = open(f"./data/field.csv", "r")
    for item in _file.readlines():
        _splitArr = item.split(';')
        if len(_field) == 0:
            for line in _splitArr:
                line = line.replace('\n', '')
                _field.append([line])
        else:
            counter = 0
            for line in _splitArr:
                line = line.replace('\n', '')
                _field[counter].append(line)
                counter += 1
    return _field


readcsv()
print(_vegetables_info[8].gdNeighboridx)