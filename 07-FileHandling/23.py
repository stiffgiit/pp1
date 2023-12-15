with open("pusty.txt", "w") as file:
    for line in range(1,11):
        sq = line**2
        cub = line**3
        file.write(f"{line},{sq},{cub}\n")
        
        