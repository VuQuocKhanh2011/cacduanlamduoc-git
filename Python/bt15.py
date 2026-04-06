tich=1
for i in range(1,11):
    tich=tich*i
    print(tich)#bai1


n=int(input('Nhap n tu ban phim:'))
giaithua=1
for k in range(1,n+1):
     giaithua=giaithua*k
     print(giaithua)#bai2

tong=0
for h in range(2,n,2):
    tong=tong+h
    print(tong)#bai4

nt = int(input('nhap nt tu ban phim: '))
nguyento=0
if nt <= 1:
    print('nt khong phai so nguyen to')
else:
    for i in range(2, int(nt**0.5) + 1):
        if nt % i == 0:
            nguyento=nguyento+1
            break
if nguyento == 0:
    print(f'{nt} la so nguyen to')
else:
    print(f'{nt} khong la so nguyen to')#bai3