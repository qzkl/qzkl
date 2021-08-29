class Test:
    
    
    def __init__(self,a):
        self.a=a
        self.n=0
        self.x=[]
    def tf(self):
        self.a=self.a-1
        return self.a
    
    def total(self):
        
        if self.a<1:
            self.x.append(self.a)
            
            return self.n,self.x
        else:
            self.n+=self.a
            self.x.append(self.a)
            
            self.tf()
            return self.total()

b=Test(10)
c=Test(20)

print(b.total()[1])
print(c.total()[0])


