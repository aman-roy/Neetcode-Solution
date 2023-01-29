class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(x for x in s.lower() if x.isalnum())
        return s == s[::-1]

assert Solution().isPalindrome("A man, a plan, a canal: Panama") == True
assert Solution().isPalindrome(" ") == True
assert Solution().isPalindrome("race a car") == False


from typing import Optional

class Solution1:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            temp_l = self.changeCaseOrReturnNone(s[l])
            if not temp_l: 
                l+=1
                continue
            temp_r = self.changeCaseOrReturnNone(s[r])
            if not temp_r:
                r-=1
                continue
            if temp_l != temp_r:
                return False
            l+=1
            r-=1
        return True


    def changeCaseOrReturnNone(self, s:str) -> Optional[str]:
        assert len(s) == 1

        if ord(s) >= ord('a') and ord(s) <= ord('z'):
            return s
        elif ord(s) >= ord('A') and ord(s) <= ord('Z'):
            diff = ord('a') - ord('A')
            return chr(ord(s)+diff)
        else:
            return None
        

assert Solution1().isPalindrome("A man, a plan, a canal: Panama") == True
assert Solution1().isPalindrome(" ") == True
assert Solution1().isPalindrome("race a car") == False


