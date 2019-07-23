# total number of elements in the set
n = int(input())
# set of numbers
s = set(map(int, input().split()))
# number of commands
n_c = int(input())

for i in range(n_c):

    # current command
    cur_cmd = input()
    # set command
    cmd = cur_cmd.split(' ')[0]

    if cmd == 'pop':
        s.pop()
    elif cmd == 'discard':
        # number to discard
        num = int(cur_cmd.split(' ')[1])
        s.discard(num)
    else:
        # number to remove
        num = int(cur_cmd.split(' ')[1])
        s.remove(num)
        
# sum of the remaining set
print(sum(s))
