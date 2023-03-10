def merge_sort(list):

    if len(list) > 1:
        left_list = list[:len(list) // 2]
        right_list = list[len(list) // 2:]

        # recursion
        merge_sort(left_list)
        merge_sort(right_list)

        # merge
        i = 0  # left_list idx
        j = 0  # right_list idx
        k = 0  # merged list idx
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list[k] = left_list[i]
                i += 1
            else:
                list[k] = right_list[j]
                j += 1
            k += 1

        while i < len(left_list):
            list[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            list[k] = right_list[j]
            j += 1
            k += 1


if __name__ == '__main__':

    list_test = [2, 3, 1, 7, 4, 5, 6, 0]
    print("Before sorting", list_test)
    merge_sort(list_test)
    print("After sorting", list_test)