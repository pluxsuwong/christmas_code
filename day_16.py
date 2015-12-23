f = open('day_16', 'r')

sue_key = {('children', '3'), ('cats', '7'), ('samoyeds', '2'), ('pomeranians', '3'), ('akitas', '0'), ('vizslas', '0'), ('goldfish', '5'), ('trees', '3'), ('cars', '2'), ('perfumes', '1')}
graph = {}

s = f.readline().rstrip()
while s != '':
    e = s.split(' ')
    graph[e[0]] = {(e[1], e[2]), (e[3], e[4]), (e[5], e[6])}
    s = f.readline().rstrip()

possible_sues = []
for sue in graph:
    if graph[sue] <= sue_key:
        possible_sues.append(sue)

print possible_sues
