data = [int(x) for x in open("in", "r").read().split()]
a = []
b = []
for i in range(len(data)//2):
    a.append(data[2*i])
    b.append(data[2*i+1])

a = sorted(a)
b = sorted(b)
c = [0] * len(a)

s = 0
for i in range(len(a)):
    for y in range(len(b)):
        if b[y] == a[i]:
            c[i] += 1
    s += a[i] * c[i]

print(s)
