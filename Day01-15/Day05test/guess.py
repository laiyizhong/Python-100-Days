
import random
answer = random.randint(1,100)
count = 0
print(answer)
while True:
    count += 1
    number = int(input('输入数字:'))
    if number > answer:
        print('高了')
    elif number < answer:
        print('低了')
    else:
        print('答对')
        break
print('总共%d次答对' % count)