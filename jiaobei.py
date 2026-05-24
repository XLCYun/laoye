
import random

# 生成两个0/1随机数
a = random.randint(0, 1)
b = random.randint(0, 1)

# 格式化输出组合
print(f"({a}, {b})")

# 判断杯型
if a != b:
    print("圣杯")
elif a == 1 and b == 1:
    print("笑杯")
else:
    print("阴杯")
