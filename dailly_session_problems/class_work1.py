# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted
# in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n,
#  return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.
#
#  Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
#
# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false




# Given an integer array, find all distinct combinations of a given length `k`. The solution should return a set
# containing all the distinct combinations, while preserving the relative order of elements as they appear in the array.
#
# Input : [2, 3, 4], k = 2
# Output: {(2, 3), (2, 4), (3, 4)}
#
# Input : [1, 2, 1], k = 2
# Output: {(1, 2), (1, 1), (2, 1)}
#
# Input : [1, 1, 1], k = 2
# Output: {(1, 1)}
#
# Input : [1, 2, 3], k = 4
# Output: {}
#
# Input : [1, 2], k = 0
# Output: {()}


def distinct_combinations(arr, k):
    # c = set()
    # print(type(c))

    # for i in range(len(a_list)):
    #     for j in a_list[i::]:
    #         # for j, ele in enumerate(a_list):
    #         a = []
    #         a.append(a_list[i])
    #         a.append(a_list[j])
    #         print(a)
    #         b = tuple(a)
    #         c.add(b)
    # print(c)
    #     # for j in a_list:
    #     #     if a_list.index(ele) != a_list.index(j):
    #     #
    if k == 1:
        return set([(x,) for x in arr])  # bas
    res = set()
    for i in range(len(arr)):
            first = arr[i]
            remaining = arr[i+1:]
            for comb in distinct_combinations(remaining, k-1):
                res.add((first,) + comb)  # add the first element to each combination of the remaining elements

    return res


def find_combinations(a_list, k):
    n = len(a_list)
    comb_set = set()
    for i in range(n):
        if k == 1:
            comb_set.add((a_list[i],))
        else:
            for j in range(i+1, n):
                for c in find_combinations(a_list[j:], k-1):
                    comb_set.add((a_list[i],) + c)
    return comb_set



#
# Given a string, return all combinations of non-overlapping substrings of it.
#
# Input : 'ABC'
# Output: {('A', 'B', 'C'), ('A', 'BC'), ('AB', 'C'), ('ABC')}
#
# Input : 'ABCD'
# Output: {('A', 'B', 'C', 'D'), ('A', 'B', 'CD'), ('A', 'BC', 'D'), ('A', 'BCD'), ('AB', 'C', 'D'), ('AB', 'CD'), ('ABC', 'D'), ('ABCD')}


def str_combinations(s):
    n = len(s)
    if n == 1:
        return {(s,)}
    combinations = set()
    for i in range(1, n):
        for c in find_combinations(s[i:]):
            combinations.add((s[:i],) + c)
    combinations.add((s,))
    return combinations





if __name__ == '__main__':
    # print(distinct_combinations([2, 3, 4], 2))
    # print(distinct_combinations([1, 2, 1], 2))
    # print(distinct_combinations([1, 1, 1], 2))
    #
    # print(find_combinations([2, 3, 4], 2))
    # print(find_combinations([1, 2, 1], 2))
    # print(find_combinations([1, 1, 1], 2))

    print(str_combinations('ABC'))