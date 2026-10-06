class Solution(object):
    def shipWithinDays(self, weights, days):
        m1=max(weights)
        m2=sum(weights)
        while(m1<=m2):
            s=0
            cnt=1
            mid=m1+(m2-m1)//2
            for i in weights:
                if(s+i>mid):
                    cnt+=1
                    s=i
                else:
                    s+=i
            if(cnt<=days):
                m2=mid-1
                res=mid
            else:
                m1=mid+1
        return res

                    

        