#viet ten
def sayHello(name):
    return 'hello'+ name
text = sayHello(' Nguyen van A')
print(text)

#ham in
def printme(str):
    print(str)
    return
printme('Vu quoc khanh')
printme('Nguyen van A')

#tong hieu
def tonghieu(x,y):
    tong=x+y
    hieu=x-y
    return tong,hieu
x,y=tonghieu(10,2)
print('tong la',x)
print('hieu la',y)

#bien toan cuc
b=20
def msg():
    a=10
    print('gia tri cua a la',a)
    print('gia tri cua b la',b)
    return
msg()
print(b)

#tham so bat buoc
def sum(a,b):
    c=a+b
    print(c)
sum(5,10)

#tham so mac dinh
def msg(id,name,age=23):
    print('id:',id)
    print('ten:',name)
    print('tuoi:',age)
    return
msg(name='Hoang',id=100)

#tham so tu khoa
def msg(id,name):
    print('id:',id)
    print('ten:',name)
    return

msg(id='100',name='Hoang')
msg(name='Nguyen',id='101')

#tham so thay doi
def printinfo(*arg2):
    tong = 0
    for v in arg2:
        print(v)
        tong += v
    return tong
tong = printinfo(10, 80, 30, 10000)
print('Kết quả tổng là:', tong)

#baitaptongcacso
def sum(a,*b):
    tong=0
    for v in b:
        tong += v
    return tong
print(sum('Tong cac so',10,20,30))
print(sum('Tong hai so',10,20))
#kiemtrasonguyento
def kiemtrasonguyento(a):
    nguyento = 0
    if a <= 1:
        print('a khong phai so nguyen to')
    else:
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                nguyento = nguyento + 1
                break
    if nguyento == 0:
        print(f'{a} la so nguyen to')
    else:
        print(f'{a} khong la so nguyen to')
print(kiemtrasonguyento(10))
print(kiemtrasonguyento(20))
#kiemtrasonguyentotrongkhoang
def kiemtrasonguyentotrongkhoang(a,*b):
    nguyento = 0
    for k in range(a,*b):
     if k <= 1:
        print('k khong phai so nguyen to')
     else:
        for i in range(2, int(a ** 0.5) + 1):
            if k % i == 0:
                nguyento = nguyento + 1
                break
     if nguyento == 0:
        print(f'{k} la so nguyen to')
print(kiemtrasonguyentotrongkhoang(2,5))
#kiemtrasohoanhao
def kiemtrasohoanhao(a):
        tonguoc = 0
        if a < 1:
            print('a khong phai so hoan hao')
        else:
            for i in range(1, int(a ** 0.5) + 1):
                if a % i == 0:
                    tonguoc = tonguoc + i
                    break
        if tonguoc == a:
            print(f'{a} la so hoan hao')
print(kiemtrasohoanhao(10))
print(kiemtrasohoanhao(6))
#kiemtrasohoanhaotrongkhoang
def kiemtrasohoanhaotrongkhoang(a,b):
    tonguoc = 0
    for h in range(a,b):
     if h < 1:
        print('h khong phai so hoan hao ')
     else:
        for o in range(1, int(a ** 0.5) + 1):
            if a % o == 0:
                tonguoc = tonguoc + o
                break
     if tonguoc == h:
        print(f'{h} la so hoan hao')
print(kiemtrasohoanhaotrongkhoang(1,10))
#cuphapfile: file object=open()
import os
filepath='main.py'
open(filepath)
print('open file with default mode')
open(filepath,'r+')
print('open file with Read & Writte mode')

info = \
'Name: CNTT\n'+\
'Mail: it@gmail.com\n'+\
'Phone: 0378817663\n'+ \
'Address: Hanoi'
f=open('testWrite.txt','w')
f.write(info)

