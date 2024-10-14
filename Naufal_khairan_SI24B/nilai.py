nilai =int(input("masukkan nilai ujian (0-100):"))

if nilai>=85:
    print("sangat baik")
elif nilai>=70:
    print("baik")
elif nilai>=55:
    print("cukup")
elif nilai>=40:
    print("kurang")
else:
    print("sangat kurang")