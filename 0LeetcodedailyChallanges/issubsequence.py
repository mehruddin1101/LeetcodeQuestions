class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        count = 0
        for i in range(len(t)):
            if (count < len(s) and s[count] == t[i]):
                count+=1
        return count== len(s)

