f = open('day_12', 'r')

tally = 0
num_buf = ''
s = f.readline().rstrip()
while s != '':
    for c in s:
        if c == '-':
            num_buf = c
        try:
            int(c)
            num_buf += c
        except:
            try:
                tally += int(num_buf)
                num_buf = ''
            except:
                pass
    s = f.readline().rstrip()

print tally
