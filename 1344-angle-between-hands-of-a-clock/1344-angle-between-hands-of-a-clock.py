class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        hour_angle = hour * 30
        minute_angle = minutes * 6
        hour_angle += minutes / 60.0 * 30
        angle = abs(hour_angle - minute_angle)
        return angle if angle < 180 and angle > 0 else 360 - angle