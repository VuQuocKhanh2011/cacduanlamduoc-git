n = int(input('Nhap vao so n:'))
for i in range (1,n):
     print(f'binh phuong la',i*2) #bai1

if n>10:
    print('so nhap vao be hon 10')
else:
    for n in range (2,11,2):
        print(n) #bai2

for h in range (80,101):
    if h%2==0 and h%3==0:
        print(h) #bai3

k=int(input('nhap vao so k:'))
for k in range(k,20):
    if k%5==0 or k%7==0:
     print(k)#bai4