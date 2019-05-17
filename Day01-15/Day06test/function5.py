
def f1(a,b=5,c=6):
    return a + b*2 +c*3

print(f1(1,2,3))
print(f1(100,200))
print(f1(100))
print(f1(c=3,a=1,b=2))

def f2(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(f2(1, 2, 3))
print(f2(1, 2, 3, 4, 5))
print(f2())

def f3(**kw):
    if 'name' in kw:
        print('欢迎%s' % kw['name'])
    elif 'tel' in kw:
        print('你的联系电话是: %s!' % kw['tel'])
    else:
        print('没找到你的个人信息!')

param = {'name': '骆昊11111', 'age': 38}
print(f3(**param))
#f3(name='骆昊', age=38, tel='13866778899')
