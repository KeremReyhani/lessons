import os.path
print(os.path.basename("C:/Users/kerem/Desktop/Python/Yeni/41.ospath modülü.py")) #en içtekinin ismini verir
print(os.path.basename("C:/Users/kerem/Desktop/Python/Yeni"))
print(os.path.dirname("C:/Users/kerem/Desktop/Python/Yeni/41.ospath modülü.py")) #dosya yolunu gösterir
print(os.path.dirname("C:/Users/kerem/Desktop/Python/Yeni"))
print(os.path.exists("C:/Users/kerem/Desktop/Python/Yeni/41.ospath modülü.py")) #dosya yolunun olup olmadığını söyler
print(os.path.exists("C:/Users/kerem/Desktop/Python/Yeni2"))
print(os.path.isfile("C:/Users/kerem/Desktop/Python/Yeni/41.ospath modülü.py")) #dosyaya mı ait
print(os.path.isdir("C:/Users/kerem/Desktop/Python/Yeni")) #klasöre mi ait
print(os.path.join(r"C:/Users/kerem/Desktop/Python", r"Yeni/41.ospath modülü.py")) #ikisini birleştirir
print(os.path.split("C:/Users/kerem/Desktop/Python/Yeni/41.ospath modülü.py")) #dosya yolunu ve dosyayı tuple'ye çevirir.

dirname, filename=os.path.split("C:/Users/kerem/Desktop/Python/Yeni/41.ospath modülü.py")
print(dirname)
print(filename)