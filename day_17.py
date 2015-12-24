import copy

def cur_vol(containers):
    tally = 0
    for tup in containers:
        tally += tup[1]
    return tally

def progress(cur_containers, rem_containers):
    if cur_vol(cur_containers) == 150:
        return [cur_containers]
    elif cur_vol(cur_containers) > 150:
        return None

    combos = []
    while rem_containers:
        c = rem_containers.pop(0)
        containers_cp = copy.deepcopy(rem_containers)
        new_cur_containers = copy.deepcopy(cur_containers)
        new_cur_containers.append(c)
        more_combos = progress(new_cur_containers, containers_cp)
        if more_combos != None:
            for combo in more_combos:
                combos.append(combo)
    return combos

f = open('day_17', 'r')

unsorted_containers = []
num_id = 0
s = f.readline().rstrip()
while s != '':
    unsorted_containers.append((num_id, int(s)))
    num_id += 1
    s = f.readline().rstrip()

containers = []
while unsorted_containers:
    max_c = unsorted_containers[0]
    for u_c in unsorted_containers:
        if u_c[1] > max_c[1]:
            max_c = u_c
    containers.append(max_c)
    unsorted_containers.remove(max_c)

combos = []
while containers:
    c = containers.pop(0)
    containers_cp = copy.deepcopy(containers)
    more_combos = progress([c], containers_cp)
    for combo in more_combos:
        combos.append(combo)
'''
for c in combos:
    print c
print combos
'''

min_size = 999
min_bufs = []
for c in combos:
    if len(c) < min_size:
        min_size = len(c)
        min_bufs = [c]
    elif len(c) == min_size:
        min_bufs.append(c)

print len(min_bufs)
