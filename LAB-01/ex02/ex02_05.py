#nhap so gio lam
so_gio_lam =float(input("nhap so gio lam: "))
#nhap luong gio
luong_gio = float(input("nhap muc luong tren moi gio: "))
gio_tieu_chuan = 44 #so gio lam chuan
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan) #so gio lam vuot chuan moi tuan
thuc_linh = gio_tieu_chuan * luong_gio + gio_vuot_chuan * luong_gio * 1.5 #tinh tong thu nhap
#ham xuat ra man hinh muc thu nhap
print (f"so tien thuc linh cua nhan vien: {thuc_linh}")