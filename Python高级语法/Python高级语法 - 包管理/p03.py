import sys

print(type(sys.path))
# 结果显示，sys.path的类型是list
print(sys.path)

for i in sys.path:
    print(i)