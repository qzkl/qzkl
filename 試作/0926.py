class A:

    def __init__(self, a):
        self.a = a
        print("A init")

    def __call__(self, b):
        print("A call")
        print(b + self.a)

class B(A):

    def __init__(self, a, c):
        super().__init__(a)
        self.c = c
        print("B init")

    def __call__(self, d):
        print("B call")
        print(self.a + self.c + d)

a=A(1)

a(2)
