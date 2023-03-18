# Shuvam17:00
# In mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1:
# Fibonacci Sequence
# and
# Fibonacci Sequence 2
# for n > 1
# The beginning of the sequence is thus:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
# The function fib_fast(num) returns the fibonacci number Fn, of the given num as an argument.
#
# Examples
# fib_fast(5) ➞ 5
# fib_fast(10) ➞ 55
# fib_fast(20) ➞ 6765
# fib_fast(50) ➞ 12586269025





# In mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence, called the Fibonacci sequence, such
# that each number is the sum of the two preceding ones, starting from 0 and 1:
# F0 = 0, F1 = 1,
# and
# Fn = F(n-1) + F(n-2)
# for n > 1
# The beginning of the sequence is thus:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
# The function fib_fast(num) returns the fibonacci number Fn, of the given num as an argument.
#
# Examples
# fib_fast(5) ➞ 5
# fib_fast(10) ➞ 55
# fib_fast(20) ➞ 6765
# fib_fast(50) ➞ 12586269025

def fib_fast(num):
    i = 0
    a = 0
    b = 1
    while num>=i:
        c = a+b
        if num-2 == i:
            return c
        a = b
        b = c
        i+=1


# The function is given an unsorted list of timestamps as strings in military format: "00:00:00" -> "23:59:59". Find
# two timestamps that have a minimum duration between them among all possible pairs from the list. It's possible that
# more than one pair can have the minimum duration. Thus return the set of tuples, e.g. {(t1, t2), (t3, t4), etc}.
# The digital clock still goes around the clock, which is important for duration calculation. For example:
# t1 = "23:59:59"
# t2 = "00:00:01"
# Then (t1, t2) has d
# Examples
# min_time_diff(["01:10:00", "02:15:30", "01:10:10"]) ➞ {('01:10:00', '01:10:10')}
# min_time_diff(["23:59:59", "14:35:30", "00:00:00"]) ➞ {('23:59:59', '00:00:00')}
# min_time_diff(["23:59:25", "23:59:57", "17:20:30", "00:00:02", "17:20:35"]) ➞ {('23:59:57', '00:00:02'), ('17:20:30', '17:20:35')}
# min_time_diff(["00:00:08", "00:00:04", "00:00:12"]) ➞ {('00:00:08', '00:00:12'), ('00:00:04', '00:00:08')}
def min_time_diff(a_list):
    a = []
    b = ''

    d = a_list[0][-1] + a_list[1][-2]
    print(d[::-1])
    # d = a_list[0] + a_list[1][-2])
    # if a_list[0] > a_list[2]:
    #     print("abc")
    # else:
    #     print("123456789")
    # for i in a_list:
    #     # print(list(i))
    #     for j in i:
    #         d = a_list[0].(i[-1]+i[-2])









if __name__ == '__main__':
    # print(fib_fast(5))
    # print(fib_fast(10))
    # print(fib_fast(20))
    # print(fib_fast(50))

    print(min_time_diff(["01:10:00", "02:15:30", "01:10:10"]))
    print(min_time_diff(["23:59:25", "23:59:57", "17:20:30", "00:00:02", "17:20:35"]))
