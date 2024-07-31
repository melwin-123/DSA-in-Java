#First Method
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace("_","")
        pattern = re.compile('\W')
        string = re.sub(pattern, '', s.lower())
        string1 = string[::-1]
        if string == string1:
            return True
        return False

#More efficient second method
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=s.lower()
        print(string)
        for i in string:
            if i.isalnum()==False:
                string=string.replace(i,"")
        return string==string[::-1]
