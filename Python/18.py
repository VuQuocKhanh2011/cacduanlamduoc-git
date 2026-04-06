
ten = str(input("Nhap ten: "))
print(ten.title())
print('----------------------')


doanvan = 'Nước Việt Nam là một, dân tộc Việt Nam là một. Sông có thể cạn núi có thể mon, song chân lý ấy không bao giờ thay đổi. (HỒ CHÍ MINH, 1890-1969)'
tucantim ='hồ chí minh'
tucantim1 = 'non sông'
if tucantim.lower()in doanvan.lower():
    print(f'Co tim thay tu can tim {tucantim} ')
else:
    print(f'Khong co tu can tim {tucantim}')
if tucantim1.lower() in doanvan.lower():
    print(f'Co tim thay tu can tim {tucantim1}')
else:
    print(f'Khong co tu can tim {tucantim1}')
danhsachcau=doanvan.split(".")
print(danhsachcau)
kytukhac=set()
for kytu in doanvan:
    if not kytu.isalnum() and kytu != " ":
        kytukhac.add(kytu)
if kytukhac:
    print('Doan van co chua cac ky tu khac chu va so')
else:
    print('Doan van khong chua cac ky tu khac va so')
thaythe = doanvan.replace('Việt Nam','VIỆT NAM')
print(f'Doan van da duoc thay the la:',thaythe)
print('-----------------')

