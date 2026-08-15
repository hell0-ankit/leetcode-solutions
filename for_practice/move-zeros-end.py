# Move Zeros to End
# Input:  [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]
class Solution(object):
    def move_zeros_end(self, arr_num):
        left = 0
        right = 0
        while right < len(arr_num):
            if arr_num[right]!=0:
                arr_num[left],arr_num[right] = arr_num[right],arr_num[left]
                left += 1
            right += 1
        return arr_num
        
arr_num =  [0, 1, 0, 3, 12]
obj = Solution()
result = obj.move_zeros_end(arr_num)
print(result)
