# Move Zeros to End
# Input:  [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]
class Solution(object):
    def move_zeros_end(self, arr_num):
        i = 0
        j = 0
        while j < len(arr_num):
            if arr_num[j]!=0:
                arr_num[i],arr_num[j] = arr_num[j],arr_num[i]
                i += 1
            j += 1
        return arr_num
        
arr_num =  [0, 1, 0, 3, 12]
obj = Solution()
result = obj.move_zeros_end(arr_num)
print(result)
