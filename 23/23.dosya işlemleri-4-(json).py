import json
with open("data.json", "r") as f:
    content=json.load(f)
    print(content)
    print(type(content))
    print(type(content["friends"]))
    print(type(content["friends"][0]))
    for friend in content["friends"]:
        print(friend)
    for friend in content["friends"]:
        print(friend["name"])
    for friend in content["friends"]:
        del friend["age"]
        print(content)


with open("data.json", "r") as f, open("data2.json", "w") as f2:
    content=json.load(f)
    for friend in content["friends"]:
        del friend["age"]
    json.dump(content, f2)
