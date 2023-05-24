print('Задача 2')
a = input("Введите трехзначное число\n")
kolvo=0
while len(a) !=3:
    if  a.isdigit() ==True:
        a = input("Вы ввели не трехзначное число, попробуйте еще раз\n")
    else:
        a = input("Вы ввели не число, на этот раз введите трехзначное число\n")
for i in a:
    kolvo+=int(i)
print(kolvo)
print('*'*100)
print('Задача 4')
x=int(input())
print(x//6,4*x//6,x//6)
print('Задача 6')
def F(n):
    a=0
    for i in n:
        a+=int(i)
    return a
s = input('Введите номер вашего билета\n')
while len(s)!=6 or s.isdigit()==False:
    s=input('Вы ввели не верный номер, попробуйте еще раз\n')

if F(s[0:3])==F(s[3:6]):
    print('yes')
else:
    print('no')

print('Задача 8')
n = int(input())
m = int(input())
k = int(input())
if k < n*m and (k % n == 0 or k % m == 0):
    print('YES')
else:
    print('NO')
