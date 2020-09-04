#Yingxuan Wang
#Surrounded regions

#1. all O's in the border are not converted to X
#2. all O's connected to the border O's are not converted to X
#3. all O's connected to O's in step2 are not converted to X
#for searching connections, I'll be using DFS

def SR(board):
    row = len(board)
    col = len(board[0])
    directions = [(-1,0), (0,1), (1,0), (0,-1)]
    visited = set()

    def dfs(i, j):
        #check the surrounding area of the visited position to see if they are O
        for xaxis, yaxis in directions:
            nx, ny = i+xaxis, j+yaxis
            if 0<=nx<row and 0<=ny<col and board[nx][ny]=='O' and \
               (nx, ny) not in visited:
                visited.add((nx,ny))
                board[nx][ny] = 'escape'
                dfs(nx, ny)
                
    #check the borderlines            
    for i in range(row):
        for j in range(col):
            if (i==0 or i==row-1 or j==0 or j==col-1) and \
               board[i][j]=='O' and (i,j) not in visited:
                #mark the current position as an escape, which means this O won't be changed
                board[i][j]='escape'
                visited.add((i,j))
                #to check the connected symbols
                dfs(i,j)
    
    #change all non-esapce O's into X's
    for i in range(row):
        for j in range(col):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'escape':
                board[i][j] = 'O'
    #return board
#print(SR([['X','X','X','X'], ['X','X','O','X'], ['X','O','X','X'], ['X','O','X','X']]))