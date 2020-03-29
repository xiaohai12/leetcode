class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0
        '''
        l = 0
        area = 0
        reduce = 0
        Max = max(height)
        for i in range(0,len(height)):
            if i>0 and height[i]>=height[l]:
                area += height[l] * (i-l-1) - reduce 
                l = i 
                reduce =0
            elif i>0:
                reduce += height[i]

            if height[i]==Max:
                break
        ## reverse 
        reduce = 0
        l = len(height) -1 
        for j in range(len(height)-2,i-1,-1):
            if height[j] >= height[l]:
                area += height[l] * (l-j-1) -reduce
                l = j 
                reduce = 0
            else:
                reduce += height[j]
        return area 

        '''
        leftmost = 0
        rightmost = 0
        left = 0
        right = len(height) - 1
        area = 0
        while left < right:
            if height[left] <= height[right]:
                ## means right side is high enough to hold water from left
                if height[left] > leftmost:
                    leftmost = height[left]
                else:
                    area += leftmost - height[left]
                left += 1
            else:
                if height[right] > rightmost:
                    rightmost = height[right]
                else:
                    area += rightmost - height[right]
                right -= 1
        return area



