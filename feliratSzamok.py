# ./usr/bin/env python
# -*- Coding:utf-8 -*-
# Mikros feliratokhoz szukseges szamok darab-darab

#Deklaracio
adatok = []
path = "betuk.txt"

#Main
print("A megadott feliratok (file) darabszamai:")



with open(path) as ff:

    for line in ff:

        line = line.strip()
        line = line.split(";")
        adatok.append(line)
        print(adatok)


