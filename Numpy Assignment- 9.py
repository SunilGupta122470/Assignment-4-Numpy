import numpy as np

A_1d = np.array([1,2,3,4,5,6,7,9,10])
A_2d = np.arange(1,10).reshape(3,3)
numpyArry = np.array([10,20,30,40,50])

print("Arrary 1 D: ",A_1d)
print("Arrary 2 D: ",A_2d)
print(numpyArry)

print(type(A_1d))
print(type(A_2d))
print(type(numpyArry))

# -------------------------------------------------------------------------
# Task 2 mathsmatical Opeartions
A= np.array([10,20,30,40])
B= np.array([1,2,3,4])
print("\n")
print(f"Addition: {A+B}")
print(f"Subtraction: {A-B}")
print(f"Multiplication: {A*B}")
print(f"Division: {A/B}")
print(f"Division: {A**2}")
print(f"sum: {np.add(A,B)}")
print(f"subtract: {np.subtract(A,B)}")

# -------------------------------------------------------------------------
# Task 3 Important Numpy Mathematical formula
values = np.array([2,4,6,8,10])

print(np.sqrt(values))
print(np.random.exponential(values))
print(np.log(values))
print(np.sum(values))
print(np.cumsum(values))

# -------------------------------------------------------------------------
# Task 4 Aggerate Opeartions

data = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

# Row wise Sum
print(np.sum(data,1))
#Columns wise sum
print(np.sum(data,0))
# Minimum values
print(np.min(data))
# Max value
print(np.max(data))
#Overall mean
print(np.mean(data))

# -------------------------------------------------------------------------
# Task 5 Statiscal Operations (Core focus)
marks = np.array([78,85,90,66,72,88,95,60])
print(np.mean(marks))
print(np.median(marks))
print(np.var(marks))
print(np.std(marks))
print(f"Maximum {np.max(marks)} & Minimum: {np.min(marks)}")
print(np.max(marks) - np.min(marks))

# -------------------------------------------------------------------------
# Task 6 Percentiles & sorting 
marks = np.array([78,85,90,66,72,88,95,60])

print(np.sort(marks))

print(np.percentile(marks,25))
print(np.percentile(marks,50))
print(np.percentile(marks,75))

Cunt_above_avg= sum(map(lambda x:x >np.average(marks),marks))
print(f"total student from the list: {Cunt_above_avg}")

# -------------------------------------------------------------------------
# Task 7 Percentiles & sorting 
sales = np.array([1200,1500,900,2000,1800,1700,1600])
print(np.sum(sales))
print(np.average(sales))
print(f"Maximum sale {np.max(sales)} & Minimum Sale: {np.min(sales)}")
print(np.std(sales))

days_above_avg = [i+1 for i, x in enumerate(sales) if x > np.average(sales)]
print(f"total Sales from the array: {days_above_avg}")



# list(map(lambda x: print(x)  if x>1500 else None,sales))
list(filter(lambda x: print(x)  if x>1500 else None,sales))
