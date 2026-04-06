fruitList=['apple','banana','lemen','apricot','coconut']
otherList=[100,'one','two',3]
print('fruitList:')
print(fruitList)
print('--------------------')
print('otherList:')
print(otherList)
print('--------------------')
for fruit in  fruitList:
    print('Hoa qua:',fruit)
print('--------------------')
for i in range(0,len(fruitList)):
    print('Phan tu thu hai cho den het',fruitList[i])
print('--------------------')
subList = fruitList[1:4]
print('Danh sach con tu 1 den 4',subList)
print('--------------------')
fruitList[4] = 'jackfruit'
print('Danh sach qua da thay',fruitList)
print('--------------------')
fruitList[2:] = []
print('Danh sach qua da thay 1',fruitList)
print('--------------------')
fruitList.append('mango')
print('Danh sach qua da thay 2',fruitList)
print('--------------------')
fruitList.insert(0,'carot')
print('Danh sach qua da thay 3',fruitList)
print('--------------------')
del fruitList[0]
print('--------------------')



diem=['A','B','C','D','E','F','A','B','C','D','E','F']
print('Bang diem lop hehe',diem)
count1=0
count2=0
count3=0
for i in range(0,len(diem)):
    count2=count2+1
print('So sinh vien trong lop',count2)
for i in range(0,len(diem)):
    if diem[i] == 'F':
        count1=count1+1
    else:
        count3=count3+1
print('So hoc sinh hoc lai mon nay la',count1)
print('So hoc sinh co tu diem B tro len',count3)
del diem[0]
del diem[-1]
print('Bang diem da thay doi la',diem)
print('--------------------')



cc=[1.65,1.7,1.8,1.9,1.67,1.56,1.85]
tongsv=0
ff=0
for l in range(0,len(cc)):
    tongsv=tongsv+1
print('Tong so sinh vien la',tongsv)
print("chieu cao lon nhat la",max(cc),'m')
print('chieu cao thap nhat la',min(cc),'m')
tbcc=sum(cc)/len(cc)
print('Chieu cao trung binh',tbcc,'m')
for cctb in range(0,len(cc)):
    if cctb >= tbcc:
        ff=ff+1
print('So sinh vien trong lop co cc >= trung binh la',ff)
print('-------------------')
dict = dict()
dict[1]='One'
dict[2]='Two'
dict[3]='Three'
print(dict)
