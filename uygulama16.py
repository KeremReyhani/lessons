#kullanıcıdan 234 34-58 şablonunda telefon numarası girmesini iste, numarayı göster, yanlış girileni belirt.
import re
def check_number(phone_number):
    pattern=re.compile(r"^\d{3} \d{2}-\d{2}$")
    result=pattern.search(phone_number)
    if result:
        return result.group()
    return "Numarayı istenen şablonda giriniz!"

print(check_number("123 44-55"))
print(check_number("x123 44-55"))
print(check_number("123 544-55"))
print(check_number("123 44-55sdf"))

print()
print()

#sdlkşg6545fh sdg45465fdfdd 1656 dsfdsg rakamları liste içine çıkar
test_string="sdlkşg6545fh sdg45465fdfdd 1656 dsfdsg"
pattern="\d+"
result=re.findall(pattern, test_string)
print(result)