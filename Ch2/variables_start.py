# 
# Example file for variables
#

# Declare a variable and initialize it
f = "0"
print(f)


# # re-declaring the variable works
f = "abc"
print(f)


# # ERROR: variables of different types cannot be combined
print("this is a string " + str(123))


# Global vs. local variables in functions
def someFunction():
    global f # makes this declaration global so will override previous definitions
    f = "def"
    print(f)

someFunction()
print(f)

del f # can delete variable definitions in real time
print(f)

