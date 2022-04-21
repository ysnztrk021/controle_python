def get_indexes(my_list, value_to_get):
    result=[]
    for i in range(len(my_list)):
        if value_to_get==my_list[i]:
            result.append(i)
    return result


my_list=[1,2,3,4,5,1]

numbers=[-2,2,3,0,-2,6,-2,-2,8]

new_list=[22,11,3,0,-7,8]

print(get_indexes(my_list,1))
print(get_indexes(numbers,-2))
print(get_indexes(new_list,100))