import re
pattern=re.compile("kerem")  #compile içindekini nesneye dönüştürür.
print(type(pattern))
print(help(pattern))

sample_text="ldskfhlsdg dfh56f645 keremsdmkflşd sg5h465"
result=pattern.search(sample_text)
print(result)   #pattern'in içindeki var mı yok mu (match)
print(result.group())



pattern=re.compile("kerem")  #compile içindekini nesneye dönüştürür.
print(type(pattern))

sample_text="ldskfhlsdg dfh56f645 yusufsdmkflşd sg5h465"
result=pattern.search(sample_text)
print(result)

print()
print()
print()
print()

#kısa yol
sample_text="ldskfhlsdg dfh56f645 keremsdmkflşd sg5h465"
result=re.search("kerem", sample_text)
print(result)
print(result.group())

result=re.match("kerem", sample_text)
print(result) #match'in eşleşmesi için aranan en başta olmalı

print()
print()
print()
print()

result=re.match("k", "kerem")
print(result)
result=re.search("k", "kerem")
print(result)
result=re.match("r", "kerem")
print(result)
result=re.search("x", "kerem")
print(result)

print()
print()
print()
print()

sample_text="lds135kfhlsdg dfh56f645 keremsdm486kflşd sg5h465"
result=re.findall(r"\d{3}", sample_text)       #var olan hepsini gösterir
print(result)
print(result[0])
print(type(result))

print()

result=re.finditer(r"\d{3}", sample_text)       #var olan hepsini gösterir
print(result)
for x in result:
    print(x.group())

print()

sample_text="kerem"

result=re.fullmatch(r"kerem", sample_text)       #birebir uyuşması durumunda
print(result)
print(result.group())

sample_text="kerem"

result=re.fullmatch(r"KEREM", sample_text, flags=re.IGNORECASE)
print(result)
print(result.group())
