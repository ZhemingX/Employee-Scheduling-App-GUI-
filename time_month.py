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


            

