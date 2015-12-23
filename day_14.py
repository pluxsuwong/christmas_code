f = open('day_14', 'r')

graph = {}

s = f.readline().rstrip()
while s != '':
    r = s.split(' ')
    graph[r[0]] = (int(r[3]), int(r[6]), int(r[13]))
    s = f.readline().rstrip()

distances = {}

for i in range(2504):
    for r in graph:
        e = graph[r]
        if i % (e[1] + e[2]) < e[1]:
            try:
                distances[r] += e[0]
            except:
                distances[r] = e[0]

print distances
