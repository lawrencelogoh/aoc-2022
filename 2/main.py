p1_possible_moves = {"A": 1, "B": 2, "C": 3}
p2_possible_moves = {"X": 1, "Y": 2, "Z": 3}

def outcome(s: str) -> int:
    moves=s.split()
    p1_move = p1_possible_moves[moves[0]]
    p2_move = p2_possible_moves[moves[1]]

    if p1_move == p2_move:
        #Tie
        return p2_move + 3
    elif p2_move == 1 and p1_move == 3:
        #win R S 
        return p2_move + 6
    elif p2_move == 2 and p1_move == 1:
       #win P R
        return p2_move + 6
    elif p2_move == 3  and p1_move == 2:
       #win R P
        return p2_move + 6
    else:
        return p2_move
    
def main() -> None:
    f = open("file.txt", "r")
    lines = f.readlines()
    f.close()
    guide = [x.strip() for x in lines] 

    points = 0

    for x in guide:
        points += outcome(x)
    
    print(points)


if __name__ == "__main__":
    main()
