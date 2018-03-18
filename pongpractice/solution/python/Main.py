# Solution to PongPractice in Python

# Input Constraints:
#   Length of Court
#   Width of Court
#   Start Position
#   Starting Direction
#   Player Hits

length = 0
width = 0
ballStart = 0
ballDir = ""
playerHits = 0

length = int(input())
width = int(input())
ballStart = int(input())
ballDir = str(input())
playerHits = int(input())

# Start Position starts at Zero
court = []

#court = [[" "] * (width + 2)] * (length + 2)
#court[0] = ["*"] * (length + 2)
#court[width] = ["*"] * (length + 2)

#court = [["*"] * width for x in range(length) if (x == length)]
#court = [["*"] * width if (x == length - 1 or x == 0) else [" "] * width for x in range(length)]

# Adjust for the Court Boundary Characters
length += 2
width += 2

# List comprehension to make the court.
court = [["*"] * length if (x == width - 1 or x == 0) else [" " if (y < length - 1) else "*" for y in range(length)] for x in range(width)]

# Move the ball

ballR = ballStart + 1
ballC = 0
up = (ballDir == "NE")
right = True

while (playerHits >= 0):
  #print ("POS: " + str(ballR) + " " + str(ballC))
  court[ballR][ballC] = "."
  
  if ballC >= length - 2:
    right = False
    
  if ballC <= 0:
    right = True
    playerHits -= 1
  
  if ballR >= width - 2:
    up = True
    
  if ballR <= 1:
    up = False
    
  if up:
    ballR -= 1
  else:
    ballR += 1
    
  if right:
    ballC +=1
  else:
    ballC -= 1

#print ("Added: " + str(ballR) + " "  + str(ballC))
#court[ballR][ballC] = "." 
  

for row in court:
  for c in row:
    print(c ,end='')
  print("")