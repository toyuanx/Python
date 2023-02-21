# 列表生成式

print([x * x for x in range(1, 9)])

L1 = ["Hello", "World", 18, "Apple", None]
L2 = [x for x in L1 if isinstance(x, str)]

print(L2)

# 列表生成器
