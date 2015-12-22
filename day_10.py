def proceed(o_num):
    main_buf = []
    sub_buf = []
    n_num = ''
    for c in o_num:
        if not sub_buf or c in sub_buf:
            sub_buf.append(c)
        else:
            main_buf.append(sub_buf)
            sub_buf = [c]
    main_buf.append(sub_buf)
    for sub_buf in main_buf:
        tmp = n_num + str(len(sub_buf)) + sub_buf[0]
        n_num = tmp
    return n_num

f = open('day_10', 'r')

s = f.readline().rstrip()

for i in range(50):
    ans = proceed(s)
    s = ans

print len(s)
