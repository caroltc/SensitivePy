#encoding=utf-8
#DFA based text filter
#version=0.3
class GFW(object):
    def __init__(self):
        self.d = {}
    
    #give a list of "ming gan ci"
    def set(self,keywords):
        p = self.d
        q = {}
        k = ''
        for word in keywords:
            word += chr(11)
            p = self.d
            for char in word:
                char = char.lower()
                if p=='':
                    q[k] = {}
                    p = q[k]
                if not (char in p):
                    p[char] = ''
                    q = p
                    k = char
                p = p[char]
        
        pass
    
    def replace(self,text,mask):
        """
        >>> gfw = GFW()
        >>> gfw.set(["sexy","girl","love","shit"])
        >>> s = gfw.replace("Shit!,Cherry is a sexy girl. She loves python.","*")
        >>> print s
        *!,Cherry is a * *. She *s python.
        """
        p = self.d
        i = 0 
        j = 0
        z = 0
        result = []
        ln = len(text)
        while i+j<ln:
            #print i,j
            t = text[i+j].lower()
            #print hex(ord(t))
            if not (t in p):
                j = 0
                i += 1
                p = self.d
                continue
            p = p[t]
            j+=1
            if chr(11) in p:
                p = self.d
                result.append(text[z:i])
                result.append(mask)
                i = i+j
                z = i
                j = 0
        result.append(text[z:i+j])
        return "".join(result)
        
    def check(self,text):
        """
        >>> gfw = GFW()
        >>> gfw.set(["abd","defz","bcz"])
        >>> print gfw.check("xabdabczabdxaadefz")
        [(1, 3, 'abd'), (5, 3, 'bcz'), (8, 3, 'abd'), (14, 4, 'defz')]
        """
        p = self.d
        i = 0 
        j = 0
        result = []
        ln = len(text)
        while i+j<ln:
            t = text[i+j].lower()
            #print i,j,hex(ord(t))
            if not (t in p):
                j = 0
                i += 1
                p = self.d
                continue
            p = p[t]
            j+=1
            #print p,i,j
            if chr(11) in p:
                p = self.d
                result.append((i,j,text[i:i+j]))
                i = i+j
                j = 0
        return result
        
if __name__=="__main__":
    import doctest,sys
    doctest.testmod(sys.modules[__name__])
    

    