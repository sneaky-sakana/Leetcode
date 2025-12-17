import ast

class Solution:
    def group_anagram_brute(self, strs: List[str]):
        anagram_groups = []

        for string in strs:
            for group in anagram_groups:
                if len(string) == len(group[0]) and sorted(string) == sorted(group[0]):
                    group.append(string)
                    break
            else:
                anagram_groups.append([string])
        return anagram_groups

    def group_anagram_optimal1(self, strs: List[str]):
        anagram_hash = {}
        for string in strs:
            sorted_str_key = ''.join(sorted(string))
            if sorted_str_key in anagram_hash:
                anagram_hash[sorted_str_key].append(string)
            else:
                anagram_hash[sorted_str_key] = [string]
        return list(anagram_hash.values())

    def group_anagram_optimal2(self, strs: List[str]):
        count_hash = {}
        for string in strs:
            count_arr = [0] * 26
            for char in string:
                count_arr[ord(char) - ord('a')] += 1
            count_tuple = tuple(count_arr)
            if count_tuple in count_hash:
                count_hash[count_tuple].append(string)
            else:
                count_hash[count_tuple] = [string]
        return list(count_hash.values())

if __name__=="__main__":
    problem_input = input()
    strings = ast.literal_eval(problem_input)
    sol = Solution()
    result = sol.group_anagram_brute(strings)
    result1 = sol.group_anagram_optimal1(strings)
    result2 = sol.group_anagram_optimal2(strings)
    print(f"result: {result}\nresult1: {result1}\nresult2: {result2}")
