import re

# get number of test cases
test_cases = int(input())

# iterate through each case
for _ in range(test_cases):
    # set falg to true
    flag  = True
    # try compiling the regex
    try:
        reg = re.compile(input())
    # if regex throws error then switch flag to false
    except re.error:
        flag = False
    # print if regex is correct/incorrect
    print(flag)