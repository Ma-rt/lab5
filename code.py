def get_next_nonzero(data, current):
    for i in range(current, len(data)):
        if data[i] != 0:
            return i
    return current


def rest_data_corr(data):
    coef = 0
    values = []
    for i in range(len(data)):
        if data[i] != 0:
            values.append(data[i])
    for i in range(len(values) - 1):
        coef += values[i] / values[i + 1]
    coef /= len(values)
    for i in range(len(data)):
        if data[i] == 0 and i != 0:
            data[i] = data[i - 1] * coef
    return data


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


d = get_data(mscd_data_path)
print(d[0:20])
dd = del_random_data_blocks(d)
print(dd[0:20])
print(rest_data_vins(dd)[0:20])

