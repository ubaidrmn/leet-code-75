class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        most_candies = max(candies)
        greatest_candies = []
        for i in range(len(candies)):
            num_of_candies = candies[i]
            if num_of_candies + extraCandies >= most_candies:
                greatest_candies.append(True)
            else:
                greatest_candies.append(False)
        return greatest_candies
