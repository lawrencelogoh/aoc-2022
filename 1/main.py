def main() -> None:
    f = open("file.txt", "r")
    lines = f.readlines()
    f.close()
    
    all_calories = []
    calories = []
    
    for l in lines:
        if l != "\n":
            calories.append(int(l.strip()))
        else:
            all_calories.append(sum(calories))
            calories=[]

    #pt 1
    print(max(all_calories))

    #pt 2
    all_calories.sort()
    print(sum(all_calories[-3:]))
if __name__ == "__main__":
    main()
