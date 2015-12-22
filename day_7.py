def find_inputs():
    global wires, cmd_list
    cmd_list_cp = cmd_list
    for cmd in cmd_list_cp:
        if len(cmd) == 3:
            try:
                wires[cmd[2]] = int(cmd[0])
                cmd_list.remove(cmd)
            except ValueError:
                pass

def exec_circuit():
    global wires, cmd_list
    used = []
    while len(cmd_list) > 0:
        cmd_list_cp = cmd_list
        for cmd in cmd_list_cp:
            if cmd[0] == 'NOT':
                try:
                    wires[cmd[3]] = ~wires[cmd[1]]
                    cmd_list.remove(cmd)
                    used.append(cmd)
                except:
                    pass
            elif cmd[1] == 'AND':
                try:
                    wires[cmd[4]] = int(cmd[0]) & wires[cmd[2]]
                    cmd_list.remove(cmd)
                    used.append(cmd)
                except:
                    try:
                        wires[cmd[4]] = wires[cmd[0]] & wires[cmd[2]]
                        cmd_list.remove(cmd)
                        used.append(cmd)
                    except:
                        pass
            elif cmd[1] == 'OR':
                try:
                    wires[cmd[4]] = wires[cmd[0]] | wires[cmd[2]]
                    cmd_list.remove(cmd)
                    used.append(cmd)
                except:
                    pass
            elif cmd[1] == 'LSHIFT':
                try:
                    wires[cmd[4]] = wires[cmd[0]] << int(cmd[2])
                    cmd_list.remove(cmd)
                    used.append(cmd)
                except:
                    pass
            elif cmd[1] == 'RSHIFT':
                try:
                    wires[cmd[4]] = wires[cmd[0]] >> int(cmd[2])
                    cmd_list.remove(cmd)
                    used.append(cmd)
                except:
                    pass
            elif len(cmd) == 3:
                try:
                    wires[cmd[2]] = wires[cmd[0]]
                    cmd_list.remove(cmd)
                    used.append(cmd)
                except:
                    pass
            else:
                print 'Invalid instruction:', cmd

f = open('day_7', 'r')

global wires, cmd_list
wires = {}
cmd_list = []
c = f.readline().rstrip()
while c != '':
    cmd = c.split(' ')
    cmd_list.append(cmd)
    c = f.readline().rstrip()

find_inputs()
wires['b'] = 46065
print 'inputs:', wires
exec_circuit()
print wires['a']
