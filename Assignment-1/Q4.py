# Create a List L that is defined as= [10, 20, 30, 40, 50, 60, 70, 80]. 
# (i) WAP to add 200 and 300 to L.
# (ii) WAP to remove 10 and 30 from L.
# (iii) WAP to sort L in ascending order.
# (iv) WAP to sort L in descending order.
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
print('The Ascending order of the list is : ', l)

# (iv)
for i in range (0, n):
    for j in range (i+1, n):
        if l[i]<l[j]:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
print('The Descending order of the list is : ', l)
