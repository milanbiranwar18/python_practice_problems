# Input: '123'
# Output: One Two Three
#
# Input: '1223'
# Output: One DoubleTwo Three
#
# Input: '12333'
# Output: One Two TripleThree

def num_alf(a_str):
    a_dict = {'1':"One", '2':"Two", '3':"Three", '4':"Four", '5':"Five", '6':"Six", '7':"Seven", '8':"Eight", '9':"Nine", '0':"Zero"}
    b_dict = {2:"Double", 3:"Triple", 4:"FourTimes", 5:"FiveTimes"}
    b_str = ""
    key = 1
    i = 0
    # for i in range(len(a_str)-1):
    while i < len(a_str)-1:
        if a_str[i] != a_str[i+1]:
            b_str = b_str + " " + a_dict[a_str[i]]
        elif a_str[i] == a_str[i + 1]:
            key += 1

            if(a_str[i] != a_str[i + 1]) and (key in b_dict.keys()):
            # if a in b_dict.keys():
                b_str = b_str + " " + b_dict[key] + a_dict[a_str[i]]
                # i += 1
        i += 1
    if a_str[-1] == a_str[-2]:
        return b_str
    return b_str + " " + a_dict[a_str[-1]]

#
# def num_to_alfa(a_string):
#     a_dict = {'1': "One", '2': "Two", '3': "Three", '4': "Four", '5': "Five", '6': "Six", '7': "Seven", '8': "Eight",
#               '9': "Nine", '0': "Zero"}
#     b_dict = {2: "Double", 3: "Triple", 4: "FourTimes", 5: "FiveTimes"}
#
#     a_list = []
#     for i in range(len(a_string)-1):
#         if i < len(a_string) - 1 and a_string[i] == a_string[i + 1]:
#             digit_word = a_dict[a_string[i]]
#             i += 1
#         else:
#             digit_word = a_dict[a_string[i]]
#         a_list.append(digit_word)
#     print(a_list)
#     output_str = ' '.join(a_list)
#     print(output_str)


if __name__ == '__main__':
    print(num_alf('123'))
    print(num_alf('1223'))
    print(num_alf('1123'))
    print(num_alf('123333'))

    # print(num_to_alfa('123'))
