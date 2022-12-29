#inheritance
class A:
    def __init__(self):
        print("A init executed")

class B(A):
    def __init__(self):
        super().__init__()
        print("B init executed")
        abc = B()
# MRO (Method Resolution Order)
class A:
    pass

class B(A):
    x = 5

class C(B):
    pass

class D(A):
    x = 10

class E(C, D):
    pass
e = E()
print(e.x)
E.mro()
# DFS
# Iteration Protocol
a = range(5)
# it = a.__iter__()
it = iter(a)
it
# it.__next__()
next(it)
a = 'jatin'
iter(a)
for i in range(5):
    print(i)
class myrange:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return myrange_iterator(self)

class myrange_iterator:
    def __init__(self, myrange):
        self.myrange = myrange
        self.i = 0

    def __next__(self):
        ret = self.i
        self.i += 1

        if ret >= self.myrange.n:
            raise StopIteration


        return ret
a = myrange(5)
# for (int i =0; i<10; i++)
it = iter(a)
next(it)