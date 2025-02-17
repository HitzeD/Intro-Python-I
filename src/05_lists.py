# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE 
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE 
for i in y:
    x.append(i)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE 
for i in y[1:]:
    x.append(i)    
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE 
x.append(9)
x.append(99)
x.append(10)
print(x)

# Print the length of list x
# YOUR CODE HERE 
len(x)

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
for i in x:
    i * 1000
