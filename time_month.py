import calendar
import math

# enter year and month and get the calendar-form 2D list

# take July for example
# Mon Tue Wed Thurs Fri Sat Sun
#               1    2   3   4 
#  5   6   7    8    9   10  11
#  12  13  14   15   16 ...
#  ...
#                        31

def month_list(year, month):
    (start, days) = calendar.monthrange(int(year), int(month))
    res = []
    flag = True
    flatten_list = [0 for i in range(0, start)] + [i for i in range(1, days+1)]
    padding = int(math.ceil(len(flatten_list)*1.0/7))*7 - len(flatten_list)
    flatten_list += [0 for i in range(0, padding)]
    start_index = 0
    while start_index != len(flatten_list):
        res.append(flatten_list[start_index:start_index+7])
        start_index += 7
    return (res, days)


def detail_month_list(year, month, res_list):
    (start, days) = calendar.monthrange(int(year), int(month))
    res = []
    flag = True
    flatten_list = [[] for i in range(0, start)] + res_list
    padding = int(math.ceil(len(flatten_list)*1.0/7))*7 - len(flatten_list)
    flatten_list += [[] for i in range(0, padding)]
    start_index = 0
    while start_index != len(flatten_list):
        res.append(flatten_list[start_index:start_index+7])
        start_index += 7
    return res

# res_list = [[0, 29, 12, 35, 6, 14], [28, 8, 13, 32, 10, 1], [15, 19, 16, 24, 3, 5], [27, 21, 7, 31, 36, 17], [26, 27, 34, 32, 12, 14], [25, 18, 11, 19, 16, 4], [5, 13, 29, 24, 31, 
# 23], [17, 3, 15, 21, 1, 7], [4, 31, 18, 1, 3, 27], [24, 11, 22, 23, 7, 20], [16, 9, 5, 26, 33, 21], [34, 29, 17, 10, 0, 32], [10, 29, 4, 22, 6, 9], [26, 21, 19, 14, 1, 16], [24, 34, 33, 32, 17, 5], [7, 3, 15, 25, 36, 30], [3, 30, 21, 31, 24, 26], [4, 15, 32, 19, 29, 20], [1, 11, 16, 10, 34, 13], [28, 6, 5, 14, 17, 23], [27, 24, 30, 34, 
# 16, 8], [5, 28, 10, 4, 32, 15], [1, 17, 9, 3, 2, 20], [26, 35, 14, 13, 31, 7], [34, 1, 17, 32, 30, 18], [15, 5, 7, 36, 2, 35], [3, 29, 19, 16, 8, 0], [27, 24, 10, 12, 14, 22], [33, 7, 19, 3, 2, 21], [16, 4, 29, 13, 25, 27], [23, 24, 1, 32, 34, 17]]

# print(month_list(2021,7))
# print()
# print(detail_month_list(2021,7,res_list))

            

