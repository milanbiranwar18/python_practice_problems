"""
# "Create a function that takes an array of numbers and return ""Boom!"" if the digit 7 appears in the array. Otherwise,
# return ""there is no 7 in the array"".
# Examples
# sevenBoom([1, 2, 3, 4, 5, 6, 7]) ➞ ""Boom!""
# // 7 contains the number seven.
# sevenBoom([8, 6, 33, 100]) ➞ ""there is no 7 in the array""
# // None of the items contain 7 within them.
# sevenBoom([2, 55, 60, 97, 86]) ➞ ""Boom!""
# // 97 contains the number seven."
"""
import re


def check_num_with_regex(a_list):

    check_num = re.compile(r'.\d*')
    a = check_num.match

"""
# "Write a function that returns True if two arrays, when combined, form a consecutive sequence. A consecutive sequence
# is a sequence without any gaps in the integers, e.g. 1, 2, 3, 4, 5 is a consecutive sequence, but 1, 2, 4, 5 is not.
# Examples
# consecutive_combo([7, 4, 5, 1], [2, 3, 6]) ➞ True
# consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]) ➞ False
# consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]) ➞ False
# consecutive_combo([44, 46], [45]) ➞ True"
"""


def consecutive_seq(a_list, b_list):


    a_list.extend(b_list)
    c_list = sorted(a_list)

    for i in c_list:
        if i+1 == c_list[i+1]:
            continue



    # print(a_list)
    # for i in range(len(a_list)-1):
    #     for j in range(i):
    #         if a_list[j] > a_list[j+1]:
    #             # a_list[j+1], a_list[j] = a_list[j], a_list[j+1]
    #             temp = a_list[j]
    #             a_list[j] = a_list[j+1]
    #             a_list[j+1] = temp
    #             print(a_list)

    # for i in range(1, len(a_list)):
    #     min_val = min(a_list[i])
    #     min_val_ind = a_list.index(min_val)
    #     temp =

    # print(a_list)

"""
# "Create a function that returns True if two lines rhyme and False otherwise. For the purposes of this exercise, two
# lines rhyme if the last word from each sentence contains the same vowels.
# Examples
# does_rhyme(""Sam I am!"", ""Green eggs and ham."") ➞ True
# does_rhyme(""Sam I am!"", ""Green eggs and HAM."") ➞ True
# # Capitalization and punctuation should not matter.
# does_rhyme(""You are off to the races"", ""a splendid day."") ➞ False
# does_rhyme(""and frequently do?"", ""you gotta move."") ➞ F
"""

def rhyme(a_str, b_str):

    for i in range(1, len(a_str)):
        for j in range(1, i):
            if (a_str[-j].lower() and isinstance(a_str[-j], str)) == (b_str[-j].lower() and isinstance(a_str[-j], str)):
                return True
            else:
                return






if __name__ == '__main__':
    # a_list = [1, 2, 3, 4, 5, 6, 7]
    # check_num_with_regex()

    # a_list = [7, 4, 5, 1]
    # b_list = [2, 3, 6]
    # # print(consecutive_seq(a_list, b_list))
    # consecutive_seq(a_list, b_list)

    a_str = "Sam I am!"
    b_str = "Green eggs and ham."
    rhyme(a_str, b_str)

