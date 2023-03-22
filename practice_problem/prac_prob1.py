# TODO : Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number
#  could represent. Return the answer in any order.
#  A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any
#  letters.
#  Input: digits = "23"
#  Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

def possible_letter_combinations(a_str):
    a_dict = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
    comb_list = []
    comb_list.append('')
    for digit in a_str:
        letters = a_dict[digit]
        new_comb_list = []
        for combination in comb_list:
            for letter in letters:
                new_comb_list.append(combination + letter)
        comb_list = new_comb_list
    return comb_list


def letter_combinations(digits):
    if not digits:
        return []
    digit_to_letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv",
                        "9": "wxyz"}
    results = []

    def backtrack(combination, next_digits):
        if not next_digits:
            results.append(combination)
            return
        for letter in digit_to_letters[next_digits[0]]:
            backtrack(combination + letter, next_digits[1:])

    backtrack("", digits)
    return results


# TODO: Find longest common ending words from given inputs
#  Input : "multiplication", "ration"
#  output : ation
#  Input : "tptotent", "tent"
#  output : tent

def longest_common_ending(a_str, b_str):
    c_str = ""

    if len(a_str) < len(b_str):
        for i in range(1, len(a_str)):
            if a_str[-i] == b_str[-i]:
                c_str += b_str[-i]
    else:
        for j in range(1, len(b_str) + 1):
            if a_str[-j] == b_str[-j]:
                c_str += b_str[-j]
    d_str = c_str[::-1]
    return d_str


# TODO: Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#  An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
#  the original letters exactly once.
#  Example 1:
#  Input: strs = ["eat","tea","tan","ate","nat","bat"]
#  Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#  Example 2:
#  Input: strs = [""]
#  Output: [[""]]
#  Example 3:
#  Input: strs = ["a"]
#  Output: [["a"]]


def group_anagrams(strs_list):
    strs_table = {}
    for string in strs_list:
        sorted_string = ''.join(sorted(string))
        if sorted_string not in strs_table:
            strs_table[sorted_string] = []
        strs_table[sorted_string].append(string)
    return list(strs_table.values())


# TODO: Pow(x, n) Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
#   Example 1:
#   Input: x = 2.00000, n = 10
#   Output: 1024.00000
#   Example 2:
#   Input: x = 2.10000, n = 3
#   Output: 9.26100
#   Example 3:
#   Input: x = 2.00000, n = -2
#   Output: 0.25000
#   Explanation: 2-2 = 1/22 = 1/4 = 0.25

def pow(x, n):
    if n == 0 or x == 1:
        return 1
    val = pow(x, n // 2)
    val *= val
    if n % 2 == 0:
        return val
    else:
        if n < 0:
            return val * (1 / x)
        return val * x


# TODO: Given an integer array nums, find the
#  subarray  with the largest sum, and return its sum.
#  Example 1:
#  Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#  Output: 6
#  Explanation: The subarray [4,-1,2,1] has the largest sum 6.
#  Example 2:
#  Input: nums = [1]
#  Output: 1
#  Explanation: The subarray [1] has the largest sum 1.
#  Example 3:
#  Input: nums = [5,4,-1,7,8]
#  Output: 23
#  Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

def max_sub_array(nums):
    max_so_far = nums[0]
    max_ending_here = nums[0]
    for i in range(1, len(nums)):
        max_ending_here = max(nums[i], max_ending_here + nums[i])
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


# TODO: Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
#  Example 1:
#  Input: num = 38
#  Output: 2
#  Explanation: The process is
#  38 --> 3 + 8 --> 11
#  11 --> 1 + 1 --> 2
#  Since 2 has only one digit, return it.
#  Example 2:
#  Input: num = 0
#  Output: 0

def adding_num(num):
    num1 = 0

    while num > 0:
        rem = num % 10
        num1 += rem
        num = num // 10

    num2 = 0
    while num1 > 0:
        rem = num1 % 10
        num2 += rem
        num1 = num1 // 10
        
    return num2


# TODO : Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same
#  color are adjacent, with the colors in the order red, white, and blue.
#  We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
#  You must solve this problem without using the library's sort function.
#  Example 1:
#  Input: nums = [2,0,2,1,1,0]
#  Output: [0,0,1,1,2,2]
#  Example 2:
#  Input: nums = [2,0,1]
#  Output: [0,1,2]

def sort_colors(nums):
    red, white, blue = 0, 0, len(nums) - 1
    while white <= blue:
        if nums[white] == 0:
            nums[red], nums[white] = nums[white], nums[red]
            white += 1
            red += 1
        elif nums[white] == 1:
            white += 1
        else:
            nums[white], nums[blue] = nums[blue], nums[white]
            blue -= 1
    return nums

#
# #Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique
# element appears at most twice. The relative order of the elements should be kept the same.
#
# Since it is impossible to change the length of the array in some languages, you must instead have the result be
# placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates,
# then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first
# k elements.
# Return k after placing the final result in the first k slots of nums.
# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1)
# extra memory.
# Custom Judge:
# The judge will test your solution with the following code:
#
# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length
#
# int k = removeDuplicates(nums); // Calls your implementation
#
# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.
# Example 1:
# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3
# respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:
#
# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3
# respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
#




if __name__ == '__main__':
    # print(letterCombinations("234"))
    # print(possible_letter_combinations("23"))
    # print(possible_letter_combinations("234"))

    # print(longest_common_ending("multiplication", "ration"))
    # print(longest_common_ending("tptotent", "tent"))

    # print(sample("23"))

    # print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # print(group_anagrams([""]))
    # print(group_anagrams(["a"]))

    # print(pow(2.00000, 10))
    # print(pow(2.10000, 3))
    # print(my_pow(2.00000, -2))

    # print(max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))

    # print(adding_num(38))
    # print(adding_num(0))

    print(sort_colors([2,0,2,1,1,0]))
    print(sort_colors([2,0,1]))