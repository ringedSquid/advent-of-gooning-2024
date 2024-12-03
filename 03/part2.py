data = open("in", "r").read().split("mul(");
s = 0
enabled = True
for i in range(len(data)):
    if ")" in data[i][:8]:
        buff = data[i][:data[i].find(")")].split(",")
        if (len(buff) == 2) and (buff[0].isdigit()) and (buff[1].isdigit()):
            if (enabled):
                s += int(buff[0])*int(buff[1])

    if "do()" in data[i]:
        enabled = True
    if "don't()" in data[i]:
        enabled = False



print(s)
