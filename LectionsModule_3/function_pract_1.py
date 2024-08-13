def find_max(list_):
    max_ = list_[0]
    for num in list_:
        if num > max_:
            max_ = num
    return max_


#print(find_max([1, 5, -14, 29, 112, -1000]))


def count_even(lst_chet):
    chet_ = []
    for num in lst_chet:
        if num % 2 == 0:
            chet_.append(num)
    return chet_


#print(count_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))


def count_even(lst_):
    counter = 0
    for num in lst_:
        if num == o:
            continue
        if num % 2 == 0:
            counter += 1
    return counter


#print(count_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))

def unique(list_):
    new_list = []
    for num in list_:
        if num not in new_list:
            new_list.append(num)
    return new_list


print(unique([1, 1, 2, 3, 4, 4, 5, 5, 11, 1, 2, 3, 4, 5, 2, 2, 1, 3]))