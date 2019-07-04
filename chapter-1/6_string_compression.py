"""
Chapter 1 - Problem 1.6 - String Compression
Problem:
Implement a method to perform basic string compression using the counts of repeated characters. For example,
the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the
original string, your method should return the original string. You can assume the string has only uppercase
and lowercase letters (a - z).

Solution:
1. Clarify the question:
Rephrase the question: We are given a string. And we need to compress the string using character counts.
Clarify assumptions: - only uppercase and lowercase letters. So there will be no confusion when we have 10 or more
                        consecutive identical characters.

                     - case sensitive? (We will assume case sensitivity.)

2. Inputs and outputs:
input: a string
output: a compressed string, or original string if the compressed string is not shorter than the original string.

3. Test and edge cases:
edge: So we can also take in an empty string or None object as an input.
test: We can also have regular input like this: 'aaaabbbaacccc' -> 'a4b3a2c4'

4. Brainstorm solution:
We iterate through the string, check if the current character is the same as the previous character. If so, add count
to the previous character; Otherwise, add previous character and count to the compressed string.
As python string is immutable, string concatenation (adding to a string) involves creating a copy of that string,
particulary for long string where there is no overallocation of space. Then at each iteration a reallocation (linear time)
would be performed, and the full runtime would be quadratic in worse-case. So we will append to a list instead.
For very long string, we can also use generator to save memory.

5. Runtime analysis:
Time complexity: O(N) in always-case as we need to iterate through the whole string.
Space complexity: O(N) as we need to allocate space for the compressed string.  In the worst case where there are no
consecutive characters, we need twice as long as the input.

6. Code
"""


# Solution 1
def compress1(input_str):
    if (input_str is None) or (len(input_str) < 3):
        return input_str

    compressed_str = []
    prev_char = input_str[0]
    count = 1
    for char in input_str[1:]:
        if char == prev_char:
            count += 1
        else:
            compressed_str.append(prev_char + str(count))
            prev_char = char
            count = 1

    # Add last character count
    compressed_str.append(prev_char + str(count))

    compressed_str = ''.join(compressed_str)
    if len(compressed_str) >= len(input_str):
        return input_str

    return compressed_str


# Solution 2
from itertools import groupby


def compress2(input_str):
    if (input_str is None) or (len(input_str) < 3):
        return input_str

    compressed_str = ''.join(char + str(sum(1 for _ in group)) for char, group in groupby(input_str))

    return min(input_str, compressed_str, key=len)


# 7. Test and debug
def test():
    solutions = [compress1, compress2]
    test_cases = [('aaaabbbaacccc', 'a4b3a2c4'),
                  ('aaaabbbbcde', 'a4b4c1d1e1'),
                  ('', ''),
                  (None, None)]

    for solution in solutions:
        for (test_input, result) in test_cases:
            if test_input is None:
                assert solution(test_input) is result
            try:
                assert solution(test_input) == result
                print('Passed')
            except AssertionError:
                print(solution.__name__, test_input, 'Failed')


test()



