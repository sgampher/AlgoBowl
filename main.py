#Authors: Sara Gampher, Kathryn Bruce, Dishita Sharma
#AlgoBowl main.py


def checkCoverage(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            check=False
            # Check left (move left along the row)
            for c in range(col-1, -1, -1):
                if isinstance(grid[row][c], int) and grid[row][c] != -1:  # Found another light bulb
                    check = True
                elif not grid[row][c] == -1 and grid[row][c].startswith("G"):
                    break
                # Check right (move right along the row)
            if (check == False):
                for c in range(col + 1, len(grid[row])):
                    if isinstance(grid[row][c], int)  and grid[row][c] != -1: # Found another light bulb
                        check =True
                    elif not grid[row][c] == -1 and grid[row][c].startswith("G"): # Stop if you hit a grey cell
                        break
                # Check up (move up along the column)
            if (check == False):
                for r in range(row - 1, -1, -1):
                    if isinstance(grid[r][col], int)  and grid[r][col] != -1:  # Found another light bulb
                        check = True
                    elif not grid[r][col] == -1 and grid[r][col].startswith("G"):  # Stop if you hit a grey cell
                        break
            if (check == False):
                # Check down (move down along the column)
                for r in range(row + 1, len(grid)):
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
    for c in range(col, -1, -1):
        if isinstance(grid[row][c], int)  and grid[row][c] != -1:  # Found another light bulb
            violationCount += 1
        elif not grid[row][c] == -1 and grid[row][c].startswith("G"):  # Stop if you hit a grey cell
            break
        

    # Check right (move right along the row)
    for c in range(col, len(grid[row])):
        if isinstance(grid[row][c], int)  and grid[row][c] != -1:  # Found another light bulb
            violationCount += 1
        elif not grid[row][c] == -1 and grid[row][c].startswith("G"):  # Stop if you hit a grey cell
            break
        

    # Check up (move up along the column)
    for r in range(row, -1, -1):
        if isinstance(grid[r][col], int)  and grid[r][col] != -1:  # Found another light bulb
            violationCount += 1
        elif not grid[r][col] == -1 and grid[r][col].startswith("G"):  # Stop if you hit a grey cell
            break
        

    # Check down (move down along the column)
    for r in range(row, len(grid)):
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

def findHighestViolation(grid, checkCell):
    highest_violation = 0
    highest_position = None

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            violations = 0
            
            if isinstance(grid[row][col], int) and grid[row][col] != -1:  # Only consider cells where a light bulb can be placed
                violations += lightBulbViolations(grid, (row, col)) #+ greyCellViolations(grid, (row, col))#ISSUE WE WANT TO LOOK AT GREY CELL AROUND THE CELL
            if row+1 < len(grid) and not(isinstance(grid[row+1][col], int)) and grid[row+1][col].startswith("G") and (len(grid[row+1][col])>1):
                violations += greyCellViolations(grid, (row+1, col))
            if row-1 >= 0 and not(isinstance(grid[row-1][col], int)) and grid[row-1][col].startswith("G") and (len(grid[row-1][col])>1):
                violations += greyCellViolations(grid, (row-1, col))
            if col+1 < len(grid[row]) and not(isinstance(grid[row][col+1], int)) and grid[row][col+1].startswith("G") and (len(grid[row][col+1])>1):
                violations += greyCellViolations(grid, (row, col+1))
            if col-1 >= 0 and not(isinstance(grid[row][col-1], int)) and grid[row][col-1].startswith("G") and (len(grid[row][col-1])>1):
                violations += greyCellViolations(grid, (row, col-1)) 
            

            if violations > highest_violation and checkCell == None:
                highest_violation = violations
                highest_position = (row, col)  
            elif violations> highest_violation and not((row,col) in checkCell):# if doesnt work HERE:
                highest_violation = violations
                highest_position = (row, col)
 
    
    return highest_position



def main():
    # Initialize variables
    # grid = []
    
    # # Read input
    # firstline = input().split(" ")
    # rows = int(firstline[0])
    # cols = int(firstline[1])

    # Read the file and store its contents in a list of lines
    file = 'input_group810.txt'
    grid = []

    with open(file, 'r') as file:
        lines = file.readlines()

        rows, cols = map(int, lines[0].strip().split()) 
        for i in range(1, rows + 1):  
            nextline = lines[i].strip()  
            addThis = []
            for n in nextline:
                if n == ".":
                    addThis.append(0) 
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
    curr_violation_count = totalViolations(grid)
    checkedCells = []
    count = 0
    highViol = findHighestViolation(grid, None)
    while highViol != None and not(highViol in checkedCells):
        #print(highViol)
        if not (highViol in checkedCells) and highViol !=None:
            checkedCells.append(highViol)
            # Make a copy of the grid and place a light bulb in the cell with the highest violation
            potentialNewGrid = [row[:] for row in grid]  # Create a deep copy
            #print(potentialNewGrid)
            potentialNewGrid[highViol[0]][highViol[1]] = -1  # Place a light bulb

        new_violation_count = totalViolations(potentialNewGrid)
        # Check if this placement is valid
        if checkCoverage(potentialNewGrid):
            print("go")
            if new_violation_count <= curr_violation_count:
                grid = potentialNewGrid
                curr_violation_count = new_violation_count
        #print(curr_violation_count) 
        highViol = findHighestViolation(grid, checkedCells)
        count = count+1
        print(count)
        
              

    finalTotalCount = 0
    printgrid = grid
    for row in range(int(rows)):
        for col in range(int(cols)):
            if isinstance(printgrid[row][col], int) and  printgrid[row][col] >0:
                printgrid[row][col] = 1
                finalTotalCount+= 1
            if not isinstance(printgrid[row][col], int) and grid[row][col].startswith("G") and (len(grid[row][col])>1):
                temp = greyCellViolations(printgrid, (row,col))
                if temp >1:
                    finalTotalCount+= 1

    #print(printgrid)

    
    # Write results to output
    with open('output_group810.txt', 'w') as f:
        f.write(str(finalTotalCount) + '\n')  # Convert the violation count to string
        for i in range(int(rows)):
            for j in range(int(cols)):
                if printgrid[i][j] == "G0":
                    f.write('0')
                elif printgrid[i][j] == "G1":
                    f.write('1')
                elif printgrid[i][j] == "G2":
                    f.write('2')
                elif printgrid[i][j] == "G3":
                    f.write('3')
                elif grid[i][j] == "G4":
                    f.write('4')  
                elif printgrid[i][j] == "G": 
                    f.write('X')  # Gray cell
                elif printgrid[i][j] == -1 :  # Blank cell
                    f.write('.')  
                else:
                    f.write('L')  # Light bulb
            f.write('\n')
           


if __name__ == '__main__':
    main()