def iterate(start, end, mode):
    global grid

    s = (int(start[0]), int(start[1]))
    e = (int(end[0]), int(end[1]))
    dx = abs(e[0] - s[0]) + 1
    dy = abs(e[1] - s[1]) + 1

    for y in range(dy):
        for x in range(dx):
            c = (s[0] + x, s[1] + y)
            if mode == 0:
                grid[c[1]][c[0]] = 0
            elif mode == 1:
                grid[c[1]][c[0]] = 1
            elif mode == 2:
                if grid[c[1]][c[0]] == 0:
                    grid[c[1]][c[0]] = 1
                else:
                    grid[c[1]][c[0]] = 0
            else:
                print 'Invalid mode'

f = open('day_6', 'r')

G_W = 1000
G_H = 1000

global grid
grid = [[0 for x in range(G_W)] for y in range(G_H)]

s = f.readline().rstrip()
while s != '':
    c = s.split(' ')
    if c[0] == 'turn':
        if c[1] == 'on':
            start = c[2].split(',')
            end = c[4].split(',')
            iterate(start, end, 1)
        elif c[1] == 'off':
            start = c[2].split(',')
            end = c[4].split(',')
            iterate(start, end, 0)
        else:
            print 'Invalid Command'
    elif c[0] == 'toggle':
        start = c[1].split(',')
        end = c[3].split(',')
        iterate(start, end, 2)
    else:
        print 'Invalid Command for:', c

    s = f.readline().rstrip()

ctr = 0
for row in grid:
    for light in row:
        if light == 1:
            ctr += 1
print ctr

