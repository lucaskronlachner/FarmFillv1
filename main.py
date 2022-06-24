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
    return _currentfld

def getAllZieher(type):
    vegs = []
    for item in _vegetables_info:
        if type.__contains__(item.fruchtflg):
            vegs.append(item)

    return vegs

def containsType(type,row, col, yearflds):
    for item in yearflds:
        veg = _vegetables_info[item[row][col] - 1]
        if veg.fruchtflg == type:
            return True
    return False

def timeGoesBy(_startfld):
    _yearflds = []
    for _ in range(0, _years):
        _currfield = createField()
        for row in range(len(_startfld)):
            for col in range(len(_startfld[0])):
                if _startfld[row][col] != -1:
                    item = _vegetables_info[_startfld[row][col] - 1]
                    if item.fruchtflg == 'Starkzehrer':
                        _currfield[row][col]  = random.choice(getAllZieher('Mittelzehrer,Schwachzehrer'))
                    elif item.fruchtflg == 'Mittelzehrer':
                        if containsType('Starkzehrer',row, col, _yearflds):
                            _currfield[row][col]  = random.choice(getAllZieher('Starkzehrer,Schwachzehrer'))
                        else:
                            _currfield[row][col]  = random.choice(getAllZieher('Schwachzehrer'))
                    elif item.fruchtflg == 'Schwachzehrer':
                        if containsType('Starkzehrer',row, col, _yearflds):
                            _currfield[row][col] = random.choice(getAllZieher('Starkzehrer,Mittelzehrer'))
                        else:
                            _currfield[row][col]  = random.choice(getAllZieher('Mittelzehrer'))
    return _yearflds



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