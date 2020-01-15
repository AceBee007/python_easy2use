
def print_pointer(data, up_pointer_list=[], down_pointer_list=[], up_pointer='^',down_pointer='v'):
    """
    data: []
    up_pointer_list = [int, int ...]
    down_pointer_list = [int, int ...]
    up_pointer = "^" 
    down_pointer = "v"
    """
    data_max_len = max([len(str(i)) for i in data])
    #print([len(str(i)) for i in data], 'max is {0}'.format(data_max_len))

    print_format = str("{0: ^"+str(data_max_len)+"}")
    if down_pointer_list != []:
        for pointer in down_pointer_list:
            for j in [down_pointer if k == pointer else ' ' for k in range(pointer+1)]:
                print(print_format.format(j), end=' ')
            print(pointer)
    for i in data:
        print(print_format.format(i),end=',')
    print()
    if up_pointer_list != []:
        for pointer in up_pointer_list:
            for j in [up_pointer if k == pointer else ' ' for k in range(pointer+1)]:
                print(print_format.format(j), end=' ')
            print(pointer)
