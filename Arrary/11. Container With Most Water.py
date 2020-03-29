class Solution:
    def maxArea(self, height: List[int]) -> int:
        Area = 0
        l = 0
        r =  len(height) -1
        while l<r:
            area = (r-l) * min(height[l],height[r])
            Area = max(Area,area)
            if height[l]<height[r]:
                l +=1
            else:
                r -=1
        return Area