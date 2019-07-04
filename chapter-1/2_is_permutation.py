"""
Chapter 1 - Problem 1.2 - Check Permutation
Problem:
Given two strings, write a method to decide if one is a permutation of the other.

Solution:
1. Clarify the question:
Rephrase/repeat the question: We are given two strings, And we need to determine if one is a permutation of the other.
Clarify assumptions: - Is the permutation comparison case sensitive? (We will assume it's not case sensitive.)
                     - Is whitespace significant? (We will assume whitespace is not significant.)
                     - permutation means they have same characters with the same number of occurrence but in different order?

2. Inputs and outputs:
So we are taking in two strings, and returning true or false for whether one is a permutation of the other.

3. Test and edge cases:
edge: So we can also take in an empty string or none object as an input.
test: We can also have regular inputs like 'python' and 'pthoyn'.

4. Brainstorm solution:
So we can first compare the length of the two strings. If the lengths are different, the two strings definitely cannot be
permutations of each other and we can immediately return false.
If the strings have the same length, we can use a dictionary to store each character and its occurrence in the string as
we don't need the characters to be ordered. Then compare the two dictionaries. The time complexity would be linear, O(N),
in always-case as we need to iterate through the whole strings. The space complexity would be O(N) as we need to allocate
additional spaces for the two dictionaries.

One optimization is that we could just use one dictionary for the 1st string and membership test for the 2nd string. As
we iterate through the characters in the 2nd string, we decrement the character count in the dictionary by 1. If we encounter
a character in the 2nd string not stored in the dictionary, we could immediately return false.

In practice, we could actually use Python's built-in sort function to sort the two strings. Though the sort function,
which uses timsort, has O(nlog(n)) in worse and average case, O(N) in best-case, thus asymptotically slower than the
previous solutions, timsort is implemented and running in C so it is faster particularly for shorter strings.

5. Runtime analysis:
Time complexity: O(N) where N is the length of the strings when they have same length; otherwise, it would be O(1)
Space complexity: O(N)

6. Code
"""
# Solution 1 
def is_permutation1(str1, str2):
    if str1 is None or str2 is None:
        return -1

    if len(str1) != len(str2):
        return False

    # remove all white spaces and convert letters to lower case
    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()

    # we can use a dict or use Counter(). In Python3, Counter() is faster.
    dict1, dict2 = {}, {}
    for char in str1:
        dict1[char] = dict1.get(char, 0) + 1
    for char in str2:
        dict2[char] = dict2.get(char, 0) + 1
    return dict1 == dict2

# Solution 2
from collections import Counter

def is_permutation2(str1, str2):
    if str1 is None or str2 is None:
        return -1

    if len(str1) != len(str2):
        return False

    # remove all white spaces and convert letters to lower case
    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()

    counter = Counter()
    for char in str1:
        counter[char] += 1
    for char in str2:
        if counter[char] == 0:
            return False
        counter[char] -= 1
    return True

# Solution 3
def is_permutation3(str1, str2):
    if str1 is None or str2 is None:
        return -1

    if len(str1) != len(str2):
        return False

    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()

    return sorted(str1) == sorted(str2)

# 7 Test and debug
def test():
    solutions = [is_permutation1, is_permutation2, is_permutation3]
    test_cases = [('Abcd', 'dcab', True),
                  ('12a b', '2ab 1', True),
                  ('', '', True),
                  ('abcd', 'abc', False),
                  ('abcd', 'abbd', False),
                  (None, None, -1)]

    for solution in solutions:
        for (test_input1, test_input2, result) in test_cases:
            if test_input1 is None or test_input2 is None:
                assert solution(test_input1, test_input2) == result
            try:
                assert solution(test_input1, test_input2) is result
                print('Passed')
            except AssertionError:
                print(solution.__name__, test, 'Failed')

test()