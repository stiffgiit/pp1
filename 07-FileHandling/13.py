movie_titles = ["F&F7", "Robin Hood", "Incepcion", "interstellar", "Limitless"]

with open('movies.txt', 'w', encoding="utf-8") as file:
    for i in movie_titles:
        file.write(str(i) + "\n")
file.close()