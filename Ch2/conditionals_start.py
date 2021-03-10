#
# Example file for working with conditional statements
#


def main():
    x, y = 10, 100

    # conditional flow uses if, elif, else
    if (x < y):
        st = "x is less than y"
    # else if is combined to keyword 'elif'
    elif (x == y):
        st = "x is the same as y"
    else:
        st = "x is greater than y"

    print(st)

    # conditional statements let you use "a if C else b"
    st = "x is less than y" if (x < y) else "x is greater than y"

    string = "His friends don't dance"
    conditionalString = "Then if they don't dance then they ain't no friends of mine" if (string) else "He can dance if he wants to"
    print(conditionalString)

if __name__ == "__main__":
    main()

# **Note: No switch statements in python