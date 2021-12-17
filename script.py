#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import csv

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

final_mobile_phone=[]
for i in mobile_phone_list:
    if i[0] == "Telefon" or i[0] == "Telèfon" or i[0] == "Telefón" or i[0] == "Tèlf":
        tlf = str(i[1])
        if tlf == "Mobil" or tlf == "Mòbil" or tlf == "mòbil":
            i[2] = str(i[2]).replace("-", "")
            if len(str(i[2])) == 9 and int(str(i[2])[0]) != 9:
                #print(str(i[2]) + ":\t" + str(i[3:]))
                final_mobile_phone.append(str(i[2]) + ";\t" + str(i[3:]))
                #print()
            else:
                if len(str(i[2])) > 8:
                    if i[2][8].isdigit():
                        #print(str(i[2][0:9]) + ":\t" + str([i[2][9:]]))
                        final_mobile_phone.append(str(i[2][0:9]) + ";\t" + str([i[2][9:]]))
                        #print()
                    else:
                        #print(str(i[2][0:8]) + ":\t" + str([i[2][8:]]))
                        final_mobile_phone.append(str(i[2][0:8]) + ";\t" + str([i[2][8:]]))
                        #print("hello", str(i[2][0:8]))
        else:
            if len(str(i[1])) == 9 and int(str(i[1])[0]) != 9:
                #print(str(i[1]) + ":\t" + str(i[2:]))

                final_mobile_phone.append(str(i[1]) + " ;\t" + str(i[2:]))

    elif i[0] == "Telèf.Mòbil":
        #print(str(i[1]) + ":\t" + str(i[2:]))
        #i[2] = str(i[2]).replace("\"" "")
        print("holaaa", str(i[1:]))
        print("holaaaaaaaaaaaaaaaaaaaaaaaaa", str(i[1]) + ";\t" + str(i[2:]))
        final_mobile_phone.append(str(i[1]) + ":\t" + str(i[2:]))
        #print("holaa")
        #print(str(i[1]) + ": \t" + str(i[2:]))

    elif i[0].isdigit():
        #print(i[0] + ":\t" + str(i[1:]))
        print("deew", str(i[0:]))
        final_mobile_phone.append(str(i[0]) + ":\t" + str(i[1:]))

#print(final_mobile_phone)

with open('employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in final_mobile_phone:
        employee_writer.writerow([i])
