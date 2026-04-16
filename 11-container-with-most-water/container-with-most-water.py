class Solution:
    def maxArea(self, height: List[int]) -> int:
        # left, right = 0, len(height) -1
        # max_area = 0

        # while left < right:
        #     width = right - left
        #     current_area = min (height[left], height[right])*width
        #     max_area = max(max_area, current_area)

        #     if height[left] < height[right]:
        #         left += 1
        #     else:
        #         right -= 1

        # return max_area





        
        left = 0
        right = len(height) - 1

        area = left*right
        max_area = 0

        while left < right:
            width = right - left
            current_area = width*min(height[left], height[right])
            max_area = max(current_area, max_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

        # max_area = 0
        # left = 0
        # right = len(height) - 1
        # while left < right:
        #     width = right - left
        #     area = width*min(height[left], height[right])
        #     max_area = max(max_area, area)
        #     if height[left] < height[right]:
        #         left += 1
        #     else:
        #         right -= 1
        # return max_area