class Person:
    def __call__(self, name):
        print("__call__"+"Hello"+name)

    def hello(selfs,name):
        print("Hello"+name)

person = Person()
person("WY")  #不需要点之后方法的调用
person.hello("lisi")

