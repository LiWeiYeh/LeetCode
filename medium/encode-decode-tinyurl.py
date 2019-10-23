# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl 
# and it returns a short URL such as http://tinyurl.com/4e9iAk.

# Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. 
# You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

# TODO

def DecimalToHex(n):
    # if (n == 0):
    #     return "0"
    # else:
    #     digit = n % 16
    #     return (DecimalToHex((n - digit) / 16) + str(digit))

    hexNumber = ""
    base = 16
    while (n > 0):
        remainder = n % base
        n = ((n - remainder)/base)
        hexNumber = str(int(remainder)) + hexNumber

    return hexNumber

class Codec:

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """

        tinyUrl = "http://tinyurl.com/"

        for symbol in longUrl:
            print("symbol: {}, ascii number: {}", symbol, ord(symbol))
            asciiValue = str(ord(symbol))
            if len(asciiValue) < 3:
                length = len(asciiValue)

                tinyUrl += ( (3-(len(asciiValue))) * "0" + asciiValue)
            else:
                tinyUrl += asciiValue

        print(tinyUrl)
        return tinyUrl

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        longUrl = ""

        shortUrlRemoved = shortUrl.replace("http://tinyurl.com/", "")
        print(shortUrlRemoved)
        n = 3
        listAsciiValues = [shortUrlRemoved[i:i+n] for i in range(0, len(shortUrlRemoved), n)]        
        print(listAsciiValues)
        for element in listAsciiValues:
            longUrl += chr(int(element))
        print(longUrl)
        return longUrl

# Your Codec object will be instantiated and called as such:
codec = Codec()
# codec.decode(codec.encode(url))
url = "https://leetcode.com/problems/design-tinyurl"
# print(codec.encode(url))
# print(codec.decode(codec.encode(url)))
codec.decode(codec.encode(url))