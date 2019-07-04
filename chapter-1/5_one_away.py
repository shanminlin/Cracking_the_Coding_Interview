"""
Chapter 1 - Problem 1.5 - One Away
Problem:
There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character.
Given two strings, write a function to check if they are one edit (or zero edit) away.

Solution:
1. Clarify the question:
Rephrase the question: We are given two strings, and we need to determine if they are different by one character.
Clarify assumptions: - Do we ignore spaces? (We will assume yes)
                     - Is it case sensitive? (We will assume yes)
                     - When the two strings are exactly the same (zero edit), we wll also return true? (Yes.)

2. Inputs and outputs:
input: two strings
output: True or False for whether they are different by one character.

3. Test and edge cases:
edge: So we can also take in an empty string or None object as an input.
test: We can also have regular input like this: python, pyton -> true
                                                python, aython -> true
                                                python, ppython -> true
                                                python, thon -> false

4. Brainstorm solution:
We can start by comparing the length of the two strings. If one or both of our input strings are none objects,
we would return -1 as taking length of a none object gives us error. If they are different by more than 1, we can immediately
return false. Then we are left with 2 cases: the length could also differ by exactly 1 or the same. For
these two cases, we can iterate over both strings until there is a difference, store that difference in a boolean.
For strings with equal length, we can check whether the remaining characters are the same. For strings with lengths
that differ by one, we need to shift the index of the longer string by 1 and compare the new character with the current
character of the shorter string. If one more difference is found, we can immediately return false.

5. Runtime analysis:
Time complexity: O(N) where N is the length of the shorter string in worse case. O(1) in best case when the length differ
by more than 1.
Space complexity: O(1) in always case.

6. Code
"""


def one_away(str1, str2):
    if str1 is None or str2 is None:
        return -1

    m = len(str1)
    n = len(str2)
    if abs(m - n) > 1:
        return False

    # if the length differ by 1 or 0
    diff_found = False
    i, j = 0, 0
    while i < m and j < n:
        if str1[i] != str2[j]:
            if diff_found:
                return False
            diff_found = True

            # match index
            if m > n:
                i += 1
            elif m < n:
                j += 1
            else:
                i += 1
                j += 1

        else:  # if current characters are the same
            i += 1
            j += 1
    return True

# 7. Test and debug


def test():
    test_cases = [('pale', 'ple', True),
                  ('pale', 'bale', True),
                  ('abc', 'abcd', True),
                  ('a', 'b', True),
                  ('', 'd', True),
                  ('pale', 'pale', True),
                  ('pale', 'apple', False),
                  ('abc', 'defd', False),
                  (None, 'a', -1),
                  ('', '', True)]

    for (test_input1, test_input2, result) in test_cases:
        if test_input1 is None or test_input2 is None:
            assert one_away(test_input1, test_input2) == result
        try:
            assert one_away(test_input1, test_input2) is result
            print('Passed')
        except AssertionError:
            print(test_input1, test_input2, 'Failed')


test()
