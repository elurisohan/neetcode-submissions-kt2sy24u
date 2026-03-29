class Solution:

    def encode(self, strs: List[str]) -> str:
        s=''
        for i in strs:
            s+=str(len(i))+'#'+str(i)
        return s

    def decode(self, s: str) -> List[str]:
        ans=[]
        i=0
        while i<len(s):
            num=''
            while s[i]!='#':
                num+=s[i]
                i+=1

            ans.append(s[i+1:i+1+int(num)])
            i=i+1+int(num)

        return ans