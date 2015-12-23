import copy

def max_path(first_node, last_node, rem_nodes):
    if len(rem_nodes) == 1:
        e_costs_f = graph[first_node]
        e_costs_l = graph[last_node]
        e_costs_r = graph[rem_nodes[0]]
        cost_buf = 0
        for tup_f in e_costs_f:
            if tup_f[0] == rem_nodes[0]:
                cost_buf += tup_f[1]
                break
        for tup_l in e_costs_l:
            if tup_l[0] == rem_nodes[0]:
                cost_buf += tup_l[1]
                break
        for tup_r in e_costs_r:
            if tup_r[0] == first_node or tup_r[0] == last_node:
                cost_buf += tup_r[1]
        return cost_buf

    max_c = 0
    for n in rem_nodes:
        node_cp = copy.deepcopy(rem_nodes)
        node_cp.remove(n)
        cur_cost = 0
        e_costs_l = graph[last_node]
        e_costs_r = graph[n]
        for tup_l in e_costs_l:
            if tup_l[0] == n:
                cur_cost += tup_l[1]
                break
        for tup_r in e_costs_r:
            if tup_r[0] == last_node:
                cur_cost += tup_r[1]
                break
        path_cost = cur_cost + max_path(first_node, n, node_cp)
        if path_cost > max_c:
            max_c = path_cost
    return max_c


f = open('day_13', 'r')

global graph, seating
graph = {}
seating = {}

s = f.readline().rstrip()
while s != '':
    e = s.split(' ')
    p_0 = e[0]
    p_1 = e[10]
    eff = 0
    if e[2] == 'lose':
        eff = -int(e[3])
    else:
        eff = int(e[3])
    try:
        graph[p_0].append((p_1, eff))
    except:
        graph[p_0] = [(p_1, eff)]
    s = f.readline().rstrip()

nodes = graph.keys()

max_cost = 0
for n in nodes:
    node_cp = copy.deepcopy(nodes)
    node_cp.remove(n)
    path_cost = max_path(n, n, node_cp)
    if path_cost > max_cost:
        max_cost = path_cost

print max_cost
