f = open('day_2', 'r')

tally = 0

s = f.readline()
while s != '':
    d = ['', '', '']
    index = 0
    for i in s:
        if i == 'x':
            index += 1
        else:
            d[index] += i
    l = int(d[0])
    w = int(d[1])
    h = int(d[2])
    sides = {l*w, w*h, h*l}
    min_s = min(sides)
    tally += 2*l*w + 2*w*h + 2*h*l + min_s
    print tally
    s = f.readline()
print tally

f.close()
