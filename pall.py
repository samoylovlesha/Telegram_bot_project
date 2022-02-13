import json
from pjson import pjson


def pall():
    fileObject = open("data.json", "r",encoding="UTF-8")
    jsonContent = fileObject.read()
    ListOfItem = json.loads(jsonContent)
    str1=""
    for item in ListOfItem:
        str1+=pjson(item)+"\n\n"
    
    return str1

if __name__ == '__main__':
    l=pall()
    print(l)