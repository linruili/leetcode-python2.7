def compareVersion( version1, version2):
    v1Arr = version1.split('.')
    v2Arr = version2.split('.')
    len1 = len(v1Arr)
    len2 = len(v2Arr)
    lenMax = max(len1 , len2)
    for i in range(0,lenMax):
        v1 , v2 = 0 , 0
        if i<len1:
            v1 = int(v1Arr[i])
        if i<len2:
            v2 = int(v2Arr[i])
        if v1<v2:
            return -1
        if v1>v2:
            return 1
    return 0

print compareVersion("2" , "1.10")
