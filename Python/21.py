class HocVien:
    def __init__(self,name,date,email,sdt,diachi,lop):
        self.name = name
        self.date = date
        self.email = email
        self.sdt = sdt
        self.diachi = diachi
        self.lop = lop
    def showInfo(self):
        print('Name: ', self.name)
        print('Date: ', self.date)
        print('Email: ', self.email)
        print('Sdt: ', self.sdt)
        print('Diachi: ', self.diachi)
        print('Lop: ', self.lop)
    def changeinfo(self, diachi='Ha Noi', lop='IT14.3'):
        self.diachi = diachi
        self.lop = lop
        print('Thong tin da cap nhat')
hv1= HocVien('Vu Quoc Khanh','20/11/2005','hanvx39@gmail.com','0378817663','Vinh Phuc','It14.4')
hv1.changeinfo()
hv1.showInfo()
print('----------------------------')
hv2 = HocVien('Hehe','12/2/2007','hhhhhh@gmail.com','03333333333','Kon Tum','It13.66')
hv2.showInfo()
print('----------------------------')

import math


class PhanSo:
    def __init__(self, tu_so, mau_so=1):
        self.tu_so = tu_so
        self.mau_so = mau_so
        self.toi_gian()

    def tong(self, other):
        tu_moi = (self.tu_so * other.mau_so) + (other.tu_so * self.mau_so)
        mau_moi = self.mau_so * other.mau_so
        return PhanSo(tu_moi, mau_moi)

    def hieu(self, other):
        tu_moi = (self.tu_so * other.mau_so) - (other.tu_so * self.mau_so)
        mau_moi = self.mau_so * other.mau_so
        return PhanSo(tu_moi, mau_moi)

    def nhan(self, other):
        tu_moi = self.tu_so * other.tu_so
        mau_moi = self.mau_so * other.mau_so
        return PhanSo(tu_moi, mau_moi)

    def chia(self, other):
        if other.tu_so == 0:
            raise ValueError("Lỗi: Không thể chia cho phân số có giá trị bằng 0!")
        tu_moi = self.tu_so * other.mau_so
        mau_moi = self.mau_so * other.tu_so
        return PhanSo(tu_moi, mau_moi)

    def toi_gian(self):
        ucln = math.gcd(self.tu_so, self.mau_so)
        self.tu_so = self.tu_so // ucln
        self.mau_so = self.mau_so // ucln

        if self.mau_so < 0:
            self.tu_so = -self.tu_so
            self.mau_so = -self.mau_so
        return self

    def __str__(self):
        if self.mau_so == 1:
            return f"{self.tu_so}"
        return f"{self.tu_so}/{self.mau_so}"

ps1 = PhanSo(3, 2)
ps2 = PhanSo(3, 5)

print(f"Phân số 1: {ps1}")
print(f"Phân số 2: {ps2}")
print(f"Chia: {ps1.chia(ps2)}")
print(f"Tổng: {ps1.tong(ps2)}")
print(f"Hiệu: {ps1.hieu(ps2)}")
print(f"Nhân (ps2 * ps2): {ps2.nhan(ps2)}")
