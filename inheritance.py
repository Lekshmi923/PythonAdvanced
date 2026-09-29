# class Parent:
#
#     def m1(self):
#         print("method in parent class m1")
#
#     def m2(self):
#         print("method in parent class m2")
#
# p=Parent()
# p.m1()
# p.m2()
#
# class Child(Parent):
#     pass
#
# c=Child()
# c.m1()
# c.m2()



# class Parent:
#
#     def m1(self):
#         print("method in parent class m1")
#
#     def m2(self):
#         print("method in parent class m2")
#
# p=Parent()
# p.m1()
# p.m2()
#
# class Child(Parent):
#
#     def m3(self):
#         print("Method in child class m3")
#
# c=Child()
# c.m1()
# c.m2()
# c.m3()



class Parent:

    def m1(self):
        print("method in parent class m1")

    def m2(self):
        print("method in parent class m2")

p=Parent()
p.m1()
p.m2()

class Child(Parent):

    def m1(self):
        super().m1()
        print("Method in child class m1")

    def m3(self):
        print("Method in child class m3")

c=Child()
c.m1()
c.m2()
c.m3()




