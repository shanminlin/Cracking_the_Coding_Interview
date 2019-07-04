"""
Chapter 1 - Problem 1.4 - Palindrome Permutation
Problem:
Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.

Solution:
1. Clarify the question:
Rephrase the question: We are given a string. And we need to determine whether it is a permutation of a palindrome.
Clarify assumptions: - Do we ignore spaces? (We will assume spaces are not significant.)
                     - Is it case sensitive? (We will assume case sensitivity.)

2. Inputs and outputs:
input: a string
output: True or False

3. Test and edge cases:
edge: So we can also take in an empty string or None object as an input.
test: We can also have regular inputs like 'aabaa' -> True; 'abba' -> True

4. Brainstorm solution:
First let's think about the characteristics of a string that satisfies the requirements: all (or all but one) of the characters are paired.
So we can use a hashtable to count how many times each character appears. Then loop through the hashtable to check the number of
odd counts.

5. Runtime analysis:
Time Complexity: O(N) in always case as we need to iterate the string
Space Complexity: O(N) in always case as we need to allocate space for the hashtable.

6. Code
"""


# Solution 1
from collections import Counter


def palindrome_permutation(input_str):
    if input_str is None or input_str == '':
        return -1

    # count character occurrence
    counter = Counter()
    for char in input_str:
        if char != ' ':
            counter[char] += 1

    # check the number of odd counts
    odd_count = sum(count % 2 == 1 for count in counter.values())
    # if spaces are significant
    # odd_count = sum(count % 2 == 1 for count in Counter(input_str).values())

    return odd_count <= 1


# Test and debug
def test():
    solutions = [palindrome_permutation]
    test_cases = [('a b ba', True),
                  ('ab BA', False),
                  ('', -1),
                  (None, -1),
                  ('Not a Palindrome', False)]

    for solution in solutions:
        for (test_input, result) in test_cases:
            if test_input is None or test_input == '':
                assert solution(test_input) == result
            try:
                assert solution(test_input) is result
                print('Passed')
            except AssertionError:
                print(solution.__name__, test_input, 'Failed')


test()