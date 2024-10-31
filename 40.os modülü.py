#operating system modülü: işletim sistemine bağlı özellikleri kullanmayı sağlar.
import os
print(dir(os))
print(os.name) #işletim sistemini gösterir.
print(os.getcwd()) #klasörün yolunu gösterir.
#os.chdir(r"C:\Users\kerem\Desktop") #konumu değiştirir.
print(os.getcwd())
print(os.listdir()) #bulunduğu konumdaki dosyaları gösterir.
#os.mkdir("40.ders_deneme") #klasör oluşturur.
#os.makedirs("kerem/reyhani/18") #iç içe klasörler oluşturur.
#os.remove("sil.txt") #dosya siler
#os.rmdir("40.ders_deneme") #klasör siler.
#os.removedirs("kerem/reyhani/18") #iç içe klasörleri siler.
#os.rename("deneme", "deneme2") #isim değiştirir.

print()
print()
print()

path=r"C:\Users\kerem\Desktop\Python\Yeni"
for paths, dirs, files in os.walk(path): #bir klosörün ve içindekilerin haritalanması
    print(f"Paths: {paths}")
    print(f"Dirs: {dirs}")
    print(f"Files: {files}")

print()
print()
print()

print(os.stat("deneme2"))
