import random
import numpy as np
import datetime


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

        data[date] = splited_line[5]
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
        if data.get(day) == None:
            data[day] = 0


dt = get_data(mscd_data_path)
delete_random_data(dt)
print(dt)
insert_missed_elements(dt)
print(dt)
