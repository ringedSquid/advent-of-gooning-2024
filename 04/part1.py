FILE = "in"
data = open(FILE, "r").read().split("\n")
data = data[:len(data)-1]

count = 0

for i in range(len(data)):
    for j in range(len(data[i])):
        if (j < len(data[i])-3):
            if (data[i][j:j+4] == "XMAS") or (data[i][j:j+4] == "SAMX"): 
                count += 1

        if (i < len(data)-3):
            word = ""
            for y in range(4):
                word += data[i+y][j]
            if (word == "XMAS") or (word == "SAMX"): count += 1

        if (i < len(data)-3) and (j < len(data[i])-3):
            word = ""
            for y in range(4):
                word += data[i+y][j+y]
            if (word == "XMAS") or (word == "SAMX"): count += 1

        if (i < len(data)-3) and (j >= 3):
            word = ""
            for y in range(4):
                word += data[i+y][j-y]
            if (word == "XMAS") or (word == "SAMX"): count += 1






print(count)



