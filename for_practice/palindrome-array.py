# Check Palindrome Array
# arr_nums:  [1, 2, 3, 2, 1]
# Output: True
class Solution(object):
    def check_plm(self, arr_nums):
        left= 0
        right = len(arr_nums)-1
        while left<right:
            if arr_nums[left] != arr_nums[right]:
                return False
            left +=1
            right -= 1
        return True
arr_nums = [1, 2, 3, 2, 1]
obj = Solution()
result = obj.check_plm(arr_nums)
print(result)