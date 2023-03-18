# Create a function that takes a list of lists and return the length of the missing list.
#
# Examples
# find_missing([[1], [1, 2], [4, 5, 1, 1], [5, 6, 7, 8, 9]]) ➞ 3
#
# find_missing([[5, 6, 7, 8, 9], [1, 2], [4, 5, 1, 1], [1]]) ➞ 3
#
# find_missing([[4, 4, 4, 4], [1], [3, 3, 3]]) ➞ 2

def find_missing(a_list):
    count = 1
    for i in range(len(a_list)-1, 0, -1):
        for j in range(i):
            if len(a_list[j]) > len(a_list[j+1]):
                temp = a_list[j]
                a_list[j] = a_list[j+1]
                a_list[j+1] = temp

    for i in a_list:
        if len(i) != count:
            return count
        count+=1



# Someone has attempted to censor my strings by replacing every vowel with a *, l*k* th*s. Luckily, I've been able to
# find the vowels that were removed.
# Given a censored string and a string of the censored vowels, return the original uncensored string.
# Example
# uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo") ➞ "Where did my vowels go?"
# uncensor("abcd", "") ➞ "abcd"
# uncensor("*PP*RC*S*", "UEAE") ➞ "UPPERCASE"

def uncensor(a_str, b_str):
    a_list = []
    for i in b_str:
        a_list.append(i)
    a = 0
    re_str = ''
    b_list = a_str.split(" ")
    for j, charact in enumerate(b_list):
        for k, char in enumerate(charact):
            if char != '*':
                re_str+=char
            else:
                re_str+=a_list[a]
                a+=1
        re_str+=" "

    return re_str

#
# Create a function that groups a list of numbers based on a size parameter. The size represents the maximum length of each sub-list.
#
# [1, 2, 3, 4, 5, 6], 3
# [[1, 3, 5], [2, 4, 6]]
# # Divide list into groups of size 3.
# [1, 2, 3, 4, 5, 6], 2
# [[1, 4], [2, 5], [3, 6]]
# # Divide list into groups of size 2.
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 4
# [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9]]
# # "Leftover" lists are okay.
# Examples
# group([1, 2, 3, 4], 2) ➞ [[1, 3], [2, 4]]
# group([1, 2, 3, 4, 5, 6, 7], 4) ➞ [[1, 3, 5, 7], [2, 4, 6]]
# group([1, 2, 3, 4, 5], 1) ➞ [[1], [2], [3], [4], [5]]
# group([1, 2, 3, 4, 5, 6], 4) ➞ [[1, 3, 5], [2, 4, 6]]

def group(a_list, num):
    abc = 0
    b_list = []
    for i, val in enumerate(a_list):
        if num == 1:
            b_list.insert(i, [val])
            continue
        elif i < num and val != abc:
            abc = a_list[i+1]
            b_list.append(a_list[i::2])

    return b_list





# Create a function that takes a function func and counts its arguments. Examining a function's bytecode using __code__ is disabled.
#
# Examples
# num_args(lambda: "") ➞ 0
# num_args(lambda x: "") ➞ 1
# num_args(lambda x, y: "") ➞ 2




if __name__ == '__main__':
    # print(find_missing([[1], [1, 2], [4, 5, 1, 1], [5, 6, 7, 8, 9]]))
    # print(find_missing([[5, 6, 7, 8, 9], [1, 2], [4, 5, 1, 1], [1]]))
    # print(find_missing([[4, 4, 4, 4], [1], [3, 3, 3]]))
    #
    #
    # print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))
    # print(uncensor("abcd", ""))
    # print(uncensor("*PP*RC*S*", "UEAE"))

    print(group([1, 2, 3, 4], 2))
    print(group([1, 2, 3, 4, 5, 6, 7], 4))
    print(group([1, 2, 3, 4, 5], 1))
    print( group([1, 2, 3, 4, 5, 6], 4))
