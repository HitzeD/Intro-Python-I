"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE

# Expilictly closing the file

# file = open('foo.txt', 'r')
# print(file.read())
# # file.read()
# file.close()

# opening the file and doing the logic while under-the-hood closing the file once outside of scope
# words = None

with open('foo.txt') as file:
    words = file.read()
    # print(file.read())



# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE

with open('bar.txt', 'w') as bar:
    bar.write('This is a test\n')
    bar.write('This 1 is a test\n')
    bar.write('This 2 is a test\n')

with open('bar.txt') as file2:
    print(file2.read())
