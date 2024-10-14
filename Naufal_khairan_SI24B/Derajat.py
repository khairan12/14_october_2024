suhu = float(input("masukkan suhu dalam derajat celcius"))

if suhu<0:
    print("suhu dibawah titik beku")
elif suhu>100:
    print("suhu diatas titik didih")
else:
    print("suhu normal")