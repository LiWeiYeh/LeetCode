# Given a valid (IPv4) IP address, return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".

# Example 1:
#     Input: address = "1.1.1.1"
#     Output: "1[.]1[.]1[.]1"

# Example 2:
#     Input: address = "255.100.50.0"
#     Output: "255[.]100[.]50[.]0"

class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        defangedAddress = ""

        for char in address:
            if char == ".":
                defangedAddress += "[.]"
            else:
                defangedAddress += char
                
        return defangedAddress

address = "1.1.1.1"
address2 = "255.100.50.0"

test = Solution()
print("input: %s\noutput: %s\n" % (address, test.defangIPaddr(address)))

print("input: %s\noutput: %s" % (address2, test.defangIPaddr(address2)))
