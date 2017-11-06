import json
import chardet
import re
import string
import collections


def decoding_json(file_name):

    with open(file_name, "rb") as f:
        file = f.read()
        res = chardet.detect(file)
        file2 = file.decode(res["encoding"])
        jason = json.loads(file2)
        return jason


def json_to_str(file):
    jason_str = ""
    for i in file["rss"]["channel"]["items"]:
        jason_str += i["description"] + " "
        jason_str = jason_str.strip()
    return jason_str


def string_parsing(text):                       # Убирает пунктуацию из текста
    regexp = '[{}]*'.format(string.punctuation)
    return re.sub(regexp, '', text)


def top_ten(text):                             # Возвращает список 10 самых популярных слов
    words = text.split()
    words_new = []
    for word in words:
        if len(word) > 6:
            words_new.append(word.lower())
    words = collections.Counter(words_new).most_common(11)
    return words


def print_result(names):                         # Печатает топ 10
    for i in range(len(names)-1):
        print("{0} - {1}".format(i+1, names[i][0]))


countries = ["Африка", "Кипр", "Франция", "Италия"]   # Основное тело
for country in countries:
    print("{0}:".format(country))
    s = ""
    if country == "Африка":
        s = "newsafr.json"
    elif country == "Кипр":
        s = "newscy.json"
    elif country == "Франция":
        s = "newsfr.json"
    elif country == "Италия":
        s = "newsit.json"
    print_result(top_ten(string_parsing(json_to_str(decoding_json(s)))))
