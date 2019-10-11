# Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

# To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].


# Example 1:
#     Input: [[1,1,0],[1,0,1],[0,0,0]]
#     Output: [[1,0,0],[0,1,0],[1,1,1]]
#     Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
#     Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

# Example 2:
#     Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
#     Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
#     Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
#     Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]


class Solution:
    def flipAndInvertImage(self, A):
        arr1 = []
        
        for element in A:
            index = len(element) - 1
            arr2 = []
            for number in element:
                if element[index] == 0:
                    arr2.append(1)
                else:
                    arr2.append(0)
                index -= 1
            arr1.append(arr2)

        return arr1

test = Solution()

testArr1 = [[1,1,0],[1,0,1],[0,0,0]]
testArr2 = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]

print("input: %s" % testArr1)
print("output: %s" % test.flipAndInvertImage(testArr1))
print("input: %s" % testArr2)
print("output: %s" % test.flipAndInvertImage(testArr2))
