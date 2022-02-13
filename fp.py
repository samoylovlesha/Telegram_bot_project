import imp
import json
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from pjson import pjson

def fp(gPlace=""):

    fileObject = open("data.json", "r",encoding="UTF-8")
    jsonContent = fileObject.read()
    ListOfItem = json.loads(jsonContent)
    nList=[]
    for item in ListOfItem:
        a = fuzz.WRatio(item['place'], gPlace)
        item['ratio']=a
        # print(a)
        nList.append(item)   
    str1=""
    for item in nList:
        if item['ratio']>=85:
            str1+=pjson(item)+'\n\n'
    return str1

if __name__ == '__main__':
    l=fp("Университет")
    print(l)