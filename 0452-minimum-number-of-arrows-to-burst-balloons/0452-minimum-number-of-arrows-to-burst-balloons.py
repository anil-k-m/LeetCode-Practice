class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        arrows = 1
        current_arrow = points[0][1]
        for i in range(1,len(points)):
            if points[i][0] > current_arrow:
                arrows += 1
                current_arrow = points[i][1]
        return arrows
            