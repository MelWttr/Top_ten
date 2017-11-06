from xml.etree import ElementTree as Et
import chardet
import re
import string
import collections


def decoding_xml(file_name):
    with open(file_name, "rb") as f:
        file = f.read()
        res = chardet.detect(file)
        file2 = file.decode(res["encoding"])
        xml_file = Et.fromstring(file2)
    return xml_file


def get_info(xml_file):
    description = ""
    for i in xml_file:
        for j in i:
            if j.tag == "item":
                for d in j:
                    if d.tag == "description":
                        description = d.text
    return description


def string_parsing(text):     # Убирает пунктуацию из текста
    text = re.sub("<br>", "", text)
    regexp = '[{}]*'.format(string.punctuation)
    return re.sub(regexp, "", text)


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
        s = "newsafr.xml"
    elif country == "Кипр":
        s = "newscy.xml"
    elif country == "Франция":
        s = "newsfr.xml"
    elif country == "Италия":
        s = "newsit.xml"
    print_result(top_ten(string_parsing(get_info(decoding_xml(s)))))
