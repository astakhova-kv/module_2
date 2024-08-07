my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index_ = 0
konec = len(my_list)
while index_ < konec:
    if my_list[index_] > 0:
        print(my_list[index_])
        index_ += 1
    elif my_list[index_] == 0:
        index_ += 1
    else:
        break
