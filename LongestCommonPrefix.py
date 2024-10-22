
class Solution:
    def CommonPrefix(self, strs: list) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
        return prefix


a = Solution()
strs = ["flower", "giow", "flight"]
print(a.CommonPrefix(strs)) 






