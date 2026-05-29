class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        
        a1=[0]*26
        a2=[0]*26
        mc=0

        for i in range(len(s1)):
            a1[ord(s1[i])-ord('a')]+=1
            a2[ord(s2[i])-ord('a')]+=1

        #for lenght s1, now we loop through these arrays to find matching characters

        for y in range(26):
            if a1[y]==a2[y]:
                mc+=1
            
        a=0
        b=len(s1)

        while b<len(s2):
            if mc==26:
                return True
           

            a2[ord(s2[a])-ord('a')]-=1

            
            if a1[ord(s2[a])-ord('a')] == a2[ord(s2[a])-ord('a')]+1:
                mc-=1
            elif a1[ord(s2[a])-ord('a')] == a2[ord(s2[a])-ord('a')]:
                mc+=1
            
            a2[ord(s2[b])-ord('a')]+=1

            if a1[ord(s2[b])-ord('a')] + 1 == a2[ord(s2[b])-ord('a')]:
                mc-=1
            elif a1[ord(s2[b])-ord('a')] == a2[ord(s2[b])-ord('a')]:
                mc+=1

            a+=1
            b+=1
        return mc==26
                
