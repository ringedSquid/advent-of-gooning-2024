data = [int(x) for x in open("in", "r").read().split()]
a = []
b = []
for i in range(len(data)//2):
    a.append(data[2*i])
    b.append(data[2*i+1])

a = sorted(a)
b = sorted(b)

s = 0

for i in range(len(a)):
    s += abs(a[i] - b[i])

print(s)

