'''class Foo(object):
    def __init__(self, frob, frotz):
        self.frobnicate = frob
        self.frotz = frotz


class Bar(Foo):
    def __init__(self, frob, frizzle):
        super(Bar, self).__init__(frob, frizzle)
        self.frotz = 34
        self.frazzle = frizzle


bar = Bar(1, 2)
print("frobnicate:", bar.frobnicate)
print("frotz:", bar.frotz)
print("frazzle:", bar.frazzle)
class Base(object):
    def __init__(self):
        print("Base created")

class ChildA(Base):
    def __init__(self):
        Base.__init__(self)

class ChildB(Base):
    def __init__(self):
        super(ChildB, self).__init__()

ChildA()
ChildB()
'''

class name():
    def __init__(self):
        print("my name is aasai")

class myname(name):
    def __init__(self):
        name.__init__(self)

class myname1(name):
    def __init__(self):
        super(myname1,self).__init__()

class myname2(name):
    def __init__(self):
        super().__init__()
myname()
myname1()
myname2()