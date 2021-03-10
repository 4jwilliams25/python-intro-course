#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  while (x < 5):
    print(x)
    x = x + 1

  # define a for loop
  for x in range(5, 10):
    print(x)

  # use a for loop over a collection
  days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  for d in days:
    print(d)
  
  # use the break and continue statements
  for x in range(5, 10):
    # 'break' statement will terminate the loop if condition met > move to next code block
    # if (x ==7): break
    # 'continue' statement will skip that iteration and then re-execute (skip it)
    if (x % 2 == 0): continue
    print(x)

  #using the enumerate() function to get index 
  days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  for i, d in enumerate(days):
    print(i, d)

if __name__ == "__main__":
  main()
