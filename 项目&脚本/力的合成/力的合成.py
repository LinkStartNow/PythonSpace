from math import *
from numpy import *

print('所有角度均为弧度制且省略π未显示')

def yyds(a, b):
    x = y = 0
    l = len(b)
    for i in range(l):
        x += a[i] * cos(b[i])
        y += a[i] * sin(b[i])
    if x < 1e-7:
        x = 0
    if y < 1e-7:
        y = 0
    e = (x ** 2 + y ** 2) ** (0.5)
    if x == 0:
        s = 0.5 if y > 0 else -0.5
    else:
        s = arctan(y / x) / pi
    if e < 1e-7:
        e = 0
        s = 0
    print('合力大小为:{}'.format(e))
    print('合力的夹角为(单位为π)：{}'.format(s))

while 1:
    a = list(map(float, input('请输入力的大小(用空格隔开):').split()))
    b = list(map(int, (input('请分别输入边与x轴的夹角(单位为π)(以分数输入，第一个为分子):')).split()))
    b = [0 if b[i] == 0 else b[i] / b[i + 1] * pi for i in range(0, len(b), 2)]
    yyds(a, b)
    k = input('是否继续(0退出,其他任意字符表示继续):')
    if(k == '0'):
        print('退出成功！')
        break
