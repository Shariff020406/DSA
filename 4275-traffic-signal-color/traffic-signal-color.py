class Solution:
    def trafficSignal(self, timer: int) -> str:
        ans=[]
        if timer==0:
            ans.append("Green")
        elif timer==30:
            ans.append("Orange")
        elif timer>30 and timer<=90:
            ans.append("Red")
        else:
            ans.append("Invalid")
        return ans[0]
        