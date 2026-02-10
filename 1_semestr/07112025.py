text = open("input.txt", 'r')
s = text.read()
parts = s.split()

parts = list(map(int, parts))

item_count, cell_count = parts[:2]

prices = parts[2:2 + item_count]


prices.sort()
h1, h2 = parts[-2:]

output = open("output.txt", 'w')
output.write(str(h1 + h2))
