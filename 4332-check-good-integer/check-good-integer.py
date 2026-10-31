class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digitsum=0
        squaresum=1
        while(n>0):
            digit=n%10
            digitsum+=digit
            squaresum+=digit**2
            n//=10
        if squaresum-digitsum>=50:
            return True
        else:
            return False
        