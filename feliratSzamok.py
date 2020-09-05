# ./usr/bin/env python
# -*- Coding:utf-8 -*-
# Mikros feliratokhoz szukseges szamok darab-darab

#Deklaracio
adatok = []
path = "betuk.txt"

#Main
print("Add meg a feliratokat es hogy hany darab szukseges!")

"""
i = input("Felirat darab szama:")
felirat = input("Felirat:")
print(f"Megadott felirat es ahany darab kell belole: {felirat} - {i} db")
feliratOsszes = append( felirat,i )
"""

counter_dict = {}
with open(path) as ff:
    for line in ff:
        line = line.strip()
        text, count = line.split(";")
        text = text.upper()
        count = int(count)
        char_list = list(text)
        for char in char_list:
            if char in counter_dict:
                counter_dict[char] += count 
            else:
                counter_dict[char] = count

print(counter_dict)


