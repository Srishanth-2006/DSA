class Solution(object):
    def findKthPositive(self, arr, k):
        m1=arr[0]
        m2=arr[-1]
        while True:
            mid=m1+abs((m2+m1)//2)
            l1=[i for i in range(1,mid+1) if i not in arr]
            if(len(l1)>=k):
                return l1[k-1]
            else:
                m1=mid+1

        