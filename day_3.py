f = open('day_3', 'r')
d = f.read()
turn = 0
houses = []
x_0 = 0
y_0 = 0
x_1 = 0
y_1 = 0
h_id = str(x_0) + ',' + str(y_0)
houses.append(h_id)
for i in d:
    if turn == 0:
        if i == '>':
            x_0 += 1
        elif i == '<':
            x_0 -= 1
        elif i == '^':
            y_0 += 1
        elif i == 'v':
            y_0 -= 1
        h_id = str(x_0) + ',' + str(y_0)
        houses.append(h_id)
        turn = 1
    else:
        if i == '>':
            x_1 += 1
        elif i == '<':
            x_1 -= 1
        elif i == '^':
            y_1 += 1
        elif i == 'v':
            y_1 -= 1
        h_id = str(x_1) + ',' + str(y_1)
        houses.append(h_id)
        turn = 0

print len(set(houses))

f.close()
