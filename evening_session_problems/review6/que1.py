# "Create a function that takes an array of numbers and return ""Boom!"" if the digit 7 appears in the array. Otherwise, return ""there is no 7 in the array"".
#
# Examples
# sevenBoom([1, 2, 3, 4, 5, 6, 7]) ➞ ""Boom!""
# // 7 contains the number seven.
#
# sevenBoom([8, 6, 33, 100]) ➞ ""there is no 7 in the array""
# // None of the items contain 7 within them.
#
# sevenBoom([2, 55, 60, 97, 86]) ➞ ""Boom!""
# // 97 contains the number seven."
# Shuvam17:13
# "Write a function that returns True if two arrays, when combined, form a consecutive sequence. A consecutive sequence is a sequence without any gaps in the integers, e.g. 1, 2, 3, 4, 5 is a consecutive sequence, but 1, 2, 4, 5 is not.
#
# Examples
# consecutive_combo([7, 4, 5, 1], [2, 3, 6]) ➞ True
#
# consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]) ➞ False
#
# consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]) ➞ False
#
# consecutive_combo([44, 46], [45]) ➞ True"
# Shuvam17:23
# "Given a list of words in the singular form, return a set of those words in the plural form if they appear more than once in the list.
#
# Examples
# pluralize([""cow"", ""pig"", ""cow"", ""cow""]) ➞ { ""cows"", ""pig"" }
#
# pluralize([""table"", ""table"", ""table""]) ➞ { ""tables"" }
#
# pluralize([""chair"", ""pencil"", ""arm""]) ➞ { ""chair"", ""pencil"", ""arm"" }"
# Shuvam17:34
# Create a function that takes a list and string. The function should remove the letters in the string from the list, and return the list.
#
# Examples
# remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string") ➞ ["w"]
# remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon") ➞ ["b", "g", "w"]
# Shuvam17:35
# "Create a function that returns True if two lines rhyme and False otherwise. For the purposes of this exercise, two lines rhyme if the last word from each sentence contains the same vowels.
#
# Examples
# does_rhyme(""Sam I am!"", ""Green eggs and ham."") ➞ True
#
# does_rhyme(""Sam I am!"", ""Green eggs and HAM."") ➞ True
# # Capitalization and punctuation should not matter.
#
# does_rhyme(""You are off to the races"", ""a splendid day."") ➞ False
#
# does_rhyme(""and frequently do?"", ""you gotta move."") ➞ F