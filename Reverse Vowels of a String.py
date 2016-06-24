
def reverseVowels(s):
    ls = list(s)
    i ,j = 0 ,len(ls)-1
    vowel = ['a','A','e','i','o','u','E','I','O','U']
    while i<j:
        while i<j and  ls[i] not in vowel:
            i+=1
        while i<j and ls[j] not in vowel:
            j-=1
        if i<j:
            ls[i] , ls[j] = ls[j] , ls[i]
            i+=1
            j-=1
    return ''.join(ls)

print reverseVowels('Hello')

