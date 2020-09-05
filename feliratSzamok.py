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

# characters to replace before counting
replace_dict = {"7": "L",
                "1": "I",
                "_": " "}

counter_dict = {}

with open(path) as ff:
    for line in ff:
        line = line.strip()
        text, count = line.split(";")
        count = int(count)

        # text processing
        text = text.upper()
        for orig_char, new_char in replace_dict.items():
            text = text.replace(orig_char, new_char) 
        
        for char in list(text):    
            if char in counter_dict:
                counter_dict[char] += count 
            else:
                counter_dict[char] = count

print(counter_dict)


