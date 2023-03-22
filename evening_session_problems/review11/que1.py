# Ques: 1
# Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.
# Examples
# format_date("11/12/2019") ➞ "20191211"
# format_date("12/31/2019") ➞ "20193112"
# format_date("01/15/2019") ➞ "20191501"


def format_date(f_date):
    a_list = f_date.split("/")
    a_str = ""
    for i in range(1,len(a_list)+1):
        a_str += a_list[-i]
    return a_str


# Ques: 2
# Write a function that takes a list of numbers and returns a list with two elements:
# The first element should be the sum of all even numbers in the list.
# The second element should be the sum of all odd numbers in the list.
# Example
# sum_odd_and_even([1, 2, 3, 4, 5, 6]) ➞ [12, 9] # 2 + 4 + 6 = 12 and 1 + 3 + 5 = 9
# sum_odd_and_even([-1, -2, -3, -4, -5, -6]) ➞ [-12, -9])
# sum_odd_and_even([0, 0]) ➞ [0, 0])

def sum_odd_and_even(a_list):
    even_num = 0
    odd_num = 0
    # list_even_odd_num = []
    for num in a_list:
        if num % 2 == 0:
            even_num += num
        else:
            odd_num += num

    # list_even_odd_num.append(even_num)
    # list_even_odd_num.append(odd_num)
    # return list_even_odd_num
    return [even_num, odd_num]


# Create a function that takes a dictionary of objects like { "name": "John", "notes": [3, 5, 4] } and returns a
# dictionary of objects like { "name": "John", "top_note": 5 }.
# Examples
# top_note({ "name": "John", "notes": [3, 5, 4] }) ➞ { "name": "John", "top_note": 5 }
# top_note({ "name": "Max", "notes": [1, 4, 6] }) ➞ { "name": "Max", "top_note": 6 }
# top_note({ "name": "Zygmund", "notes": [1, 2, 3] }) ➞ { "name": "Zygmund", "top_note": 3 }


def top_note(a_dict):
    result_dict = {}
    # for value in a_dict.values():
    #     if value == "notes":
    notes_list = a_dict.get("notes")
    for i in range(len(notes_list)-1, 0, -1):
        for j in range(i):
            if notes_list[j] > notes_list[j+1]:
                notes_list[j], notes_list[j+1] = notes_list[j+1], notes_list[j]
    result_dict.update({"name": a_dict.get("name"), "top_note": notes_list[-1]})
    # result_dict.update({})
    return result_dict


# Ques: 4
# Write a function that accepts the height and width (m, n) and an optional proc s and generates a list with m elements.
# Each element is a string consisting of either:
# The default character (hash #) repeating n times (if no proc is given).
# The character passed in through the proc repeating n times.
# Examples
# make_rug(3, 5, '#') ➞ [
#   "#####",
#   "#####",
#   "#####"
# ]
# make_rug(3, 5, '$')  ➞ [
#   "$$$$$",
#   "$$$$$",
#   "$$$$$"
# ]
# make_rug(2, 2, 'A')  ➞ [
#   "AA",
#   "AA"
# ]


def make_rug(row, col, patt):

    result_list = []
    for i in range(row):
        patt_str = ""
        for j in range(col):
            patt_str += patt
        result_list.append(patt_str)
    print(result_list)


# A list is given. Return a new list having the sum of all its elements except itself. For more clarity, check the
# examples below.
#
# Clarification
# [1, 2, 3, 4] = for first element => sum will be 2+3+4 = [9]
# [1, 2, 3, 4] = for second element => sum will be 1+3+4 = [9, 8]
# [1, 2, 3, 4] = for third element => sum will be 1+2+4 = [9, 8, 7]
# [1, 2, 3, 4] = for fourth element => sum will be 1+2+3 = [9, 8, 7, 6]
# Examples
# lst_ele_sum([1, 2, 3, 2, 1]) ➞ [8, 7, 6, 7, 8]
# lst_ele_sum([1, 2]) ➞ [2, 1]
# lst_ele_sum([1, 2, 3]) ➞ [5, 4, 3]
# lst_ele_sum([1, 2, 3, 4, 5]) ➞ [14, 13, 12, 11, 10]
# lst_ele_sum([10, 20, 30, 40, 50, 60]) ➞ [200, 190, 180, 170, 160, 150]

def lst_ele_sum(a_list):
    new_list = []
    for i, ele in enumerate(a_list):
        sum_num = 0
        for j in a_list:
            if a_list.index(ele) != a_list.index(j):
                sum_num += j
        print(sum_num)
            # print(sum_num)
        new_list.append(sum_num)


    print(new_list)

if __name__ == '__main__':
    # print(format_date("11/12/2019"))
    # print(format_date("12/31/2019"))
    # print(format_date("01/15/2019"))

    # print(sum_odd_and_even([1, 2, 3, 4, 5, 6]))
    # print(sum_odd_and_even([-1, -2, -3, -4, -5, -6]))
    # print(sum_odd_and_even([0, 0]))

    # print(top_note({ "name": "John", "notes": [3, 5, 4] }))
    # print(top_note({ "name": "Max", "notes": [1, 4, 6] }))
    # print(top_note({ "name": "Zygmund", "notes": [1, 2, 3] }))

    print(make_rug(3, 5, '#'))

    print(lst_ele_sum([1, 2, 3, 2, 1]))