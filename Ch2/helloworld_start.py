#
# Example file for HelloWorld
#

def main():
    print("Hello World")
    name = input("What is your name? ")
    print("Nice to meet you ", name)

# '__name__' is a variable that represents the current module
# The below statement essentially just means that this file is being run as the current module
# Otherwise it would execute the code immediately even if it was being imported to another module
if __name__ == "__main__":
    main()
