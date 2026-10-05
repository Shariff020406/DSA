class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        # Helper function to convert "HH:MM:SS" into total seconds
        def to_seconds(time_str):
            h, m, s = map(int, time_str.split(':'))
            return h * 3600 + m * 60 + s
        
        start_seconds = to_seconds(startTime)
        end_seconds = to_seconds(endTime)
        
        return end_seconds - start_seconds