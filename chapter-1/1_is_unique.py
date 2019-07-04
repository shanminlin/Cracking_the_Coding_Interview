"""
Chapter 1 - Problem 1.1 - Is Unique
Problem:
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data
structures?

Solution:
1. Clarify the question:
Rephrase the question: So we are given a string. And we need to determine whether it contains only unique characters, no repeats.
Check assumptions: - To clarify how many characters are available to us, are the characters ASCII or Unicode? (We'll assume Unicode.)
                   - And is it supposed to be case sensitive? (We will assume it's not case sensitive. So 'aAbc' is not unique.)

2. Inputs and outputs:
So we're taking in a string and returning true or false for whether it has only unique characters.

3. Test and edge cases:
edge: So we can also take in an empty string or None object as an input.
test: We can also have regular input like this: 'hello' -> False
                                                 'abcd' -> True
                                                 'a' -> True
4. Brainstorm solution:
If we were to take an empty string, or string having only one character, or a none object, we would return True because
there would be no repeats for sure.

But we could also have inputs like 'aabcd'. In this case, we could use a set, because a set in python, which is implemented
as a hashtable, stores only unique characters. After we pass the string to a set, we can then just compare the length of
that set and the original string. If they are equal, we could return true. The time complexity would be linear O(N) in always-case
as we need to iterate through the whole string. Other steps like .lower() is also O(N) in always-case; getting the
length of the set and the string takes only constant time. The space complexity would also be linear O(N) in always case as
we need extra space to store the characters.

If we consider the use case of long strings that contain non-unique characters, there could be an optimization, that is
to stop the iteration early if we have found a non-unique character. So in this case, we need to iterate through the string
and keep track of the characters seen. If we encounter a character that is already seen before, we could immediately return false.
So which data structure to use to store the seen characters? we could use a set or a list. However, as a set takes constant time
for membership test in average case whereas a list takes linear time in average case, and we don't need to characters to be ordered, we would use a set.
The time complexity overall would be O(N) in worse case. The space complexity would also be O(N) in worse case.

What if we cannot use additional data structures?
In this case, we could use a bit vector. In Python, integers are either 32 or 64 bits depending on the system. Assuming
32-bit system, we can use the bits of a number to indicate the presence or absence of a characters. But we have to assume
the input string contains only lower alphabet a-z as we only have 32 bits. We will initiate an integer variable and treat
it as a vector of 26 boolean variables. These are set to 0 initially. Then iterate through the string, each time we see
a character, we modify the bit to 1 at the position defined by the difference between the ascii value of that character and 'a'.
If it is already 1, we have seen this character before and we have found a repeat. In this case, we don't need to allocate
space of the boolean variables, we operate on the bits of the number. So the space complexity would be O(1) in always-case.
The time complexity would be O(N) in worse-case.

5. Runtime analysis:
time complexity: O(N) in always case for solution 1, O(N) in worse case for solution 2 and 3.
space complexity: - O(N) for solution 1 and 2
                  - O(1) for solution 3.

6. Code
"""
# solution 1
def is_unique1(input_str):
    if input_str is None or len(input_str) < 2:
        return True

    input_str = input_str.lower()
    return len(set(input_str)) == len(input_str)

# solution 2
def is_unique2(input_str):
    if input_str is None or len(input_str) < 2:
        return True

    input_str = input_str.lower()
    seen_chars = set()
    for char in input_str:
        if char in seen_chars:
            return False
        seen_chars.add(char)
    return True

# solution 3
def is_unique3(input_str):
    # validate assumption
    assert all('a' <= char <= 'z' for char in input_str)

    char_size = 26
    if len(input_str) > char_size:
        return False

    seen_chars = 0
    for char in input_str:
        mask_char = 1 << (ord(char) - ord('a'))
        if seen_chars & mask_char:
            return False
        seen_chars |= mask_char
    return True

# 7 Test and debug
def test():
    solutions = [is_unique1, is_unique2]
    test_cases = [('', True), (None, True), ('abcd1', True), ('a', True), ('aA', False), ('aabc', False)]

    for solution in solutions:
        for (test, result) in test_cases:
            try:
                assert solution(test) is result
                print('Passed')
            except AssertionError:
                print(solution.__name__, test, 'Failed')

test()

assert is_unique3('a')
assert not is_unique3('aabc')
