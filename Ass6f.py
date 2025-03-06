import re

str= "Hello, World!"
pattern = r"Hello"

if re.match(pattern, str):
    print("Match found!")
else:
    print("No match.")
