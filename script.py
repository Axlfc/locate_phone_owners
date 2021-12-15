#!/usr/bin/env python3

import pandas as pd

df = pd.read_excel (r'Consum mobils del 2002 al 20073.xlsx')
column_headers = df.columns.ravel()

a_column = df[column_headers[0]].tolist()
c_column = df[column_headers[2]].tolist()

#unique_index = pd.Index(c_column)
index_list = []
c = 1
for i in c_column:
    i = str(i)
    i_list = i.split()
    for j in i_list:
        if j == "Telefon" or j == "Telèfon" or j == "Telefón" or j == "Tèlf":
            #print("eureka")
            if i_list[1] == "Mobil" or i_list[1] == "Mòbil":
                #print(i_list[2])
                # Here we need to find the index of the current line
                index = c_column.index(i)
                #print("El contingut de la casella A és: " + str(a_column[index]))

                print("Index del telèfon " + str(i_list[2]) + ": " + str(index + 2) + " i pertany a " + str(i_list[3:]))
            #else:
                # Telèfons no mòbils
                #print(i_list[1])
        elif j == "Telèf.Mòbil":
            #print(i_list[1])
            #print("holaaaa" + str(index + 2))
            print("Index del telèfon " + str(i_list[1]) + ": " + str(index + 2))

    '''
    for j in line:
        if "Telefon" in str(j):
            print("aleluya")'''
    #index_list.append(unique_index.get_loc(str(i)))
    c+=1
