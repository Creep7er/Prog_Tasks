d = {"a": [2, 4, 6], "b": [3, 5], "c": [2, 3, 4]}

res = []

for key, values in d.items():
    if not values: 
        continue

    all_even = all(x % 2 == 0 for x in values)
    all_odd = all(x % 2 == 1 for x in values)

    if all_even:
        res.append(f"{key}_even")
    elif all_odd:
        res.append(f"{key}_odd")

res.sort()
print(res)