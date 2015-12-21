n = 20 + 1
grid = [[1 for x in range(n)] for x in range(n)] 
for a in range(1,n):
	for b in range(1,n):
		grid[a][b]=grid[a-1][b]+grid[a][b-1]
print(grid[n-1][n-1])