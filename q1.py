maths_mark = int(input("please input maths mark:"))

chemistry = int(input('please input chemistry mark:'))

physics = int(input('please input physics mark:'))

final = maths_mark + chemistry + physics / 3

if final < 40:
    print('you failed')
elif final >= 40 and final < 50:
    print('D')   
elif final >= 50 and final < 60:
    print('C') 
elif final >= 60 and final < 70:
    print('B')
elif final >= 70:
    print('A')

