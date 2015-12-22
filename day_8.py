f = open('day_8', 'r')

lit = 0
in_mem = 0

s = f.readline().rstrip()
while s != '':
    lit += len(s)
    in_mem_buf = 2
    for c in s:
        if c == '\\' or c == '\"':
            in_mem_buf += 2
        else:
            in_mem_buf += 1
    in_mem += in_mem_buf
    s = f.readline().rstrip()

print -lit + in_mem
