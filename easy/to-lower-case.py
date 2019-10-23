# Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

# Example 1:
#   Input: "Hello"
#   Output: "hello"

# Example 2:
#   Input: "here"
#   Output: "here"

# Example 3:
#   Input: "LOVELY"
#   Output: "lovely"

class Solution:
    def toLowerCase(self, str: str) -> str:
        lowerCaseLetters = "abcdefghijklmnopqrstuvwxyz"
        upperCaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        lowerCasedString = ""
        for char in str:
            if char in upperCaseLetters:
                index = upperCaseLetters.index(char)
                lowerCasedString += lowerCaseLetters[index]
            else:
                lowerCasedString += char
        
        return lowerCasedString


string = "HelloWorldAbCdEfG"

test = Solution()
print(test.toLowerCase(string))
