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