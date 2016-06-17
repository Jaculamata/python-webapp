h=input('input your height :')
w=input('input your weight :')
h=float(h)
w=float(w)
bmi = w/(h*h)
if bmi<18.5:
    print('过轻')
elif bmi<25:
    print('正常')
elif bmi<28:
    print('过重')
elif bmi<32:
    print('肥胖')
else:
    print('严重肥胖')
