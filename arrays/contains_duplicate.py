from collections import Counter

class Solution:
    def containsDuplicateBrute(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

    def containsDuplicateOptimal1(self, nums: List[int]) -> bool:
        hash_counter = Counter(nums)
        for num in hash_counter:
            if hash_counter[num] > 1:
                return True
        return False

    def containsDuplicateOptimal2(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

if __name__=="__main__":
    problem_input = input()
    numbers = list(map(int, problem_input.split(',')))
    sol = Solution()
    result = sol.containsDuplicateBrute(numbers)
    result1 = sol.containsDuplicateOptimal1(numbers)
    result2 = sol.containsDuplicateOptimal2(numbers)
    print(f"result: {result}\nresult1: {result1}\nresult2: {result2}")
