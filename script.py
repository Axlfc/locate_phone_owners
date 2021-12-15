#!/usr/bin/env python3

import pandas as pd


df = pd.read_excel (r'Consum mobils del 2002 al 20073.xlsx')
column_headers = df.columns.ravel()

a_column = df[column_headers[0]].tolist()
c_column = df[column_headers[2]].tolist()

index_list = []

for i in a_column:
    i = str(i)
    i_list = i.split()
    for j in i_list:
        if j != "nan" and j.isdigit():
            index = a_column.index(i)
            index_list.append(str(index))

mobile_phone_list=[]
for n in index_list:
    mobile_phone_list.append(c_column[int(n)].split())

for i in mobile_phone_list:
    if i[0] == "Telefon" or i[0] == "Telèfon" or i[0] == "Telefón" or i[0] == "Tèlf":
        tlf = str(i[1])
        if tlf == "Mobil" or tlf == "Mòbil":
            if len(str(i[2])) == 9 and int(str(i[2])[0]) != 9:
                print(str(i[2]) + ":\t" + str(i[3:]))
                print()
        else:
            if len(str(i[1])) == 9 and int(str(i[1])[0]) != 9:
                print(str(i[1]) + ":\t" + str(i[2:]))
                print()
    elif i[0] == "Telèf.Mòbil":
        print(str(i[1]) + ":\t" + str(i[2:]))
        print()
