# 
# Example file for retrieving data from the internet
#

import urllib.request

def main():
  # Define URL
  webUrl = urllib.request.urlopen("http://www.google.com")
  # Print out request code
  print("Result code: " + str(webUrl.getcode()))
  # Print out the HTML code for the site
  data = webUrl.read()
  print(data)

if __name__ == "__main__":
  main()
