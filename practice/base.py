# 列表生成式

print([x * x for x in range(1, 9)])

L1 = ["Hello", "World", 18, "Apple", None]
L2 = [x for x in L1 if isinstance(x, str)]

print(L2)

# 列表生成器


# 过滤器求素数
def _odd_filter():
    n = 1
    while True:
        n = n + 2
        yield n


n = 1
while n <= 10:
    print(next(_odd_filter()))
    n = n + 1
