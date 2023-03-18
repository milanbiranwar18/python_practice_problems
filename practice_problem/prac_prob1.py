# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could
# represent. Return the answer in any order.
#
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any
# letters.
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

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


def sample(a_srt):
    a_dict = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
    a = []
    a.append("")
    for i in a_srt:
        c = a_dict.get(i)
        d = []
        for j in a:
            for k in c:
                d.append(j + k)
            a = d
    return a


def letter_combinations(digits):
    if not digits:
        return []
    digit_to_letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    results = []
    def backtrack(combination, next_digits):
        if not next_digits:
            results.append(combination)
            return
        for letter in digit_to_letters[next_digits[0]]:
            backtrack(combination + letter, next_digits[1:])
    backtrack("", digits)
    return results


def longest_common_ending(a_str, b_str):
    c_str = ""

    if len(a_str) < len(b_str):
        for i in range(1, len(a_str)):
            if a_str[-i] == b_str[-i]:
                c_str += b_str[-i]
    else:
        for j in range(1, len(b_str)+1):
            if a_str[-j] == b_str[-j]:
                c_str += b_str[-j]
    d_str = c_str[::-1]
    return d_str


if __name__ == '__main__':
    # print(letterCombinations("234"))
    # print(possible_letter_combinations("23"))
    # print(possible_letter_combinations("234"))

    # print(longest_common_ending("multiplication", "ration"))
    # print(longest_common_ending("tptotent", "tent"))

    print(sample("23"))






