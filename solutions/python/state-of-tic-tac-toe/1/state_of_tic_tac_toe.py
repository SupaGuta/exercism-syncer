def gamestate(board):  
    # Count symbols on board 
    x = o = 0
    for ch in "".join(board):
        if ch == "X": x += 1
        elif ch == "O": o += 1

    # Check turn validity
    if x < o: raise ValueError("Wrong turn order: O started")
    if x > o + 1: raise ValueError("Wrong turn order: X went twice")
    
    # Build array with symbols in rows, columns and diagonals
    lines = []
    lines.extend(board) # rows
    lines.extend("".join(board[r][c] for r in range(3)) for c in range(3)) # columns
    lines.append("".join(board[i][i] for i in range(3)))   # diagonal (left to right)
    lines.append("".join(board[i][2 - i] for i in range(3)))  # diagonal (right to left)

    # Looking for winning lines
    winners = set()
    for line in lines:
        if line == "XXX": winners.add("X")
        elif line == "OOO": winners.add("O")

    # Check validity of winners    
    if len(winners) == 2: raise ValueError("Impossible board: game should have ended after the game was won")
    
    # Return game state
    if winners: return "win"
    if x + o == 9: return "draw"
    return "ongoing"