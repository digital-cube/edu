

class MyClass:

    def __init__(self, arg):
        self.arg = arg
        pass

    def my_method(self):
        print('my method with value ', self.arg)

    @classmethod
    def my_class_method(cls):
        print('my class method')


if __name__=="__main__":

    a = MyClass(5)
    a.my_method()

    b = MyClass(10)
    b.my_method()
    a.my_method()

    MyClass.my_class_method();
    MyClass.my_class_method();