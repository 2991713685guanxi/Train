"""
a= 3.14
b = []
print(a)

print(f"我今年{a}hhhe")
c = int(a)
print(type(c))
age = 18
bbb = "很牛" if age >= 18 else "很拉"
print(bbb)
"""
b = []
while True:
    a = [0]
    for i in range(1,10):
        a.append(i)
    b.append(a)
    print(b)
    if len(b) == 10:
        break

nums = [1,3,5,6,97,7]
names = ["ha","sdada"]
numsss = nums + names
print(numsss)