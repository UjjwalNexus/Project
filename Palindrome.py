class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <0:
            return False
        i=x
        d=0
        rev=0
        while i !=0:
            d= i%10
            rev = rev*10 + d
            i= i //10
        return rev==x


a= Solution()
print (a.isPalindrome(21))
            


        
