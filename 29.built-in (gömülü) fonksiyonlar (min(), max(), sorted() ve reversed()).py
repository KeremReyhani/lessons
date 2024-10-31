#MAX-MİN iterable alır
print(max(3,99,-121,7))
print(min(3,99,-121,7))
print(max("a","t","b","e"))
print(min("a","t","b","e"))
print(max("kerem"))
list1=["cumhuriyet"]
print(max(list1))



#SORTED
nums=[3,9,26,18,25]
print(nums.sort())
nums.sort()
print(nums)

nums2=[6,4,17,58,1]
sorted(nums2)
print(sorted(nums2))
print(sorted(nums2, reverse=True))

friends=["kerem", "mustafa", "ege", "umut"]
print(sorted(friends))
print(sorted(friends, reverse=True))
print(sorted(friends, key=len, reverse=True))


#REVERSED
nums3=[7,8,3,5]
nums3.reverse()
print(nums3)

nums4=[17, 25, 8, 9, 16]
print(reversed(nums4))
for num in reversed(nums4):
    print(num)