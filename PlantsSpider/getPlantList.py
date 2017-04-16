# coding: utf-8

# 从Symbol.csv中读入1900+个植物项

def getPlantsList():
    f = open("./CSVfile/Symbol.csv","r")
    Symbol = []

    for i in range(0,1090,1):
        Symbol[i] = f.readline()

    return Symbol