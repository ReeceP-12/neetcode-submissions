class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_count = {}
        for i in s:
            if i not in s_count:
                s_count[i] = 1
            else: s_count[i] += 1
        for y in t:
            if y not in s_count or s_count[y] == 0:
                return False
            elif y in s_count:
                s_count[y] -= 1

        return True       

