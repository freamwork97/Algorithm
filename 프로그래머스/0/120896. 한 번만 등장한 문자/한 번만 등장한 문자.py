from collections import Counter

def solution(s):
    freq = Counter(s)
    single_chars = sorted([char for char in freq if freq[char] == 1])
    return ''.join(single_chars)
