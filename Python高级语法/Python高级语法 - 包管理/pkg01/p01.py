class Student():
    def __init__(self, name = "NoName", age =18 ):
        self.name = name
        self.age =age

    def say(self):
        print("My name is {0}".format(self.name))

def SayHello():
    print("Hi,欢迎使用")

# 当
if __name__ ==  '__main__':
    print("正在调用模块p01")