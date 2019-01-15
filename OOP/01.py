'''
定义一个学生类，用来形容学生
'''
# 定义一个空的类
class Student():
    # 一个空类，pass代表直接跳过
    # 此处pass必须有
    pass

#定义一个对象
student1 = Student()

# 再定义一个类，用来描述听Python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = "Python"

    # 需要注意：
    # 1.def一个函数的缩进层级和变量的层级是相同的
    # 2.系统默认有一个self参数
    def doHomeWork(self):
        print("I do my homewoek.")

        # 推荐在函数末尾使用return语句
        return None

# 实例化一个叫A的学生，是一个具体的人
A = PythonStudent()
print(A.name)
print(A.age)
# 注意成员函数的调用没有传递进入参数
A.doHomeWork()