class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product=1
        sum=0
        while(n>0):
            ans=n%10
            product*=ans
            sum+=ans
            n//=10
            final=product-sum
        return final
            