l = [10, 20, 30, 40, 50, 60, 70, 80]
print(l)

# (i)
l.append(300)
l.append(200)
print(l)

# (ii)
l.remove(10)
l.remove(30)
print(l)

# (iii)
n = len(l)
for i in range (0, n):
    for j in range (i+1, n):
        if l[i]>l[j]:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
print(l)
for i in range (0, n):
    for j in range (i+1, n):
        if l[i]<l[j]:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
print(l)
