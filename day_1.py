f = open('day_1', 'r')
s = f.read()

up = 0
down = 0
floor = 0
for i in s:
    if i == '(':
        up += 1
    elif i == ')':
        down += 1
    else:
        print i

floor = up - down
print up
print down
print floor

f.close()
