
# Write a function that divides a phrase into word buckets, with each bucket containing n or fewer characters.
# Only include full words inside each bucket.
# Examples
# bucketize("she sells sea shells by the sea", 10)
# ➞ ["she sells", "sea shells", "by the sea"]
# bucketize("the mouse jumped over the cheese", 7)
# ➞ ["the", "mouse", "jumped", "over", "the", "cheese"]
# bucketize("fairy dust coated the air", 20)
# ➞ ["fairy dust coated", "the air"]
# bucketize("a b c d e", 2)
# ➞ ["a", "b", "c", "d", "e"]

def bucketize(a_str, n):
    a_list = a_str.split(" ")
    a = []
    b = ''
    for j in range(len(a_str)):
        for b_str in a_list:
            if len(b) + len(b_str) <= n:
                for i in b_str:
                    if n >= len(b_str):
                        b+=i
                b += " "
        a.append(b)
    print(a)


def bucketize1(phrase, n):
    words = phrase.split()
    buckets = []
    current_bucket = ""
    for i, word in enumerate(words):
        if len(current_bucket) + len(word) <= n:
            current_bucket += " " + word if current_bucket else word
        else:
            buckets.append(current_bucket)
            current_bucket = word
    if current_bucket:
        buckets.append(current_bucket)
    return buckets

# Given an integer n, create a function that returns the length of the repeating cycle of the sequence 1/n. If the
# cycle is non-repetitive, return -1.
#
# repeating_cycle(13) ➞ 6
# # 1/13 = 0.076923 076923 076923 076923 ...
# # length of `076923` is 6.
# Examples
# repeating_cycle(5) ➞ -1
# # 1/5 = 0.2 (non-repeative)
#
# repeating_cycle(33) ➞ 2
# # 1/33 = 0.03 03 03 03 03 03 03 03
# # length of `03` is 2
#
# repeating_cycle(197) ➞ 98

def len_repeating_cycle(num):
    f_num = 1/num
    b_str = str(f_num)
    c_list = b_str.split(".")
    a = 1
    for a_str in c_list[1].split(" "):
        for i in range(len(a_str)-1):
            if a_str[0] == a_str[i+1]:
                break
            a+=1
    return a


def repeating_cycle(n):
     if n % 2 == 0 or n % 5 == 0:
      return -1
     r = 10 % n
     c = 1
     while r != 1:
      r = r * 10 % n
      c += 1
     return c



if __name__ == '__main__':

    # print(bucketize("she sells sea shells by the sea", 10))
    # print(bucketize("the mouse jumped over the cheese", 7))
    # print(bucketize("fairy dust coated the air", 20))
    # print(bucketize("a b c d e", 2))

    print(bucketize1("she sells sea shells by the sea", 10))
    print(bucketize1("the mouse jumped over the cheese", 7))
    print(bucketize1("fairy dust coated the air", 20))
    print(bucketize1("a b c d e", 2))

    # print(len_repeating_cycle(13))
    # print(len_repeating_cycle(5))
    # print(len_repeating_cycle(33))

    # print(repeating_cycle(13))
    # print(repeating_cycle(5))
    # print(repeating_cycle(33))
    # print(repeating_cycle(197))
