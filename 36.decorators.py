#DECORATORS: diğer fonksiyonları çevreleyerek onlara ekstra özellikler katar.

def merhaba(func):    #merhaba decorator olur.
    def wrapper():
        print("Fonksiyondan önce yazdırıyoruz.")
        func()
        print("Fonksiyondan sonra yazdırıyoruz.")
    return wrapper

@merhaba
def lang_es():
    print("hola")

lang_es()


user={
    "username": "kerem",
    "role": "admin"
}

def check_admin(func):
    def wrapper():
        if user.get("role")=="admin":
            return func()
        else:
            raise PermissionError("yetkiniz yok")
    return wrapper

@check_admin
def delete_product():
    print("ürün silindi")

delete_product()



def merhaba(func):
    def wrapper(name,age):
        print("Fonksiyondan önce yazdırıyoruz.")
        func(name,age)
        print("Fonksiyondan sonra yazdırıyoruz.")

    return wrapper

@merhaba
def info(name,age):
    print(f"benim adım {name}, yaşım {age}")
info("kerem", 18)


def merhaba(func):
    def wrapper(*args,**kwargs):
        print("Fonksiyondan önce yazdırıyoruz.")
        func(*args,**kwargs)
        print("Fonksiyondan sonra yazdırıyoruz.")

    return wrapper

@merhaba
def info(name,age,gender):
    print(f"benim adım {name}, yaşım {age}. cinsiyet:{gender}")
info("kerem", 18, "M")
