def main():
    grid = [[2,4,5,6,0],[2,4,7,8,1]]
    newGrid = [row[:] for row in grid]
    newGrid[0][2] = 50
    print(grid)
    print(newGrid)


if __name__ == '__main__':
    main()