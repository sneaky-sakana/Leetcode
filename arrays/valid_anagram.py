from collections import Counter

class Solution:
    def valid_anagram_brute(self, s: str, t: str):
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

    def valid_anagram_optimal1(self, s: str, t: str):
        if len(s) != len(t):
            return False

        char_hash = {}
        for char in s:
            char_hash[char] = 1 + char_hash.get(char, 0)
        for char in t:
            char_hash[char] = -1 + char_hash.get(char, 0)
        for char in char_hash:
            if char_hash[char] != 0:
                return False
        return True

    def valid_anagram_optimal2(self, s: str, t: str):
        if len(s) != len(t):
            return False

        char_array = [0] * 26
        for char in s:
            char_array[ord(char) - ord('a')] += 1
        for char in t:
            char_array[ord(char) - ord('a')] -= 1
        for cnt in char_array:
            if cnt != 0:
                return False
        return True

if __name__=="__main__":
    problem_input = input()
    strings = problem_input.split(',')
    sol = Solution()
    result = sol.valid_anagram_brute(strings[0], strings[1])
    result1 = sol.valid_anagram_optimal1(strings[0], strings[1])
    result2 = sol.valid_anagram_optimal2(strings[0], strings[1])
    print(f"result: {result}\nresult1: {result1}\nresult2: {result2}")
