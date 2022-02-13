import json

def pjson(item):
    str1="Описание вакансии: "+ item['desc'] + " Метро: " + item['place'] + ""\
        " Оплата: " + item['cost'] + " Контактное лицо: " + item['name'] + ""\
        " Контактный телефон: " + item['tel'] + " e-mail: " + item['e-mail'] 
    return str1


if __name__ == '__main__':
    fileObject = open("data.json", "r",encoding="UTF-8")
    jsonContent = fileObject.read()
    ListOfItem = json.loads(jsonContent)
    item=ListOfItem[0]
    a=pjson(item)
    print(a)
