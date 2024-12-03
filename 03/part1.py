data = open("in", "r").read().split("mul(");
s = 0
for i in range(len(data)):
    if ")" in data[i][:8]:
        data[i] = data[i][:data[i].find(")")].split(",")
        if (len(data[i]) == 2) and (data[i][0].isdigit()) and (data[i][1].isdigit()):
            s += int(data[i][0])*int(data[i][1])

print(s)
