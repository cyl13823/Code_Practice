class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        car = []
        for i in range(len(candies)):
            candies[i] += extraCandies
            if candies[i] == max(candies):
                car.append(True)
                candies[i] -= extraCandies
            else:
                car.append(False)
                candies[i] -= extraCandies
            
        return car
    
# test
candies = [2,3,5,1,3]
extraCandies = 3
solution = Solution()
result = solution.kidsWithCandies(candies,extraCandies)
print(result)