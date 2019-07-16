
from collections import OrderedDict

# create ordered dictionary
item_dict = OrderedDict()

# get the number of items
items = int(input())
# iterate through the items
for i in range(items):
    # get the current item
    cur_item = input().split(' ')
    # get the name of the current item
    item_name = ' '.join(cur_item[i] for i in range(len(cur_item)-1))
    # get the price of the current item
    item_price = int(cur_item[-1])

    # check if item exists in the ordered dictionary
    if item_name in item_dict:
        # if it exists then add the price of the item
        item_dict[item_name] += item_price
    else:
        # otherwise add the item with its price
        item_dict[item_name] = item_price

# print out items in the dictionary
for key in item_dict.keys():
    print(key, item_dict[key])