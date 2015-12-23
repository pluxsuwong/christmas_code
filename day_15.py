import copy

def cur_score(quantities):
    total_score = 1
    for x in range(4):
        property_score = 0
        for i in quantities:
            e = graph[i]
            property_score += quantities[i]*e[x]
        total_score *= property_score
    if total_score < 0:
        return 0
    return total_score

f = open('day_15', 'r')

graph = {}

s = f.readline().rstrip()
while s != '':
    e = s.split(' ')
    graph[e[0]] = (int(e[2]), int(e[4]), int(e[6]), int(e[8]), int(e[10]))
    s = f.readline().rstrip()

quantities = {}
for i in graph:
    quantities[i] = 1

for x in range(96):
    best_i, best_score = '', -1
    for i in quantities:
        quantities_cp = copy.deepcopy(quantities)
        quantities_cp[i] += 1
        i_score = cur_score(quantities_cp)
        if i_score > best_score:
            best_score = i_score
            best_i = i
    quantities[best_i] += 1

print quantities
print cur_score(quantities)
