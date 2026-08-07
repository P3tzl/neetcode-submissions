class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        max = 0
        for num in nums:
            if num:
                current += 1
            else:
                if current > max:
                    max = current
                    current = 0
                current = 0
        if current > max:
            return current
        else:
            return max 