#Authors: Sara Gampher, Kathryn Bruce, Dishita Sharma
#AlgoBowl main.py


#ISSUE - THE REASON WE ARE PRINTING A BUNCH OF LIGHTBULBS IS BECAUSE WE ARENT RETURNING OUR GRID 
# AND WE DONT PASS BY REFERENCE OR BY POINTER SO GRID IS NEVER UPDATED - FIX 

def checkCoverage(grid):
    check = True
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # Check left (move left along the row)
            for c in range(col - 1, -1, -1):
                if isinstance(grid[row][c], int) and grid[row][c] != -1:  # Found another light bulb
                    check =True
                    break
                elif not grid[row][c] == -1 and grid[row][c].startswith("G"):  # Stop if you hit a grey cell 
                    check = False
                

            # Check right (move right along the row)
            for c in range(col + 1, len(grid[row])):
                if isinstance(grid[row][c], int)  and grid[row][c] != -1: # Found another light bulb
                    check =True
                    break
                elif not grid[row][c] == -1 and grid[row][c].startswith("G"): # Stop if you hit a grey cell
                    check = False
                

            # Check up (move up along the column)
            for r in range(row - 1, -1, -1):
                if isinstance(grid[row][c], int)  and grid[row][c] != -1:  # Found another light bulb
                    check =True
                    break
                elif not grid[row][c] != -1 and grid[row][c].startswith("G"):  # Stop if you hit a grey cell
                    check = False


            # Check down (move down along the column)
            for r in range(row + 1, len(grid)):
                if isinstance(grid[row][c], int) and grid[row][c] != -1:  # Found another light bulb
                    check =True
                    break
                elif not grid[row][c] != -1 and grid[row][c].startswith("G"):  # Stop if you hit a grey cell
                    check = False
                
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
            elif not (grid[row][col].startswith("G")):  # Skip gray cells
                temp += greyCellViolations(grid, (row, col))
                total += temp
                grid[row][col] = temp
    return total

# Lightbulb Violation Calculation
def lightBulbViolations(grid, position):
    violationCount = 0
    row, col = position

    # Check left (move left along the row)
    for c in range(col - 1, -1, -1):
        if isinstance(grid[row][c], int)  and grid[row][c] != -1:  # Found another light bulb
            violationCount += 1
        elif not grid[row][c] != -1 and grid[row][c].startswith("G"):  # Stop if you hit a grey cell
            break
        

    # Check right (move right along the row)
    for c in range(col + 1, len(grid[row])):
        if isinstance(grid[row][c], int)  and grid[row][c] != -1:  # Found another light bulb
            violationCount += 1
        elif not grid[row][c] == -1 and grid[row][c].startswith("G"):  # Stop if you hit a grey cell
            break
        

    # Check up (move up along the column)
    for r in range(row - 1, -1, -1):
        if isinstance(grid[row][c], int)  and grid[row][c] != -1:  # Found another light bulb
            violationCount += 1
        elif not grid[row][c] != -1 and grid[row][c].startswith("G"):  # Stop if you hit a grey cell
            break
        

    # Check down (move down along the column)
    for r in range(row + 1, len(grid)):
        if isinstance(grid[row][c], int)  and grid[row][c] != -1:  # Found another light bulb
            violationCount += 1
        elif not grid[row][c] != -1 and grid[row][c].startswith("G"):  # Stop if you hit a grey cell
            break
        

    return violationCount


def greyCellViolations(grid, position):
    violations = 0
    row, col = position

    # Check all four neighboring cells
    for r_offset, c_offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        r = row + r_offset
        c = col + c_offset

        if 0 <= r < len(grid) and 0 <= c < len(grid[r]):
            # Check if the neighboring cell is a gray cell with a number
            if not(isinstance(grid[r][c], int)) and grid[r][c].startswith("G"):  # Only consider cells starting with 'G'
                if len(grid[r][c]) > 1:  # Ensure there is a number after 'G'
                    required_bulbs = int(grid[r][c][1])
                    # Add to violations based on the number of light bulbs in neighbors
                    current_bulbs = countBulbsInNeighbors(grid, (r, c))
                    if current_bulbs != required_bulbs:
                        violations += 1

    return violations

def countBulbsInNeighbors(grid, position):
    count = 0
    row, col = position

    # Check all four neighboring cells
    for r_offset, c_offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        r = row + r_offset
        c = col + c_offset

        if 0 <= r < len(grid) and 0 <= c < len(grid[r]):
            if isinstance(grid[row][c], int) and grid[row][c] != -1:  # Count the light bulbs
                count += 1

    return count

def findHighestViolation(grid):
    highest_violation = 0
    highest_position = None

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if isinstance(grid[row][col], int):  # Only consider cells where a light bulb can be placed
                violations = lightBulbViolations(grid, (row, col)) + greyCellViolations(grid, (row, col))
                if violations > highest_violation:
                    highest_violation = violations
                    highest_position = (row, col)
    if(highest_position):
        return highest_position


def main():
    # Initialize variables
    grid = []
    
    # Read input
    firstline = input().split(" ")
    rows = int(firstline[0])
    cols = int(firstline[1])
    
    # Read in the rest of the given input and store in grid
    for i in range(rows):
        nextline = input().strip()  # Read the line and remove any extra spaces
        addThis = []
        for n in nextline:
            if n == ".":
                addThis.append(0)  # Keep as a string
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
    
   
    # Loop through, remove violations, check coverage, repeat
    
    # Count violations
    curr_violation_count = totalViolations(grid)
    run = rows * cols
    for i in range(run+1):
        # Find cell with the highest violation
        highViol = findHighestViolation(grid)
        
        # Make a copy of the grid and place a light bulb in the cell with the highest violation
        potentialNewGrid = grid  # Create a deep copy
        print(potentialNewGrid)
        potentialNewGrid[highViol[0]][highViol[1]] = -1  # Place a light bulb


        # Check if this placement is valid
        if checkCoverage(potentialNewGrid):
            new_violation_count = totalViolations(potentialNewGrid)
            if new_violation_count < curr_violation_count:
                grid = potentialNewGrid
                curr_violation_count = new_violation_count

    # Write results to output
    with open('output.txt', 'w') as f:
        f.write(str(curr_violation_count) + '\n')  # Convert the violation count to string
        for i in range(int(rows)):
            for j in range(int(cols)):
                if grid[i][j] == "G0":
                    f.write('0')
                elif grid[i][j] == "G1":
                    f.write('1')
                elif grid[i][j] == "G2":
                    f.write('2')
                elif grid[i][j] == "G3":
                    f.write('3')
                elif grid[i][j] == "G4":
                    f.write('4')  
                elif grid[i][j] == "G": 
                    f.write('X')  # Gray cell
                elif grid[i][j] == -1 :  # Blank cell
                    f.write('.')  
                else:
                    f.write('L')  # Light bulb
            f.write('\n')
            #so each cell is 1 and so total violation can only be the max number of cells 


if __name__ == '__main__':
    main()