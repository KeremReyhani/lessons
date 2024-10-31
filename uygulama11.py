try: #kod çalışmazsa exception bloğuna girer
    print(12/0)
except KeyError:
    print("Key Error")
except ZeroDivisionError:
    print("ZeroDivisionError")
finally:
    print("her türlü çalışırım")

try:
    print(12/0)
except Exception:
    print("Exception")
except ZeroDivisionError:
    print("ZeroDivisionError")
else:
    print("bölme işlemi başarıyla sonuçlandı")

try:
    print(12/2)
except Exception:
    print("Exception")
except ZeroDivisionError:
    print("ZeroDivisionError")
else:
    print("bölme işlemi başarıyla sonuçlandı")



try:
    num = int(input("lütfen bir sayı giriniz"))
except:
    print("girdiğiniz bir sayı değildir")
else:
    print(f"Girdiğiniz değer: {num}")


try:
    num = int(input("lütfen bir sayı giriniz"))
except:
    print("girdiğiniz bir sayı değildir")
else:
    print(f"Girdiğiniz değer: {num}")
finally:
    print("her türlü çalışırım")