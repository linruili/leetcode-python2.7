def merge(nums1, m, nums2, n):
    m-=1
    n-=1
    for i in range(m+n+1 , -1 , -1):
        if m==-1 or (n>=0 and nums1[m] < nums2[n]):
            nums1[i] = nums2[n]
            n -= 1
        else:
            nums1[i] = nums1[m]
            m -= 1
    return nums1

a=[1,""]
b=1
print merge(a,b,[2],1)
print b