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

    print(longest_common_ending("multiplication", "ration"))
    print(longest_common_ending("tptotent", "tent"))
