#Authors: Sara Gampher, Kathryn Bruce, Dishita Sharma
#AlgoBowl main.py

def main():
    #initialize variables
    grid = []
    
    #read input
    #read in first line of input 
    firstline = input().split(" ")
    rows = firstline[0]
    cols = firstline[1]
    #parse into grid
    
    #read in rest of given input and store in grid
    for i in range(int(rows)):
        nextline = input().split(" ")
        grid.append(nextline)
    #count violations
    #loop through, remove violations, check coverage, repeat
    #parse into output






    #call seperateVioldation on the grid to get current violation count
    curr_violation_count = separateViolation(grid)

    for i in range(int(rows * cols)):
        #find highest violation - returns a tuple storing row and col of highest
        highViol = findHighestViolation(grid)
        #make a copy of the grid and assign the highest violation cell with a -1 
        potentialNewGrid = grid
        potentialNewGrid[highViol[0]][highViol[1]] = -1

        if(checkCoverage(potentialNewGrid)):
            new_violation_count = separateViolation(potentialNewGrid)
            if new_violation_count < curr_violation_count:
                grid = potentialNewGrid
                curr_violation_count = new_violation_count


    with open('output.txt', 'w') as f:
        f.write(curr_violation_count + '\n')
        for i in range(int(rows)):
            for j in range(int(cols)):
                if(grid[i][j] == -1):
                    f.write('. ')#MIGHT NEED TO WATCH EXTRA SPACE AT THE END FOR OTHER TEAMS VERIFICATION    
                elif(grid[i][j] == "G1"): #MIGHT NEED TO WATCH FOR STORING INTS AND STRINGS IN GRID
                    f.write('1 ') 
                elif(grid[i][j] == "G2"): 
                    f.write('2 ')
                elif(grid[i][j] == "G3"): 
                    f.write('3 ')
                elif(grid[i][j] == "G4"): 
                    f.write('4 ')  
                elif(grid[i][j] == "G0"): 
                    f.write('0 ') 
                elif(grid[i][j] == "G"): 
                    f.write('X ')   
                else:
                    f.write('L ')   
            f.write('\n')





if __name__ == '__main__':
    main()