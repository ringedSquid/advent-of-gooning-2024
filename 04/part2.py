FILE = "in"
data = open(FILE, "r").read().split("\n")
data = data[:len(data)-1]

count = 0

for i in range(len(data)):
    for j in range(len(data[i])):
        if i > 0 and i < len(data) - 1 and j > 0 and j < len(data[i]) - 1:
            if (data[i][j] == 'A'):
                lu = data[i-1][j-1]
                ld = data[i+1][j-1]
                ru = data[i-1][j+1]
                rd = data[i+1][j+1] 
                if (sorted([lu, ld, ru, rd]) == ['M', 'M', 'S', 'S']): count += 1
                    
print(count)



