# class A:
#     a=10
#     b=20
# print(A.a,A.b)
# ob=A
#
# print(A)


class A:
    def rk(self):
        print(" In class A")


class B(A):
    def rk(self):
        print(" In class B")


r = B()
r.rk()