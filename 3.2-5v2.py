d = {} # завожу пустой словарь

# начало функции
def update_dictionary(d, key, value):
    if key in d:
        vol = [d[key]] + [value]
        d[key] = vol
    else:
        key2 = key * 2
        vol2 = d.get(key2)
        if vol2 is None:
            d[key2] = value
        else:
            vol3 = [vol2] + [value]
            d[key2] = vol3


# конец функции

# проверка
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}