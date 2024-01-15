# D is a dictionary defined as D= {1:”One”, 2:”Two”, 3:”Three”, 4: “Four”, 5:”Five”}.
# (i) WAP to add new entry in D; key=6 and value is “Six”
# (ii) WAP to remove key=2.
# (iii) WAP to check if 6 key is present in D.
# (iv) WAP to count the number of elements present in D.
# (v) WAP to add all the values present in D.
D = {1:"One",
    2:"Two",
    3:"Three",
    4:"Four",
    5:"Five",
    }
print(D)

# (i)
D[6] = "Six"
print(D)

# (ii)
D.pop(2)
print(D)

# (iii)
x=6
for i in D.keys():
    if i==x:
        print(f"Yes, {x} is present.")
        break;
else:
    print(f"No, {x} is not present.")

# (iv)
count = 0
for i in D.keys():
    count = count + 1
print(f'Number of elements in D are {count}')

# (v)
sum_of_ele_in_D = 0
for key in D.keys():
    sum_of_ele_in_D = sum_of_ele_in_D + key
print(sum_of_ele_in_D)
