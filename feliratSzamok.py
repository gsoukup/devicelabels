# !/usr/bin/env python
# -*- Coding:utf-8 -*-
# Mikros feliratokhoz szukseges szamok darab-darab

import argparse #to write user-friendly command-line interfaces

parser = argparse.ArgumentParser()
parser.add_argument("filepath", help="Feliratok es darab szam fajl.")
args = parser.parse_args()

#Deklaracio
adatok = []
path = args.filepath

#Main
print(f"A megadott feliratokhoz ({path}) szukseges karakterek:")

"""
i = input("Felirat darab szama:")
felirat = input("Felirat:")
print(f"Megadott felirat es ahany darab kell belole: {felirat} - {i} db")
feliratOsszes = append( felirat,i )
"""

# characters to replace before counting, same character at manufacturer
replace_dict = {"7": "L",
                "1": "I",
                "_": " "}
# Counter container, 'Char' : amount
counter_dict = {}

with open(path) as ff:
    for line in ff:
        line = line.strip()                 # stripping line ending /n
        text, count = line.split(";")       # separating the data given,
        count = int(count)                  # conversion

        # text processing
        text = text.upper()                 # only upperscale letters
        for orig_char, new_char in replace_dict.items(): # looping through replace dictionary, making local variables
            text = text.replace(orig_char, new_char)     # from keys:values
        
        for char in list(text):             # for loop on strings with a given variable means the closest lower object
            if char in counter_dict:        # the characters
                counter_dict[char] += count # specific characters count from path
            else:
                counter_dict[char] = count  # new character

print(counter_dict)                         # printing the result


