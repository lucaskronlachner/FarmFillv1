from _vegInfo import _vegInfo
import random
import numpy as np
import copy

_filename = "./data/values.csv"
_years = 4
_vegetables_info = []


def readcsv():
    f = open(f"./data/Gemuese.csv", "r")
    next(f)
    for line in f.readlines():
        veggieInfo = line.split(';')
        gdNeighbors = veggieInfo[2].split(',')
        bdNeighbors = veggieInfo[3].strip('\n').split(',')
        tempVeggie = _vegInfo(veggieInfo[0], veggieInfo[1], [int(numeric_string) for numeric_string in gdNeighbors if gdNeighbors[0] != ''], [int(numeric_string) for numeric_string in bdNeighbors if bdNeighbors[0] != ''])
        _vegetables_info.append(tempVeggie)

def createField():
    _field = []
    _file = open(f"./data/field.csv", "r")
    for item in _file.readlines():
        _splitArr = item.split(';')
        if len(_field) == 0:
            for line in _splitArr:
                line = int(line.replace('\n', ''))
                _field.append([line])
        else:
            counter = 0
            for line in _splitArr:
                line = int(line.replace('\n', ''))
                _field[counter].append(line)
                counter += 1
    return _field
    

def optimizeNeighbors(veggieId, field, row, col):
    veggie = _vegetables_info[veggieId - 1]
    #shit mit random aber keinen plan wie ma's gscheid mocht
    if ((col != 0 and row != len(field[0]) - 1) and field[row + 1][col - 1] in veggie.bdNeighboridx):
        field[row + 1][col - 1] = random.choice(veggie.gdNeighboridx)
    if ((row != len(field[0]) - 1) and field[row + 1][col] in veggie.bdNeighboridx):
        field[row + 1][col] = random.choice(veggie.gdNeighboridx)
    if (((col != len(field) - 1 and row != len(field[0]) - 1)) and field[row + 1][col + 1] in veggie.bdNeighboridx):
        field[row + 1][col + 1] = random.choice(veggie.gdNeighboridx)
    if ((col != len(field) - 1) and field[row][col + 1] in veggie.bdNeighboridx):
        field[row][col + 1] = random.choice(veggie.gdNeighboridx)
    return field

def perfection():
    _currentfld = firstTry()
    print('Before optimization')
    print(np.matrix(_currentfld))
    print()
    b = True
    while (b):
        _originalFld = copy.deepcopy(_currentfld)
        for row in range(len(_currentfld)):
            for col in range(len(_currentfld[0])):
                if _currentfld[row][col] == -1:
                    continue
                else:
                    _currentfld = optimizeNeighbors(_currentfld[row][col], _currentfld, row, col)
        print(_originalFld)
        print(_currentfld)
        if(_originalFld == _currentfld):
            b = False
    print('After optimization')
    print(np.matrix(_currentfld))

def firstTry():
    _firstTryFld = createField()
    currentVeggie = 1
    for row in range(len(_firstTryFld)):
        for col in range(len(_firstTryFld[0])):
            if _firstTryFld[row][col] == -1:
                continue
            else:
                _firstTryFld[row][col] = currentVeggie
                currentVeggie = random.choice(_vegetables_info[currentVeggie - 1].gdNeighboridx)
    return _firstTryFld

readcsv()
perfection()