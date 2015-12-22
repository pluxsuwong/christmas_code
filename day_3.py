f = open('day_3', 'r')
d = f.read()
houses = []
x = 0
y = 0
h_id = str(x) + ',' + str(y)
houses.append(h_id)
for i in d:
    if i == '>':
        x += 1
    elif i == '<':
        x -= 1
    elif i == '^':
        y += 1
    elif i == 'v':
        y -= 1
    h_id = str(x) + ',' + str(y)
    houses.append(h_id)

print len(set(houses))

f.close()
