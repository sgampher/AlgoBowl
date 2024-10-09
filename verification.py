#Authors: Sara Gampher, Kathryn Bruce, Dishita Sharma
#AlgoBowl main.py


def checkCoverage(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if isinstance(grid[row][col], int):
                check=False
                # Check left (move left along the row)
                for c in range(col, -1, -1):
                    if isinstance(grid[row][c], int) and grid[row][c] != -1:  # Found another light bulb
                        check = True
                    elif not grid[row][c] == -1 and grid[row][c].startswith("G"):
                        break
                    # Check right (move right along the row)
                if (check == False):
                    for c in range(col, len(grid[row])):
                        if isinstance(grid[row][c], int)  and grid[row][c] != -1: # Found another light bulb
                            check =True
                        elif not grid[row][c] == -1 and grid[row][c].startswith("G"): # Stop if you hit a grey cell
                            break
                    # Check up (move up along the column)
                if (check == False):
                    for r in range(row, -1, -1):
                        if isinstance(grid[r][col], int)  and grid[r][col] != -1:  # Found another light bulb
                            check = True
                        elif not grid[r][col] == -1 and grid[r][col].startswith("G"):  # Stop if you hit a grey cell
                            break
                if (check == False):
                    # Check down (move down along the column)
                    for r in range(row, len(grid)):
                        if isinstance(grid[r][col], int) and grid[r][col] != -1:  # Found another light bulb
                            check =True
                        elif not grid[r][col] == -1 and grid[r][col].startswith("G"):  # Stop if you hit a grey cell
                            break
                if check == False:
                    return False
            
            
    return True
            

def totalViolations(grid):
    total = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if isinstance(grid[row][col], int) and grid[row][col] != -1:  # Checking if it's a light bulb (indicated by int)
                temp = lightBulbViolations(grid, (row, col))
                
                total += temp
                grid[row][col] = temp

            #elif not (grid[row][col] == -1) and (grid[row][col].startswith("G")) and (len(grid[row][col])>1): 
            #    total += greyCellViolations(grid, (row, col))
    #print(grid)            
    for row in range(len(grid)):
            for col in range(len(grid[row])):
                if not(isinstance(grid[row][col], int)) and not (grid[row][col] == -1) and (grid[row][col].startswith("G")) and (len(grid[row][col])>1): 
                   total += greyCellViolations(grid, (row, col))
                #total += temp
                #grid[row][col] = temp
    return total

# Lightbulb Violation Calculation
def lightBulbViolations(grid, position):
    violationCount = 0
    row, col = position

    # Check left (move left along the row)
    for c in range(col-1, -1, -1):
        if isinstance(grid[row][c], int)  and grid[row][c] != -1:  # Found another light bulb
            violationCount += 1
        elif not grid[row][c] == -1 and grid[row][c].startswith("G"):  # Stop if you hit a grey cell
            break
        

    # Check right (move right along the row)
    for c in range(col+1, len(grid[row])):
        if isinstance(grid[row][c], int)  and grid[row][c] != -1:  # Found another light bulb
            violationCount += 1
        elif not grid[row][c] == -1 and grid[row][c].startswith("G"):  # Stop if you hit a grey cell
            break
        

    # Check up (move up along the column)
    for r in range(row-1, -1, -1):
        if isinstance(grid[r][col], int)  and grid[r][col] != -1:  # Found another light bulb
            violationCount += 1
        elif not grid[r][col] == -1 and grid[r][col].startswith("G"):  # Stop if you hit a grey cell
            break
        

    # Check down (move down along the column)
    for r in range(row+1, len(grid)):
        if isinstance(grid[r][col], int)  and grid[r][col] != -1:  # Found another light bulb
            violationCount += 1
        elif not grid[r][col] == -1 and grid[r][col].startswith("G"):  # Stop if you hit a grey cell
            break
        

    return violationCount


def greyCellViolations(grid, position):
    violations = 0
    row, col = position

    # Check all four neighboring cells
    #for r_offset, c_offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        #r = row + r_offset
        #c = col + c_offset

        #if 0 <= r < len(grid) and 0 <= c < len(grid[r]):
            # Check if the neighboring cell is a gray cell with a number
    if not(isinstance(grid[row][col], int)) and grid[row][col].startswith("G"):  # Only consider cells starting with 'G'
        if len(grid[row][col]) > 1:  # Ensure there is a number after 'G'
            required_bulbs = int(grid[row][col][1])
            # Add to violations based on the number of light bulbs in neighbors
            current_bulbs = countBulbsInNeighbors(grid, (row, col))
            if current_bulbs != required_bulbs:
                violations = 1

    return violations

def countBulbsInNeighbors(grid, position):
    count = 0
    row, col = position
    #Check all four neighboring cells
    for r_offset, c_offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        r = row + r_offset
        c = col + c_offset

        if 0 <= r < len(grid) and 0 <= c < len(grid[r]):
            if isinstance(grid[row][c], int) and grid[row][c] != -1:  # Count the light bulbs
                count += 1

    return count



def main():
    # Initialize variables
    # grid = []
    
    # # Read input
    # firstline = input().split(" ")
    # rows = int(firstline[0])
    # cols = int(firstline[1])

    # Read the file and store its contents in a list of lines
    file = 'input_group864.txt'
    grid = []

    with open(file, 'r') as file:
        lines = file.readlines()

        theirViol = int(lines[0].strip().split()) 
        rows = 315
        for i in range(1, rows + 1):  
            nextline = lines[i].strip()  
            addThis = []
            for n in nextline:
                if n == ".":
                    addThis.append(-1) 
                if n == "L":
                    addThis.append(1) 
                elif n == "0":
                    addThis.append("G0")
                elif n == "1":
                    addThis.append("G1")
                elif n == "2":
                    addThis.append("G2")
                elif n == "3":
                    addThis.append("G3")
                elif n == "4":
                    addThis.append("G4")
                elif n == "X":
                    addThis.append("G")  # Gray cell
            grid.append(addThis)

    # Now grid contains the processed grid
    # Print the grid for verification
    #for row in grid:
    #    print(row)

# Further processing, such as removing violations and checking coverage, can be done here.
 
    # Loop through, remove violations, check coverage, repeat
    
    # Count violations
    print(grid)
    if(checkCoverage(grid)):
        totalViolations(grid)
        finalTotalCount = 0
        for row in range(int(rows)):
            for col in range(int(cols)):
                if isinstance(grid[row][col], int) and  grid[row][col] > 0:
                    finalTotalCount+= 1
                    print(finalTotalCount)
                if not isinstance(grid[row][col], int) and grid[row][col].startswith("G") and (len(grid[row][col])>1):
                    temp = greyCellViolations(grid, (row,col)) 
                    if temp > 0:# ADD ONE TO THE COUNT IF GREY CELL VIOLATION IS A NUMBER BASICALLY 
                        finalTotalCount+= 1 
        if(finalTotalCount == theirViol):
            print(True)


    

           


if __name__ == '__main__':
    main()