def longest_palindromic_substring(s):
    if len(s) < 2:
        return s

    start = 0
    max_length = 1

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    for i in range(len(s)):
        palindrome1 = expand_around_center(i, i)
        palindrome2 = expand_around_center(i, i + 1)

        if len(palindrome1) > max_length:
            max_length = len(palindrome1)
            start = i - (len(palindrome1) - 1) // 2

        if len(palindrome2) > max_length:
            max_length = len(palindrome2)
            start = i - len(palindrome2) // 2

    return s[start:start + max_length]
