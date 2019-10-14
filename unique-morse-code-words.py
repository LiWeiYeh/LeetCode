# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: 
# "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

# For convenience, the full table for the 26 letters of the English alphabet is given below:
# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, 
# "cba" can be written as "-.-..--...", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.

# Return the number of different transformations among all words we have.

# Example:
#   Input: words = ["gin", "zen", "gig", "msg"]
#   Output: 2

# Explanation: 
# The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."

# There are 2 different transformations, "--...-." and "--...--.".

class Solution:
    def uniqueMorseRepresentations(self, words) -> int:
        
        MorseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        MorseCodedWordsUnique = []

        for word in words:
            concatWord = ""
            for letter in word:
                index = alphabet.index(letter)
                concatWord += MorseCode[index]
            # print(concatWord)
            if concatWord not in MorseCodedWordsUnique:
                MorseCodedWordsUnique.append(concatWord)
        
        return len(MorseCodedWordsUnique)


words = ["gin", "zen", "gig", "msg"]

test = Solution()

print("input: {}".format(words))
print("output: {}".format(test.uniqueMorseRepresentations(words)))
