# TODO - Que = 1
def roman_int(s):
    r_num_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    b_str = 0
    # for i in range(len(r_str)-1):
    #     if r_str[i] < r_str[i+1]:
    #         b_str = b_str - r_num_dict[r_str[i]]
    #     else:
    #         b_str = b_str + r_num_dict[r_str[i]]
    #
    # print(b_str + r_num_dict[r_str[-1]])

    decimal_num = 0
    prev_num = 0
    for c in s[::-1]:
        curr_num = r_num_dict[c]
        if curr_num < prev_num:
            decimal_num -= curr_num
        else:
            decimal_num += curr_num
        prev_num = curr_num
    return decimal_num

# shuvam021

if __name__ == '__main__':
    print(roman_int('LVIII'))