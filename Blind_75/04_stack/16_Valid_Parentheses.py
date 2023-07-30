class Solution:
    def isValid(self, s: str) -> bool:
        mydict = { '(': ')', '[': ']', '{': '}' }
        mystack = []
        for char in s:
            if char in mydict.keys():
                mystack.append(char)
            else:
                if len(mystack.pop())==0:
                    return False
                last_element = mystack.pop()
                if mydict[last_element] != char:
                    return False
        return True if len(mystack)==0 else False


print(Solution().isValid(s="()"))
print(Solution().isValid(s="(){}[]"))
print(Solution().isValid(s="(]"))
