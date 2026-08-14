class Solution(object):
    def check_plm(self, word):
        left= 0
        right = len(word)-1
        while left<right:
            if word[left] != word[right]:
                return f"False"
            left +=1
            right -= 1
        return f"True"
word = "madam"
obj = Solution()
result = obj.check_plm(word)
print(result)