s = input("i")
words   = sum(c.isalpha() for c in s)
spaces  = sum(c.isspace() for c in s)
others  = len(s) - words - spaces
print(others)