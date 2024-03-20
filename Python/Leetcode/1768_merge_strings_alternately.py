class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minimum = min(len(word1),len(word2))
        car = []
        for i in range(minimum):
            car.append(word1[i])
            car.append(word2[i])

        if len(word1)>len(word2):
            car.append(word1[len(word2):])
        elif len(word2)>len(word1):
            car.append(word2[len(word1):])

        return ''.join(car)

# test
x = 'abc'
y = 'qrty'
solution = Solution()
result = solution.mergeAlternately(x,y)
print(result)