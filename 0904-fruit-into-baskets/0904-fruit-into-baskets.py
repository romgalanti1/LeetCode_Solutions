class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        left = 0
        fruit_count = {}
        max_count = 0
        for right in range(len(fruits)):
            currfruit = fruits[right]
            fruit_count[currfruit] = fruit_count.get(currfruit , 0) + 1
            while len(fruit_count) > 2:
                leftfruit = fruits[left]
                fruit_count[leftfruit] -= 1
                if fruit_count[leftfruit] == 0:
                    del fruit_count[leftfruit]
                left += 1
            max_count = max(max_count, right - left + 1)
        return max_count