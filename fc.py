import imp
import json
from pjson import pjson
import re

def fc(minc,maxc):
    # print(minc)
    # print(maxc)
    minc=int(minc)
    maxc=int(maxc)
    fileObject = open("data.json", "r",encoding="UTF-8")
    jsonContent = fileObject.read()
    ListOfItem = json.loads(jsonContent) 
    str1=""
    for item in ListOfItem:
        cost=re.findall(r'[\d]+', item['cost'])[0]
        cost=int(cost)
        # print(cost)
        if cost>=minc and cost<=maxc:
            str1+=pjson(item)+'\n\n'
    print(str1)
    if str1=="":
        str1= "Ничего не найдено..."
    return str1

if __name__ == '__main__':
    l=fc(50,150)
    print(l)
    # word="300р. в час"
    # l = re.findall(r'[\d]+', word)[0]
    # print(l)