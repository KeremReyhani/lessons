movies_file="movies.csv"
def fl_add_movie(name, director):
    with open(movies_file, "a") as f:
        f.write(f"{name}, {director}, {False}\n") #False: ilk başta izlenmemiş kabul edilir.

def fl_list_movies():
    with open(movies_file, "r") as f:
        lines=[]
        for line in f.readlines():
            lines.append(line.strip().split(","))
        #lines=[line.strip().split(",") for line in f.readlines()]
    return [{"name":line[0], "director":line[1], "watched":line[2]} for line in lines]

def fl_watch_movie(name):
    movies=fl_list_movies()
    for movie in movies:
        if movie["name"]==name:
            movie["watched"]=True

    fl_save_movies(movies) #kaydetmek için

def fl_save_movies(movies):
    with open(movies_file, "w") as f:
        for movie in movies:
            f.write(f"{movie['name']}, {movie['director']}, {movie['watched']}\n")

def fl_delete_movie(name):
    movies=fl_list_movies()
    movies=[movie for movie in movies if movie["name"]!=name]
    fl_save_movies(movies)
