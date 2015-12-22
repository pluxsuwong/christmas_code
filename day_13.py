f = open('day_13', 'r')

fb = {}

s = f.readline().rstrip()
while s != '':
    e = s.split(' ')
    p_0 = e[0]
    p_1 = e[10]
    eff = 0
    if e[2] == 'lose':
        eff = -int(e[3])
    else:
        eff = int(e[3])
    try:
        fb[p_0].append((p_1, eff))
    except:
        fb[p_0] = [(p_1, eff)]
    s = f.readline().rstrip()



print fb
