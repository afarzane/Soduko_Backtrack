board = [[8, 1, 0, 0, 3, 0, 0, 2, 7], 
         [0, 6, 2, 0, 5, 0, 0, 9, 0], 
         [0, 7, 0, 0, 0, 0, 0, 0, 0], 
         [0, 9, 0, 6, 0, 0, 1, 0, 0], 
         [1, 0, 0, 0, 2, 0, 0, 0, 4], 
         [0, 0, 8, 0, 0, 5, 0, 7, 0], 
         [0, 0, 0, 0, 0, 0, 0, 8, 0], 
         [0, 2, 0, 0, 1, 0, 7, 5, 0], 
         [3, 8, 0, 0, 7, 0, 0, 4, 2]]
    
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
            
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
                
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return(i, j) #return row, column
            
def check_valid(bo, num, pos):
    #Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
        
    #Check column
    for j in range(len(bo)):
        if bo[j][pos[1]] == num and pos[0] != i:
            return False
        
    #Check box
    pos_x = pos[1] // 3
    pos_y = pos[0] // 3
    
    for i in range(pos_y*3, pos_y*3 + 3):
        for j in range(pos_x*3, pos_x*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
        
    return True
    
    
def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
        
    for i in range(1,10):
        if check_valid(bo, i, (row, col)):
            bo[row][col] = i
            
            if solve(bo):
                return True
            
            bo[row][col] = 0
            
    return False

print_board(board)
print("-------------------------")
solve(board)
print_board(board)
    
    
    
    
            
    
    