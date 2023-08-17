xau = input()
count_upper = sum(1 for c in xau if c.isupper())
if count_upper > len(xau)/2:
    print(xau.upper())
else:
    print(xau.lower())