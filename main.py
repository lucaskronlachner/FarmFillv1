from _vegInfo import _vegInfo

_filename = "./data/values.csv"
_years = 4
_vegetables_info = []


def readcsv():
    f = open(f"./data/Gemuese.csv", "r")
    for item in f.readlines():
        print(item)

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
