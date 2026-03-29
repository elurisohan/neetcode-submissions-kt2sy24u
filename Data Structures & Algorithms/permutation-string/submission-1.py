class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        m1=[0]*26
        m2=[0]*26
        matches=0
        l=0
        for i in range(len(s1)):
            m1[ord(s1[i])-ord('a')]+=1
            m2[ord(s2[i])-ord('a')]+=1

        for x in range(26):
            if m1[x]==m2[x]:
                matches+=1

        for r in range(len(s1),len(s2)):
            if matches==26:
                return True

            index=ord(s2[r])-ord('a')
            m2[index]+=1

            if m1[index]==m2[index]:
                matches+=1
            elif m1[index]+1==m2[index]:
                matches-=1

            inde=ord(s2[l])-ord('a')
            m2[inde]-=1

            if m1[inde]==m2[inde]:
                matches+=1
            elif m1[inde]-1==m2[inde]:
                matches-=1
            
            l+=1
        
        return matches==26


        