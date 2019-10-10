class Solution:
    def uniqueOccurrences(self, arr: list) -> bool:
        
        uniqueArray = []
        uniqueArrayOccurences = []
        uniqueArrayOccurencesTemp = []
        
        for element in arr:
            if element not in uniqueArray:
                uniqueArray.append(element)
                uniqueArrayOccurences.append(1)
            else:
                index = uniqueArray.index(element)
                uniqueArrayOccurences[index] += 1

        for element in uniqueArrayOccurences:
            if element in uniqueArrayOccurencesTemp:
                return False
            else:
                uniqueArrayOccurencesTemp.append(element)
        
        return True


arr = [1, 2, 2, 1, 1, 3]

Test = Solution()
print(Test.uniqueOccurrences(arr))