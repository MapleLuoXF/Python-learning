# 包含一个学生类，一个SayHello函数，一个打印语句
# 在使用模块时，相当于把模块内的代码全部粘贴到本文件的开头
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