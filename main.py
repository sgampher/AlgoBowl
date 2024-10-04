#Authors: Sara Gampher, Kathryn Bruce, Dishita Sharma
#AlgoBowl main.py

def totalViolations(grid):
    total = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if isinstance(grid[row][col], int):  # Checking if it's a light bulb (indicated by int)
                total += lightBulbViolations(grid, (row, col))
            elif grid[row][col] != "G":  # Skip gray cells
                total += greyCellViolations(grid, (row, col))
    return total

# Lightbulb Violation Calculation
def lightBulbViolations(grid, position):
    violationCount = 0
    row, col = position

    # Check the row for other light bulbs
    for c in range(len(grid[row])):
        if c != col and grid[row][c] == "L":  # Found another light bulb in the same row
            violationCount += 1

    # Check the column for other light bulbs
    for r in range(len(grid)):
        if r != row and grid[r][col] == "L":  # Found another light bulb in the same column
            violationCount += 1

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
            if grid[r][c].startswith("G"):  # Only consider cells starting with 'G'
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
            if grid[r][c] == "L":  # Count the light bulbs
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

    return highest_position if highest_position else (0, 0)  # Default to (0, 0) if no position found

def checkCoverage(grid):
    # Check if all blank cells ('.') are illuminated by at least one light bulb
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 0:  # Blank cell
                if not isIlluminated(grid, (row, col)):
                    return False  # Found a blank cell that is not illuminated
    return True  # All blank cells are illuminated

def isIlluminated(grid, position):
    row, col = position
    # Check row and column for light bulbs
    # Check left
    for c in range(col - 1, -1, -1):
        if grid[row][c] == "X":  # Blocked by a gray cell
            break
        if grid[row][c] == "L":  # Found a light bulb
            return True

    # Check right
    for c in range(col + 1, len(grid[row])):
        if grid[row][c] == "X":  # Blocked by a gray cell
            break
        if grid[row][c] == "L":  # Found a light bulb
            return True

    # Check up
    for r in range(row - 1, -1, -1):
        if grid[r][col] == "X":  # Blocked by a gray cell
            break
        if grid[r][col] == "L":  # Found a light bulb
            return True

    # Check down
    for r in range(row + 1, len(grid)):
        if grid[r][col] == "X":  # Blocked by a gray cell
            break
        if grid[r][col] == "L":  # Found a light bulb
            return True

    return False  # No light bulb illuminates the cell

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
                addThis.append(".")  # Keep as a string
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
                addThis.append("X")  # Gray cell
        grid.append(addThis)
    
   
    # Loop through, remove violations, check coverage, repeat
    
    # Count violations
    curr_violation_count = totalViolations(grid)

    for _ in range(rows * cols):
        # Find cell with the highest violation
        highViol = findHighestViolation(grid)
        
        # Make a copy of the grid and place a light bulb in the cell with the highest violation
        potentialNewGrid = [row[:] for row in grid]  # Create a deep copy
        potentialNewGrid[highViol[0]][highViol[1]] = "L"  # Place a light bulb

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
                    f.write('0 ')
                elif grid[i][j] == "G1":
                    f.write('1 ')
                elif grid[i][j] == "G2":
                    f.write('2 ')
                elif grid[i][j] == "G3":
                    f.write('3 ')
                elif grid[i][j] == "G4":
                    f.write('4 ')  
                elif grid[i][j] == "X": 
                    f.write('X ')  # Gray cell
                elif grid[i][j] == ".":  # Blank cell
                    f.write('. ')  
                else:
                    f.write('L ')  # Light bulb
            f.write('\n')


if __name__ == '__main__':
    main()