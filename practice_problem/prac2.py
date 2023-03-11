def palindrom_num(num):
    result = 0
    number = num
    while num > 0:
        temp = num % 10
        result = (result * 10) + temp
        num //= 10
    if result == number:
        return True
    return False


def roman_to_int(r_str):  # LVIII
    r_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    for i in range(len(r_str) - 1):
        if r_dict[r_str[i]] < r_dict[r_str[i + 1]]:
            res = res - r_dict[r_str[i]]
        else:
            res = res + r_dict[r_str[i]]
    return res + r_dict[r_str[-1]]


def move_zero(nums):
    for i in nums:
        if i == 0:
            nums.remove(0)
            nums.append(0)
    return nums


def fill_none(a_list):  # [1, None, 2, 3, None, None, 5, None]
    val = 0
    res = []
    for i in a_list:
        if i is not None:
            res.append(i)
            val = i
        else:
            res.append(val)
    return res


def max_min(data):
    a = data[0]
    b = data[0]
    for i in data:
        if i > a:
            a = i
        elif i < b:
            b = i
    print("maximum number is", a, "minimum number is", b)


def reverse_string(text):
    index = -1
    for i in range(len(text) - 1, len(text)//2, -1):  # len(text) = 17
        if text[i].isalpha():
            temp = text[i]
            while True:
                index += 1
                if text[index].isalpha():
                    text[i] = text[index]
                    text[index] = temp
                    break
    return text


def str_to_dic(a_string):
    a_dict = {}
    for i in a_string:
        a_dict.update({i: a_string.count(i)})
    print(a_dict)


def remove_duplicate_value(my_list):
    dup = []
    for i in my_list:
        if i not in dup:
            dup.append(my_list[i])
    return dup


def remove_duplicates(nums):
    count = 1
    for i in range(1, len(nums)):
        for j in range(i-1, i):
            if nums[i] == nums[j]:
                continue
            else:
                nums[count] = nums[i]
                count += 1
    return count


if __name__ == '__main__':
    # obj = palindrom_num(121)
    # print(obj)

    print(roman_to_int('LVIII'))

    # a_list1 = [0, 1, 0, 3, 12]
    # a_list2 = [1, 7, 0, 0, 8, 0, 10, 12, 0, 4]
    # print(move_zero(a_list1))
    # print(move_zero(a_list2))

    a_list1 = [1, None, 2, 3, None, None, 5, None]
    print(fill_none(a_list1))

    # data = [0, 10, 15, 40, -5, 42, 17, 28, 75]
    # max_min(data)

    # a_string = 'python practice'
    # str_to_dic(a_string)

    # string = "a!!!b.c.d,e'f,ghi"
    # print("Input string: ", string)
    # string = reverse_string(list(string))
    # print("Output string: ", "".join(string))

    # my_list = [1, 2, 2, 3, 4, 4, 5, 5]
    # obj = remove_duplicate_value(my_list)
    # print(obj)


