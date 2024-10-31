class Human:
    def __init__(self):
        self.friends=[]
    def add_friends(self, friend):
        self.friend=friend
        self.friends.append(self.friend)
        #raise NotImplementedError("friend can't be add")

human_1=Human()
human_1.add_friends("ahmet")
#print(human_1.friends)
human_1.add_friends("mehmet")
#print(human_1.friends)




friends=["ahmet", "mehmet", "fatma"]
def select_best_friend(friend):
    if type(friend) is not str:
       raise TypeError("friend name must be string")
    if friend not in friends:
        raise ValueError("entered name must be in friends list")
    print(f"en iyi arkadaşım : {friend}")
select_best_friend("ahmet")
#select_best_friend(35)
#select_best_friend("kerem")


class MyCustomTypeError(TypeError):
    def __init__(self, message, code):
        super().__init__(f"hata kodu: {code}: {message}")
        self.code=code

friends=["ahmet", "mehmet", "fatma"]
def select_best_friend(friend):
    if type(friend) is not str:
       raise MyCustomTypeError("friend must be string", 1903)
    if friend not in friends:
        raise ValueError("entered name must be in friends list")
    print(f"en iyi arkadaşım : {friend}")
select_best_friend(True)

