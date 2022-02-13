#pip install fuzzywuzzy
#pip install python-Levenshtein
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

sList=["Университет","Проспект Вернадского", "Юго-западная"]
# a = process.extractOne("Вернадского", sList)
# a = a[0]
# print(a)

a = fuzz.WRatio('Привет наш мир', '!ПриВЕт, наш мир!')
print(a)
#https://habr.com/ru/post/491448/