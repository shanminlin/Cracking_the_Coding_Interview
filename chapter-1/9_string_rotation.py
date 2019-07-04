"""
Chapter 1 - Problem 1.9 - String Rotation
Problem:
Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2,
write code to check if s2 is a rotation of s1 using only one call to isSubstring (e.g. "waterbottle" is a rotation of
"erbottlewat")

Solution:
1. Clarify the question:
Rephrase the question: We are given two strings s1 and s2, and a method isSubstring that indicates whether one word is
a substring of another. And we need to check whether s2 is a rotation of s1 using only one call to isSubstring.
Clarify assumptions: - Is it case sensitive? (We will assume not case sensitive.)
                     - Is whitespace significant? (We will assume whitespace is significant.)

2. Inputs and outputs:
So we are taking in two strings, s1 and s2, and returning a boolean for whether one is a rotation of the other

3. Test and edge cases:
edge: So we can also take in an empty string or none object as an input.
test: We can also have regular input like this: 'hello', 'llohe' -> True
                                                'hello', 'lolhe' -> False

4. Brainstorm solution:
If a string is a rotation of another string, they need to have the same length. So the first we can do is to compare the
length of the two strings. If they are different, we can immediately return false.
Then we may observe that if we concatenate s1, hellohello, the concatenated string contains all possible rotations of
that string. So we can check whether s2 is a substring of the concatenated s1+s1.

5. Runtime analysis:
Time complexity: O(N) in average case (for the operation of s1 in s2) where N is the length of the longer, concatenated string.
Space complexity: O(N) as we need to allocate extra space to double the length of s1.

6. Code
"""


def is_substring(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    return s1 in s2


def string_rotation(s1, s2):
    if s1 is None or s2 is None:
        return -1

    if len(s1) != len(s2):
        return False

    return is_substring(s2, s1+s1)


# 7.Test and debug
assert string_rotation(None, None) == -1
assert string_rotation('', '')
assert string_rotation('python', 'thonpy')
assert not string_rotation('python', 'ppthon')
assert not string_rotation('python', 'pyhton')