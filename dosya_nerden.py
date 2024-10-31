print(__name__) #direkt o dosyadan mı yoksa başka dosyadan import edildiğini mi gösterir

def hello():
    print("kerem")
if __name__=="__main__":
    hello()

if __name__=="dosya_nerden":
    hello()
