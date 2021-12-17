#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import csv

def read_excel():
    #df = pd.read_excel(r'Consum mobils del 2002 al 20073.xlsx')
    df = pd.read_excel(r'Consum mobils del 2008 al 2019.xlsx')
    return df


def read_column(excel_obj, num_column):
    column_headers = excel_obj.columns.ravel()
    return excel_obj[column_headers[num_column]].tolist()


def write_iterations_through_column(name_column):
    list_index = []
    for i in name_column:
        i = str(i)
        i_list = i.split()
        for j in i_list:
            if j != "nan" and j.isdigit():
                index = name_column.index(i)
                list_index.append(str(index))
    return list_index

def write_final_iterations_though_excel():
    final_mobile_phone = []
    for i in mobile_phone_list:
        if i[0] == "Telefon" or i[0] == "Telèfon" or i[0] == "Telefón" or i[0] == "Tèlf":
            tlf = str(i[1])
            if tlf == "Mobil" or tlf == "Mòbil" or tlf == "mòbil":
                i[2] = str(i[2]).replace("-", "")
                if len(str(i[2])) == 9 and int(str(i[2])[0]) != 9:
                    final_mobile_phone.append(str(i[2]) + ";\t" + str(i[3:]))
                else:
                    if len(str(i[2])) > 8:
                        if i[2][8].isdigit():
                            final_mobile_phone.append(str(i[2][0:9]) + ";\t" + str([i[2][9:]]))
                        else:
                            final_mobile_phone.append(str(i[2][0:8]) + ";\t" + str([i[2][8:]]))
            else:
                if len(str(i[1])) == 9 and int(str(i[1])[0]) != 9:
                    final_mobile_phone.append(str(i[1]) + " ;\t" + str(i[2:]))
        elif i[0] == "Telèf.Mòbil":
            final_mobile_phone.append(str(i[1]) + ":\t" + str(i[2:]))
        elif i[0].isdigit():
            final_mobile_phone.append(str(i[0]) + ":\t" + str(i[1:]))
    return final_mobile_phone



if __name__ == "__main__":
    #excel_name = "Consum mobils del 2002 al 20073.xlsx"
    excel = read_excel()

    a_column = read_column(excel, 0)
    b_column = read_column(excel, 1)
    c_column = read_column(excel, 2)

    index_list = write_iterations_through_column(a_column)

    mobile_phone_list = []
    for n in index_list:
        mobile_phone_list.append(c_column[int(n)].split())

    phone_list = write_final_iterations_though_excel()
    print(phone_list)

    with open('employee_file.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in phone_list:
            employee_writer.writerow([i])