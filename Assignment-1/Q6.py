import random

list = []
n = 100
for i in range (n):
    list.append(random.randint(100,900))
print(list)

# (i) & (ii)
even_count = 0
odd_count = 0
odd_list = []
even_list = []
for element in list:
    if element%2 == 0:
        even_list.append(element)
        even_count  = even_count + 1
        
    else:
        odd_list.append(element)
        odd_count= odd_count + 1
        
print(f"\nThe Odd list of elements is : {odd_list}")
print(f"\nThe total no. of elements in Odd_count is : {odd_count}")
print(f"\nThe Even list of elements is : {even_list}")
print(f"\nThe total no. of elements in Even_count is : {even_count}")

# (iii)
Prime_list = []
Prime_count = 0
for elements in list:
    if elements < 2:
        print("Element is less than 2")
        break;
    for i in range (2, int(elements/2)+1):
        if elements%i == 0:
            break;
    else:
        Prime_list.append(elements)
        Prime_count = Prime_count + 1
print(f"\nThe Prime list of elements is : {Prime_list}")
print(f"\nThe total no. of elements in Prime_list is : {Prime_count}")
