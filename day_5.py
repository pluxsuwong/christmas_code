def test_1(s):
    a = s.count('a')
    e = s.count('e')
    i = s.count('i')
    o = s.count('o')
    u = s.count('u')
    if a + e + i + o + u >= 3:
        return True
    else:
        return False

def test_2(s):
    prev = s[0]
    for i in s[1:]:
        if i == prev:
            return True
        else:
            prev = i
    return False

def test_3(s):
    ab = s.count('ab')
    cd = s.count('cd')
    pq = s.count('pq')
    xy = s.count('xy')
    if ab + cd + pq + xy == 0:
        return True
    else:
        return False

f = open('day_5', 'r')

ctr = 0

s = f.readline().rstrip()
while s != '':
    if test_1(s) and test_2(s) and test_3(s):
        ctr += 1
    s = f.readline().rstrip()

print ctr
