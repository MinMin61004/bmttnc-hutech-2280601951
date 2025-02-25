#ham kiem tra so nhi phan co chia het cho 5 hay k 
def chia_het_cho_5 (so_nhi_phan):
    so_thap_phan = int(so_nhi_phan,2)
    if so_thap_phan%5==0:
        return True
    else:
        return False

chuoi_so_nhi_phan = input("nhap chuoi so nhi phan(phan tach boi dau phay): ")

#tach chuoi thanh cac so nhi phan va kiem tra so chia het cho 5
so_nhi_phan_list = chuoi_so_nhi_phan.split(',')
so_chia_het_cho_5 = [so for so in so_nhi_phan_list if chia_het_cho_5 (so)]
#in ra cac so nhi phan chia het cho 5
if len(so_chia_het_cho_5) > 0:
    ket_qua = ','.join(so_chia_het_cho_5)
    print("cac so nhi phan chia het cho 5: ", ket_qua)
else:
    print("khong co so nhi phan nao chia het cho 5")