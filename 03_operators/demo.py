# Operators

# Arithmetic Operators
num1 = 3
num2 = 2
print(f"Sum of {num1} and {num2} is {num1+num2}")
print(f"Difference of {num1} and {num2} is {num1-num2}")
print(f"Product of {num1} and {num2} is {num1*num2}")
print(f"Division of {num1} and {num2} is {num1/num2}")
print(f"Modulus of {num1} and {num2} is {num1%num2}")

print(f"Floor Division of {num1} and {num2} is {num1//num2}")
print(f"Result of {num1} power {num2} is {num1**num2}") # 3 ^ 2

# Compound Assignment Operators
num = 10
num = num + 5 # without Compound Assignment Operators
print(num)

num = 10
num+=5
print(num) # with Compound Assignment Operators
num*=5
print(num)

count = 1
# increment count 
count += 1
print(count)

count = 10
# decrement count 
count -= 1
print(count)

# Comparison Operators 
a = 10
b = 5
c = 3
d = 2

print(a == b)
print(a > b)
print(a < b)

# Logical Operators 
res_and = a > b and c < d # T and F -> F
print(res_and)
res_and = a > b and c > d # T and T -> T
print(res_and)

res_or = a > b or c < d # T or F -> T
print(res_or)

res_or = a > b # T
print(not res_or) # F
