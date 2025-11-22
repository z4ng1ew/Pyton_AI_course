
#  Программа для отдела, который занимается выдачей загранпаспортов

def longest_unique_substr(text):
    curr = ""
    pos = 0
    while pos < len(text):
        if text[pos] in curr:
            break
        curr += text[pos]
        pos += 1
    if pos == len(text):
        return curr
    tail = longest_unique_substr(text[1:])
    return tail if len(tail) > len(curr) else curr

print(longest_unique_substr("abcdefab"))
print(longest_unique_substr("sssssss"))
print(longest_unique_substr("abcabcbb"))







# Программа, которая возвращает самую длинную неповторяющуюся подстроку для входной строки.


text = input("Введите ФИО:\n")

translit = {
    "А": "A",  "а": "a",
    "Б": "B",  "б": "b",
    "В": "V",  "в": "v",
    "Г": "G",  "г": "g",
    "Д": "D",  "д": "d",
    "Е": "E",  "е": "e",
    "Ё": "E",  "ё": "e",
    "Ж": "Zh", "ж": "zh",
    "З": "Z",  "з": "z",
    "И": "I",  "и": "i",
    "Й": "I",  "й": "i",
    "К": "K",  "к": "k",
    "Л": "L",  "л": "l",
    "М": "M",  "м": "m",
    "Н": "N",  "н": "n",
    "О": "O",  "о": "o",
    "П": "P",  "п": "p",
    "Р": "R",  "р": "r",
    "С": "S",  "с": "s",
    "Т": "T",  "т": "t",
    "У": "U",  "у": "u",
    "Ф": "F",  "ф": "f",
    "Х": "Kh", "х": "kh",
    "Ц": "Ts", "ц": "ts",
    "Ч": "Ch", "ч": "ch",
    "Ш": "Sh", "ш": "sh",
    "Щ": "Shch", "щ": "shch",
    "Ъ": "Ie", "ъ": "ie",
    "Ы": "Y",  "ы": "y",
    "Ь": "",   "ь": "",
    "Э": "E",  "э": "e",
    "Ю": "Iu", "ю": "iu",
    "Я": "Ia", "я": "ia",
}

result = "".join(translit.get(char, char) for char in text)
print(result)