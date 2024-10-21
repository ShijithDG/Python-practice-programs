original_list = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155, 12]

def remove_duplicates(input_list):
    my_set = set()
    result = []
    for i in input_list:
        if i not in my_set:
            my_set.add(i)
            result.append(i)
    return result

filtered_list = remove_duplicates(original_list)
print(filtered_list)
