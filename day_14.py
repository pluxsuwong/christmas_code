f = open('day_14', 'r')

graph = {}

s = f.readline().rstrip()
while s != '':
    r = s.split(' ')
    graph[r[0]] = (int(r[3]), int(r[6]), int(r[13]))
    s = f.readline().rstrip()

distances = {}
points = {}

for i in range(2504):
    for r in graph:
        e = graph[r]
        if i % (e[1] + e[2]) < e[1]:
            try:
                distances[r] += e[0]
            except:
                distances[r] = e[0]
    leaders = []
    for r in distances:
        if not leaders:
            leaders.append(r)
        elif distances[r] > distances[leaders[0]]:
            leaders = [r]
        elif distances[r] == distances[leaders[0]]:
            leaders.append(r)
    for r in leaders:
        try:
            points[r] += 1
        except:
            points[r] = 1

print points
