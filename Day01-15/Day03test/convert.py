

value = float(input('长度:'))
unit = input('单位')

if unit == 'in' or unit == '英尺':
    print('%f英尺=%f厘米' % (value,value*2.54))
elif unit == 'cm' or unit == '厘米':
    print('%f厘米=%f英尺' % (value,value/2.54))
else:print('单位不正确')