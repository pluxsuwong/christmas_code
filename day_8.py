f = open('day_8', 'r')

lit = 0
in_mem = 0

s = f.readline().rstrip()
while s != '':
    lit += len(s)
    in_mem_buf = -2
    esc_flag = False
    for c in s:
        if esc_flag:
            if c == 'x':
                in_mem_buf -= 2
            esc_flag = False
        elif c == '\\':
            in_mem_buf += 1
            esc_flag = True
        else:
            in_mem_buf += 1
    in_mem += in_mem_buf
    s = f.readline().rstrip()

print lit - in_mem
