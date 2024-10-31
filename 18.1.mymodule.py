import module_kavramı as m_m

numbers=[3, 8, 5, 11]
sum=m_m.summation(numbers)
print(sum)

print(m_m.mystring)

from module_kavramı import mystring,summation
sum=summation(numbers)
print(sum)
print(mystring)

import sys #python'ın modulleri aradığı yeri gösterir
print(sys.path)

#hazır moduller
import math
print(math.pi)
import random
number=[5, 6, 9, 12]
random_number=random.choice(number)
print(random_number)



