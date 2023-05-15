string = input("Tell me the string you want to check:")
print('Tell me the cfg you want to check the string with\n (Make sure to input the cfg in this specific format: ["S -> AB","A -> CD | CF"]\n So, its a list of strings and make sure to maintain the spaces. You may add more than one rule using | ):')
grammar = input()

grammer = eval(grammar)
cfg = {}

for i in grammer:
    cmd = i.split(" -> ")
    cmd[1] = cmd[1].split(" | ")
    if cmd[0] not in cfg.keys():
        cfg[cmd[0]] = []
    for j in cmd[1]:
        if j not in cfg[cmd[0]]:
            cfg[cmd[0]].append(j)

arr = []

for i in range(len(string),0,-1):
    g = [0]*i
    arr.append(g)

def unify(a:list,b:list): #this function creates a new list like you give it [B] and [A,C] and it returns [BA,BC]
    if len(a)==0:
        return b
    if len(b)==0:
        return a
    result = []
    for i in a:
        for j in b:
            result.append(i+j)
    return result

reverse_cfg = {}

for key in cfg.keys():
    for item in cfg[key]:
        if item not in reverse_cfg.keys():
            reverse_cfg[item] = []
        reverse_cfg[item].append(key)
    

for i in range(len(string)):
    if i == 0:
        for j in range(len(string)):
            arr[i][j] = reverse_cfg[string[j]]
    else:
        for j in range(len(string)-i):
            p = i-1
            q= j+1
            cache = []
            for k in range(i):
                for item in unify(arr[k][j],arr[p][q]):
                    if item in reverse_cfg.keys():
                        for it in reverse_cfg[item]:
                            if it not in cache:
                                cache.append(it)
                p-=1
                q+=1

            arr[i][j] = cache

print()
if "S" in arr[-1][-1]:
    print("YES it can be derived")
else:
    print("NO it can't be derived")
print()
print("Printing the CYK table:")
print()
printing = ""
for i in arr:
    output = ""
    for j in i:
        output+="{"
        for k in j:
            output+= k + ","
        if output[-1] == ",":
            output = output[:-1]+"} "
        else:
            output = output+"} "
    printing = output+"\n"+printing

print(printing)