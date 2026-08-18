class Solution(object):
    def longestCommonPrefix(self, strs):
        result = ""
        base = strs[0]
        for i in range(len(base)):
            for word in strs:
                if i == len(word) or word[i] != base[i]:
                    return(result)
                    exit()
            result += base[i]
        return(result)
        
strs=["flower","flow","flight"]
obj = Solution()
result = obj.longestCommonPrefix(strs)
print(result)