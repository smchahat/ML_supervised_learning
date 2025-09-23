grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

def check_nodes(r, c, grid):
    #if grid[r][c] == "2":
    #    return
            
    if grid[r][c] == "1":
        grid[r][c] = "2" # 0, 0  
        print("checking for values", r, c)
        # left node
        if c > 0 and c < len(grid[r]) :
            check_nodes(r, c-1, grid)
        # right node
        if (c == 0 or c > 0) and (c < len(grid[r]) -1) :
            check_nodes(r, c+1, grid)
        # top node
        if r > 0 and r < len(grid) :
            check_nodes(r-1, c, grid) 
        # bottom node
        if (r == 0 or r > 0) and r < len(grid) - 1 :
            check_nodes(r+1, c, grid)
            


island_count = 0

print(len(grid))

for rows in range(len(grid)):
    print(len(grid[rows]))
    for col in range(len(grid[rows])):
        #print("row and col", rows, col)
        if grid[rows][col] == "1": 
            #print("its 1 at : ", rows, col)
            #grid[rows][col] = "2"
            island_count += 1
            check_nodes(rows, col, grid)
            
        
print("no off islands : ", island_count)
print(grid)


            
            