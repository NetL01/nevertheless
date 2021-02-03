class A:
    def __str__(self):
        return str(self.parent)

a = A()
a.parent = a
a = B
str(B)
