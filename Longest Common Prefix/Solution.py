class Solution:
    def longestCommonPrefix(self, strs):
        min_len = min(len(word) for word in strs)
        prefix = ""
        flag = False
        for i in range(min_len):
            sample = strs[0][i]
            for word in strs[1:]:
                if word[i] != sample:
                    flag = True
                    break
            if flag == True:
                break
                
            prefix += sample
        return prefix
        




strs = ["flower","flow","flight"]
a =  Solution().longestCommonPrefix(strs)
print(a)
    
