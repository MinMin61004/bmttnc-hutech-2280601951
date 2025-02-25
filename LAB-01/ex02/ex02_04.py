#tao mot danh sach rong de luu ket qua
j=[]
#duyet qua tat ca cac so trong doan khoang tu 2000- 3200
for i in range(2000,3201):
    if (i%7==0) and (i%5!=0): 
        j.append(str(i))
print (','.join(j))