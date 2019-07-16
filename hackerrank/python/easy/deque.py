from collections import deque

# create a deque obj
dq = deque()

# get the number of operations
num_op = int(input())

# number of operations
for i in range(num_op):
    # get current operation and 
    # if operation is not pop then
    # get the operation and the number
    cur_op = input().split(' ')
    if len(cur_op) > 1:
        op, cur_num = cur_op[0], cur_op[1]
    else:
        op = cur_op[0]

    # check what operation needs to be performed
    # and then perform it

    if op == 'append':
        dq.append(cur_num)
    elif op == 'appendleft':
        dq.appendleft(cur_num)
    elif op == 'pop':
        dq.pop()
    elif op == 'popleft':
        dq.popleft()
    else:
        pass

# print out items in deque
for item in dq:
    print(item, end=' ')




