class Solution:

    def encode(self, strs: List[str]) -> str:
      s=""
      for i in strs:
        s+=str(len(i)) + '#' + str(i)
      return s

    
    def decode (self, s ):
        li = []
        i=0
        while i < len(s)-1:
            num = ''
            while s[i]!= '#':
                num+=s[i]
                i+=1
            
            a=i+1
            b=a+int(num)
            li.append(s[a:b])

            i=b
        
        return li