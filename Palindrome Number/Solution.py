class Solution:
    def isPalindrome(self, x):
        x_str = str(x)
        flag = True  
        for i in range(len(x_str)//2):
            if x_str[i] != x_str[-(i+1)]:
                flag = False
                break
        return flag
x = 1 
print(Solution().isPalindrome(x))
