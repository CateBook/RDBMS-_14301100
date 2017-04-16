# import re
"""
def block(str):
    str = str.replace('\t', '')
    str = str.replace('<br>', '')
    str = str.replace(' &nbsp; ', ' ')
    str = str.strip()
    str = str.replace('\n\n', '; ')
    return str

def WriteProfileCSV():
    f = open("./CSVfile/profile.csv","a")
    f.write('Symbol,'
            + 'Group,'
            + 'Family,'
            + 'Duration,'
            + 'Growth_Habit,'
            + 'Native_Status' + '\n')
    f.close()

def getProfileItem(content):

    Symbol_item = re.compile(r'<td valign="top"><strong>Symbol:</strong></td>.+?<td valign="top">(.+?)</td>', re.S)
    Symbol = Symbol_item.findall(content)[0]
    Group_item = re.compile(r'<td valign="top"><strong>Group:</strong></td>.+?<td valign="top">(.+?)</td>', re.S)
    Group = Group_item.findall(content)[0]
    Family_item = re.compile(r'<td valign="top"><strong>Family:</strong></td>.+?<td valign="top">(.+?)</td>',re.S)
    Family = Family_item.findall(content)[0]
    Duration_item = re.compile(r'<td valign="top"><strong>Duration:</strong></td>.+?<td valign="top">(.+?)</td>',re.S)
    Duration = Duration_item.findall(content)[0]
    Growth_Habit_item = re.compile(r'<strong>Growth.+?Habit</strong></a><strong>:</strong></td>.+?<td valign="top">(.+?)</td>', re.S)
    Growth_Habit = Growth_Habit_item.findall(content)[0]
    Native_Status_item = re.compile(r'<strong>Native.+?Status</strong></a><strong>:</strong></td>.+?<td valign="top">(.+?)</td>', re.S)
    Native_Status = Native_Status_item.findall(content)[0]

    output = open("./CSVfile/profile.csv", "a")
    output.write(
        block(Symbol) + ','
        + block(Group) + ','
        + block(Family) + ','
        + block(Duration) + ','
        + block(Growth_Habit) + ','
        + block(Native_Status) + '\n')
    output.close()
"""

import time

from getListPDFanddocx import SpiderPlants

begin = time.time()

url="https://plants.usda.gov/java/factSheet/"

plantSpider = SpiderPlants()
contentHTML = plantSpider.openUrl(url)
plantDic = plantSpider.getplantsDictionary(contentHTML)
sortedPlants = plantSpider.sortplants(plantDic)

for plant in sortedPlants:
    print plant[0], ":", plant[1]

time_cons = "%.2f" % (time.time() - begin)
print "time consumed: " + time_cons + "s"
