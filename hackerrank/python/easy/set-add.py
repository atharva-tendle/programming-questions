# create the set
stamp_set = set()

# get number of stamps
num_stamps = int(input())

# iterate through stamps
for i in range(num_stamps):
    # get the current stamp
    cur_stamp = input()
    # add the current stamp to the stamp set
    stamp_set.add(cur_stamp)

# print out number of unique stamps
print(len(stamp_set))