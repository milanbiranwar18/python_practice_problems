# Length of Last Word
# Given a string s consisting of words and spaces, return the length of the last word in the string.
#
# A word is a maximal substring consisting of non-space characters only.
#
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
#
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

def length_last_word(s):

    x = s.split()
    a = 0
    for i in x[-1]:
        a+=1
    return a


def length_of_last_word(s):
    if len(s) == 1 and s[0] != ' ':
        return 1
    n = len(s) - 1
    i = len(s) - 1
    while i >= 0:
        if s[i] == ' ':
            if n - i != 0 and s[i+1] != ' ':
                return n - i
            else:
                n = i - 1
        i -= 1
    if s[0] != ' ':
        return n + 1
    return 0


# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
# Input: nums = [3,3], target = 6
# Output: [0,1]

def int_num_tar_num(a_list):
    target = 9
    new_list = []
    for i in range(len(a_list)-1):
        a = a_list[i] + a_list[i+1]
        if a == target:
            new_list.append(i)
            new_list.append(i+1)
    return new_list


if __name__ == '__main__':
    # s = "Hello World"
    # s = "   fly me   to   the moon  "
    # print(length_last_word(s))
    # print(length_of_last_word(s))

    a_list = [2,7,11,15]
    # a_list = [3,2,4]
    n_list = int_num_tar_num(a_list)
    print(n_list)
