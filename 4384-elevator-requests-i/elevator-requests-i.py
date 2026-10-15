class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        count=0
        current_flr=0
        for i in range(len(requests)):
            count+=abs(requests[i]-current_flr)
            current_flr=requests[i]
        return count
            
        