d = {}


def update_dictionary(d, key, value):
    if key in d:
        d[key] = [value]
    if key not in d:
        if key*2 in d:
            vladd = d.get(key*2)
            d[key*2] = value+vladd
        if key*2 not in d:
            add = {key*2 : value}
            dict.update(add)




print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}