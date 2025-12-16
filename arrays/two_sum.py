

class Solution():
	def two_sum_brute(self, nums, target):
		for i in range(len(nums)):
			for j in range(i+1, len(nums)):
				if nums[i] + nums[j] == target:
					return i, j

	def two_sum_optimal(self, nums, target):
		diff_hash = {}

		for i in range(len(nums)):
			if nums[i] in diff_hash:
				return i, diff_hash[nums[i]]
			else:
				diff_hash[target - nums[i]] = i

if __name__ == "__main__":
	input_array = input()
	target = int(input())
	array = list(map(int, input_array.split(',')))

	sol = Solution()
	result = sol.two_sum_brute(array, target)
	result1 = sol.two_sum_optimal(array, target)
	print(f"result: {result}\nresult1: {result1}")
