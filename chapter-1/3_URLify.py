"""
Chapter 1 - Problem 1.3 - URLify
Problem:
Write a method to replace all spaces in a string with '%20: You may assume that the string has sufficient space at the
end to hold the additional characters. and that you are given the "true" length of the string.

Solution:
1. Clarify the question:
Rephrase the question: We are given a string with or without spaces. And we need to replace all the spaces with '%20'.
Clarify assumptions: - are leading and trailing spaces significant? (We will assume no leading spaces.)

2. Inputs and outputs:
So we are taking in a string like 'this is a string.' and returning a string like 'this%20is%20a%20string.'

3. Test and edge cases:
edge: So we can also take in an empty string (one or more spaces) or none object as an input.
test: We can also have regular inputs like 'this is a string.' -> 'this%20is%20a%20string.'

4. Brainstorm solution:
This involves string modification. As strings are immutable in Python, we can create an auxiliary list and
copy characters one by one. The reason to use a list instead of an empty string is because string concatenation could
involve creating a copy of the string at each iteration when looping over the characters in the string. When a space
is encountered, replace it with %20. But this is not in place.

A simpler solution is to use the function 'replace' to replace space with %20. But this will also return a new string,
not an in-place solution. In addition, to remove trailing spaces, we use the method strip() which is also not in-place.

To do this close to in place, we can first find the required length of the new string, and add the required number of
trailing spaces. Then fill the string from the empty trailing spaces and working backwards. If we encounter spaces,
replace space with %20. We are moving backwards so that we don't need to move the elements to make room.

5. Runtime analysis:
Time complexity: O(N) in always-case as we need to iterate through the whole string.
Space complexity: O(1) for the in place solution.

6. Code
"""


# Solution 1, not in-place;
def replace_spaces2(input_str):
    if input_str is None or input_str.isspace():
        return -1

    input_str = input_str.strip()
    new_list = ['%20' if char == ' ' else char for char in input_str]

    return ''.join(new_list)


# Solution 2, not in place
def replace_spaces1(input_str):
    if (input_str is None) or (all(char == ' ' for char in input_str)):
        return -1

    return input_str.strip().replace(' ', '%20')


# Solution 3; close to in-place
def replace_spaces3(input_str, true_len):
    if (input_str is None) or (all(char == ' ' for char in input_str)):
        return -1

    # find required length for new string
    new_len = 0
    for i in range(true_len):
        if input_str[i] == ' ':
            new_len += 3
        else:
            new_len += 1

    # input_str has the required number of trailing spaces.
    input_str = list(input_str)
    input_str = input_str[:true_len] + [' '] * (new_len - true_len)

    for i in reversed(range(true_len)):
        if input_str[i] == ' ':
            input_str[new_len-3: new_len] = '%20'
            new_len -= 3
        else:
            input_str[new_len-1] = input_str[i]
            new_len -= 1

    return ''.join(input_str)


# 7. Test and debug
assert replace_spaces1('Mr John Smith     ') == 'Mr%20John%20Smith'
assert replace_spaces1(None) == -1
assert replace_spaces1('   ') == -1

assert replace_spaces2('Mr John Smith     ') == 'Mr%20John%20Smith'
assert replace_spaces2(None) == -1
assert replace_spaces2('   ') == -1

assert replace_spaces3('Mr John Smith      ', 13) == 'Mr%20John%20Smith'
assert replace_spaces3(None, 0) == -1
assert replace_spaces3('   ', 0) == -1


