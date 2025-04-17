class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        arrows = 1
        current_arrow = points[0][1]
        for balloon in points[1:]:
            if balloon[0] > current_arrow:
                arrows += 1
                current_arrow = balloon[1]
            else:
                current_arrow = min(balloon[1], current_arrow)
        return arrows
            