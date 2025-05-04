# i: grid  . -> open without checkpoints, * -> pass with checkpoints, # -> wall
# checkpoint <= 300
# pick k checkpoints , find min # of squares(edges) to pass all checkpoints
# start any cell , end any cell
# field = [
#  "*#..#",
#  ".#*#.",
#  "*...*"]
# K = 2
from collections import deque

def expectedLength(list, k):
  grid, checkpoints = createGrid(list) # [[]]
  memo = {} # i: list of points 
  kPoints = findKPoints(k, checkpoints, 0, memo) # [[() * k ]]

  # for every k point in findKPoints 
  finaMin = float('inf')
  for pointCount in kPoints:
    for row in range(len(grid)):
      for col in range(len(grid[0])):
        if grid[row][col] != "#":
          startPoint = (row, col)
          currentMin = exploreGrid(startPoint, grid, set(pointCount))
          if currentMin:
            finaMin = min(currentMin, finaMin)
    
  return finaMin 
    

def createGrid(MyList):
  grid = []
  checkpoints = []
  for index, string in enumerate(MyList):
    row = list(string) # "*#..#" -> ['*', '#' , ....]
    for i, char in enumerate(row):
      if char == "*":
        checkpoints.append((index, i))
    grid.append(row)

  return grid, checkpoints
    
def findKPoints(k, checkpoints, i, memo):

  
  # bc  
  if k == 0:
    return [[]]
  if i in memo:
    return memo[i]

  if i == len(checkpoints):
    return []

  point = checkpoints[i]

  inclusive = findKPoints(k-1, checkpoints, i+1, memo) # [[]]
  exclusive = findKPoints(k, checkpoints, i+1, memo)   # []


  finalCheckPoints = []
  for index, points in enumerate(inclusive):    
    inclusive[index] = points + [point]

  
  memo[i] = inclusive + exclusive
  return memo[i]

  
def exploreGrid(startPoint, grid, kPoints):
  # BFT 
  row, col = startPoint
  queue = deque([(row, col, 0)])  
  vistited = set()
  visiting = set()
  done = set()

  while queue:
    row, col, distance = queue.popleft()

    # inbound
    row_inbound = 0 <= row < len(grid)
    col_inbound = 0 <= col < len(grid[0])
    if not row_inbound or not col_inbound:
      continue    

    if grid[row][col] == '#': # wall
      continue

    if (row, col) in vistited:
      continue
      
    # print("Done", done)
    # print("kPoints", kPoints)

    if (row, col) in kPoints:      
      done.add((row,col)) 

    if len(done) == len(kPoints):
      break 
    
    if (row, col) in visiting:
      vistited.add((row, col))
      visiting.remove((row,col))
      continue
    visiting.add((row, col))               

    up = (row-1, col)
    down = (row +1, col)
    left = (row, col -1)
    right = (row, col +1)
    neighbors = [up, down, left, right]

    queue.append((row,col, distance))
    for neighbor in neighbors:
      row, col = neighbor
      queue.append((row, col, distance+1))
  return distance

# 1  
field = [
 "*#..#",
 ".#*#.",
 "*...*"]
print("Test case 1")
print(expectedLength(field, 2) == 3.8333333333333353)

# 2
field2 = [
 "*#..#",
 ".#*#.",
 "*...*"]
K = 4
# Returns: 8.0
print("Test case 2")
print(expectedLength(field2, 4) == 8.0)

# 3
field3 = [
 "#.#**",
 "....#",
 "#*#**",
 "**#*#",
 "#..##",
 "*#..#",
 ".#.#.",
 "....*"]
K = 3
# Returns: 10.825000000000024

print("Test case 2")
print(expectedLength(field3, 3) == 10.825000000000024)


# 4
field = [    	
 "###################",
 "#*###############*#",
 "#.....#######.....#",
 "#*###*.#.*.#.*###*#",
 "#*####*.*#*.*####*#",
 "#*#####*###*#####*#",
 "###################"]
K = 9
#Returns: 30.272233648704244

print("Test case 4")
print(expectedLength(field3, 9) == 30.272233648704244)






  
  