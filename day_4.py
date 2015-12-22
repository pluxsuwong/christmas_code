import hashlib as hl

f = open('day_4', 'r')
s = f.read()
s = s.rstrip()

m = hl.md5()
m.update(s)
mh = m.digest()
op = "".join("{:02x}".format(ord(c)) for c in mh)
num = 0

while op[:6] != '000000':
    num += 1
    ss = s + str(num)
    mm = hl.md5()
    mm.update(ss)
    mh = mm.digest()
    op = "".join("{:02x}".format(ord(c)) for c in mh)

print num

f.close()
