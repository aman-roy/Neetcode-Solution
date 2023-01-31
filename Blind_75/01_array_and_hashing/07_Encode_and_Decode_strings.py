class Solution:
    def encode(self, strs):
        final = ""
        for s in strs:
            final += str(len(s)) + '@' + s
        print(final)
        return final

    def decode(self, str):
        final = list()
        while True:
            try:
                i = str.index('@')
            except:
                break
            str_len = int(str[:i])
            final.append(str[i+1:i+1+str_len])
            str = str[i+1+str_len:]
            
        return final


assert Solution().decode(Solution().encode(["lint", "code", "love", "you"])) ==  ["lint", "code", "love", "you"]
assert Solution().decode(Solution().encode(["we", "say", ":", "yes"])) ==  ["we", "say", ":", "yes"]
