# Write a Python Program to input basic salary of an employee and calculate its Gross salary according to following: Basic Salary <= 10000 : HRA = 20%, DA = 80% Basic Salary <= 20000 : HRA = 25%, DA = 90% Basic Salary > 20000 : HRA = 30%, DA = 95%.

Basic_Salary = int(input('Enter the amount of Salary : '))

def Gross(Basic_Salary, HRA, DA):
   hra_value = (HRA / 100) * Basic_Salary
   da_value = (DA / 100) * Basic_Salary
   gross_income_value = Basic_Salary + hra_value + da_value
   return gross_income_value

if Basic_Salary <= 10000:
    HRA = 20
    DA = 80
elif Basic_Salary <= 20000:
    HRA = 25
    DA = 90
else:
    HRA = 30
    DA = 95
Gross_income = Gross(Basic_Salary, HRA, DA)
print(Gross_income)
