#!/usr/bin/env python
# coding: utf-8




from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import argparse
import os





# аргументы для командной строки
parser = argparse.ArgumentParser(description='Сбор данных в таблицу')
parser.add_argument('indir', type=str, help='Ссылка на список')
args = parser.parse_args()
# аргументы переданы из командной строки
doc = args.indir
page = requests.get(doc)
# вывод кода состояния протокола HTTP
print(page.status_code)
soup = BeautifulSoup(page.text, "html.parser")
a = soup
# перевод HTML-кода в текст для регулярных выражений
b = a.text





# регулярное выражения для сбора ФИО жертв
o = re.findall(r'\b[А-Я](?!НИГИ)(?!омиссара)(?!ЕЙТЕНАНТУ)(?!ОИМЕННО)(?!ОВЕРШЕННО)(?!АРКОМА)(?!аркома)(?!енерального)(?!рокурора)(?!оенн)(?!ерковь)(?!оллег)(?!рхив)\w+.[А-Я](?![А-Я])(?!оенн)(?!риста)(?!ресвятой)(?!АССР)\w+\s[А-Я](?![А-Я])(?!оллег)(?!оюза)(?!овета)(?!скусства)(?!еркви)(?!АССР)(?!еспублики)(?!аулио)(?!нненский)(?!ессинг)(?!ревениц)(?!ильдер)(?!льриха)\w+\b', b)
data_names = pd.Series(o)
# шаблон для поиска подписавших
e = re.search(r'подписью', b)
if e is not None:
    dot2 = b.find(".", e.end())
    r = [b[e.end():dot2]]
else:
    r = ["NaN"]
Signature = pd.Series(r)
# шаблон для поиска организаций
q = re.search(r'рхив', b)
if q is not None:
    dot2 = b.find("\n", q.end())
    w = ["архив" + b[q.end():dot2]]
else:
    w = ["NaN"]
Organisation = pd.Series(w)




# шаблон для поиска ФИО палача
p = re.search(r'Исполнитель', b)
if p is not None:
    dot = b.find(".", p.end())
    title_of_the_excutioner = b[p.end()+3:dot]
else:
    title_of_the_excutioner = ["NaN"]
data_title_of_the_excutioner = pd.Series(title_of_the_excutioner)
# шаблон для поиска образования палача
n = re.search(r'Образование', b)
if n is not None:
    dot1 = b.find("\n", n.end())
    education = b[n.end()+3:dot1]
else:
    education = ["NaN"]
data_education = pd.Series(education)
# шаблон для поиска присутствоваших
c = re.search(r'ПРИСУТСТВОВАЛИ', b)
if c is not None:
    dot2 = b.find("\n", c.end())
    Attended = b[c.end()+2:dot2]
else:
    Attended = ["NaN"]
data_attended = pd.Series(Attended)
# регулярное выражение для сбора дат расстрела и приговора
c = re.findall(r'\d{1,2}\s\w{3,8}\s\d{4}\s\w{4}', b)
if c[0] == c[1]:
    shot = []
    shot.append(c[0])
    sentence = ["NaN"]
    sentence_date = pd.Series(sentence*len(data_names))
    shot_date = pd.Series(shot*len(data_names))
else:
    sentence = []
    shot = []
    sentence.append(c[0])
    sentence_date = pd.Series(sentence*len(data_names))
    shot.append(c[1])
    shot_date = pd.Series(shot*len(data_names))




# вся собранная информация объединена в датафрейм
df = pd.DataFrame({'ФИО': data_names, 'Дата расстрела': shot_date, 'Дата приговора': sentence_date, 'ФИО и звание палача': data_title_of_the_excutioner, 'Уровень образования палача': data_education, 'Присутствовали': data_attended, 'Подпись': Signature, 'Организация': Organisation})
df





# сохранение данных
writer = pd.ExcelWriter('Total.xlsx')
df.to_excel(writer, 'Sheet1')
writer.save()
filename = "Total.xlsx"
a = os.getcwd()
print("Your file is", a+'/'+filename)

