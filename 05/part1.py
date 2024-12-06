FILE = "test"
data = open(FILE, "r").read().split("\n");
data = data[:len(data)-1]

rules = [] 
sub = 0
r = 0
for i in range(len(data)):
    if (data[i] == ""):
        r = i+1
        break
    d = data[i].split("|")
    d = [int(x) for x in d]
    rules.append(d)

for i in range(r, len(data)):
    d = data[i].split(",")
    print(d)
    d = [int(x) for x in d]
    sub += d[len(d)//2]
    for y in range(len(d)):
        valid = True
        for rule in rules:
            if rule[0] == d[y]:
                if rule[1] not in d[y:]:
                    valid = False
                    sub -= d[len(d)//2]
        if (valid == False):
            break

print(sub)



