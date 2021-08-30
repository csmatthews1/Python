def countdown(count):
    list = [];
    for x in range (count,-1,-1):
        list.append(x)
    return list;

# test countdown
# list = countdown(5)
# print(list)

def print_and_return (two_num_list):
    print(two_num_list[0])
    return two_num_list[1]

# test print_and_return
# second = print_and_return([5,7])
# print(second)

def first_plus_length (list):
    return list[0] + len(list)

# test first_plus_length
# result = first_plus_length([1,2,3,4,5])
# print(result)

def greater_values (list):
    newList = []
    for x in list:
        if x > list[1]:
            newList.append(x)
    
    return newList

# test greater_values
# list = greater_values([5,2,3,2,1,4])
# print(list)

def list_size_val (size, value):
    newList = []
    for x in range(size):
        newList.append(value)
    
    return newList

#test list_size_val
# list = list_size_val (6, 2)
# print(list)
