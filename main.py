import datetime
import random
import numpy as np
import matplotlib.pyplot as plt

visa_data_path = "visa.txt"
mscd_data_path = "mscard.txt"


def get_data(path):
    file = open(path)
    lines = file.readlines()
    data = {}
    for i in range(0, len(lines)):
        splited_line = lines[i].split(",")

        date = splited_line[2][4:]
        date = date[0:2] + "." + date[2:]

        data[date] = float(splited_line[5])
    file.close()
    return data


def delete_random_data(data):
    for i in data.keys():
        if random.random() <= 0.5:
            data[i] = 0
    return data


def get_all_days_between_dates(date1=(2021, 11, 1), date2=(2022, 11, 1)):
    d1 = datetime.date(*date1)
    d2 = datetime.date(*date2)
    return [(d1 + datetime.timedelta(days=x)).strftime('%m.%d') for x in range((d2-d1).days + 1)]


def insert_missed_elements(data):
    for day in get_all_days_between_dates():
        if data.get(day) is None:
            data[day] = 0


def convert_dict_to_list(source_dict):
    data_list = []
    for day in get_all_days_between_dates():
        data_list.append(source_dict[day])
    return data_list


def get_next_nonzero(data, current):
    for i in range(current, len(data)):
        if data[i] != 0:
            return i
    return current


def rest_data_vins(data):
    for i in range(len(data)):
        if data[i] == 0 and i != 0:
            data[i] = data[get_next_nonzero(data, i)]
    return data


def rest_data_linear(data):
    for i in range(len(data)):
        if data[i] == 0 and i != 0:
            next_i = get_next_nonzero(data, i)
            data[i] = data[i - 1] + ((data[next_i] - data[i - 1]) / (next_i - i))
    return data


def calculate_corr_coef(data1, data2):

    return np.corrcoef(data1, data2)


dt = get_data(mscd_data_path)
dt2 = get_data(visa_data_path)
delete_random_data(dt)


def find_index_of_next_nonzero(start, data):
    for i in range(start, len(data)):
        if data[i] != 0:
            return i
    return -1


insert_missed_elements(dt)
insert_missed_elements(dt2)
print(convert_dict_to_list(dt))
print(dt2)

coeff = calculate_corr_coef(convert_dict_to_list(dt), convert_dict_to_list(dt2))
print(coeff)

c = convert_dict_to_list(dt)
b = convert_dict_to_list(dt2)



