numbers=[3, 7, 5, 9, 11]
for x in numbers:
    print(x)

name="keremreyhani"
for harf in name:
    print(harf)

for x in range(5,10):
    print(x)

for x in range(5,15,2):
    print(x)

friends={"joey":"acting", "ross":"dinosaur", "rachel":"fashion", "monica":"cooking"}
for k,v in friends.items():
    print(k,v)

friends={"joey":"acting", "ross":"dinosaur", "rachel":"fashion", "monica":"cooking"}
for k,v in friends.items():
    if k == "rachel":
        break
    print(k,v)

friends={"joey":"acting", "ross":"dinosaur", "rachel":"fashion", "monica":"cooking"}
for k,v in friends.items():
    if k == "rachel":
        continue
    print(k,v)

takımlar=["beşiktaş", "fenerbahçe", "galatasaray", "trabzonspor", "hatayspor"]
for i, takım in enumerate(takımlar):
    print(i, takım)