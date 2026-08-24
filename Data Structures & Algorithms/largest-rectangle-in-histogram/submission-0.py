class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = heights[0]
        for i, h in enumerate(heights):
            ind = i
            while stack and h < stack[-1][0]:
                stackHeight, stackInd = stack.pop()
                area = max(area, stackHeight*(i - stackInd))
                ind = stackInd
            stack.append((h, ind))
        while stack:
            stackHeight, stackInd = stack.pop()
            area = max(area, stackHeight*(len(heights) - stackInd))
        return area
