# read in the first number
a = int(input())
# read in the second number
b = int(input())

# print out a ** b
print(pow(a, b))

# try to read in a third number
try:
    m = int(input())
    
    # if a third number is provided then assert that b is not negative
    assert b > 0

    # print a ** b mod m
    print(pow(a, b, m))
except:
    pass