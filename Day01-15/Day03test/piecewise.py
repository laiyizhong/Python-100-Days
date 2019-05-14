"""
		3x - 5	(x > 1)
f(x) =	x + 2	(-1 <= x <= 1)
		5x + 3	(x < -1)
"""

x = float(input('输入x:'))

if x>1:
    y = 3*x
elif x < -1:
    y = 5*x +3
else:
    y=x+2
print(y)