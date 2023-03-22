# Given an array of distinct integers, in-place replace each array element by its corresponding rank in the array.
# The minimum array element has the rank 1; the second minimum element has a rank of 2, and so on.
#
# Input : [10, 8, 15, 12, 6, 20, 1]
# Output: [4, 3, 6, 5, 2, 7, 1]
#
# Input : [0, 1, -1]
# Output: [2, 3, 1]

def list_element_rank(b_list):
    a = sorted(b_list)
    for i in range(len(b_list)):
        b_list[i] = a.index(b_list[i]) + 1

    print(b_list)

    # a_list = b_list
    # a = sorted(a_list)
    # for i in range(len(a_list)-1, 0, -1):
    #     for j in range(i):
    #         if a_list[j] > a_list[j+1]:
    #             temp = a_list[j+1]
    #             a_list[j + 1] = a_list[j]
    #             a_list[j] = temp
    # print(a_list)
    # a = a_list
    # a = sorted(b_list)
    # for i in range(len(b_list)):
    #     b_list[i] = a.index(b_list[i]) + 1
    #
    # print(b_list)


    b = []
    c = []
    # for i in range(len(a)):
    #     b.append(i+1)
    # for j in range(len(b)):
    #     if a.index(j)
    #     if a[j] in a_list:
    #         c.append(a_list[a[j]])
    # print(c)

    # for i in range(len(a_list)):
    #     a_list[i] = a.index(a_list[i]) + 1
    #
    # print(a_list)
    #


def replace_ranks(arr):
    n = len(arr)
    idx_arr = [i for i in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if arr[idx_arr[i]] > arr[idx_arr[j]]:
                temp = idx_arr[i]
                idx_arr[i] = idx_arr[j]
                idx_arr[j] = temp

    ranks = [0] * n
    for i in range(n):
        ranks[idx_arr[i]] = i + 1
    res_arr = [0] * n
    for i in range(n):
        res_arr[i] = ranks[i]
    return res_arr


if __name__ == '__main__':
    print(list_element_rank([10, 8, 15, 12, 6, 20, 1]))

    arr1 = [10, 8, 15, 12, 6, 20, 1]
    print(replace_ranks(arr1))
