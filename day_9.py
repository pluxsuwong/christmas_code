import sys, copy

def max_path(last_node, rem_nodes):
    if len(rem_nodes) == 1:
        e_costs = graph[rem_nodes[0]]
        for tup in e_costs:
            if tup[0] == last_node:
                return tup[1]
        print 'Couldn\'t find tuple in graph'
        sys.exit(0)
    max_c = 0
    for n in rem_nodes:
        node_cp = copy.deepcopy(rem_nodes)
        node_cp.remove(n)
        cur_cost = 0
        e_costs = graph[n]
        for tup in e_costs:
            if tup[0] == last_node:
                cur_cost = tup[1]
                break
        path_cost = cur_cost + max_path(n, node_cp)
        if path_cost > max_c:
            max_c = path_cost
    return max_c

f = open('day_9', 'r')

graph = {}

s = f.readline().rstrip()
while s != '':
    tmp = s.split(' ')
    e = (tmp[0], tmp[2], int(tmp[4]))
    try:
        graph[e[0]].append((e[1], e[2]))
    except:
        graph[e[0]] = [(e[1], e[2])]
    try:
        graph[e[1]].append((e[0], e[2]))
    except:
        graph[e[1]] = [(e[0], e[2])]
    s = f.readline().rstrip()

nodes = graph.keys()

max_cost = 0
for n in nodes:
    node_cp = copy.deepcopy(nodes)
    node_cp.remove(n)
    path_cost = max_path(n, node_cp)
    if path_cost > max_cost:
        max_cost = path_cost

print max_cost
