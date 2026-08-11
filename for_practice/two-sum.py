'''
Question:
Given a sorted array and a target, find two numbers whose sum equals the target. 
arr = [1, 2, 3, 4, 6, 8]
target = 10
'''
class Solution:
    def two_some(self, arr):
        target = 10
        left=0
        right=len(arr)-1
        while left<right:
            total = arr[left]+arr[right]
            if total==target:
                return f"{arr[left]},{arr[right]}"
            elif total<target:
                left += 1
            else:
                right -= 1
arr = [1, 2, 3, 4, 6, 8]
obj = Solution()
print(obj.two_some(arr))

        