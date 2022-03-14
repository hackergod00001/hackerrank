#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'numCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def numCells(grid):
    count = 0
    steps = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            neighbours = 0
            count_temp = 0
            for step in steps:
                if all([len(grid) > i + step[0] >= 0, len(grid[0]) > j + step[1] >= 0 ]):
                    neighbours += 1
                    print(i,j,step,grid[i][j] , grid[i + step[0]][j + step[1]])
                    if grid[i][j] > grid[i + step[0]][j + step[1]]:
                        count_temp += 1
            if neighbours == count_temp:
                count += 1

    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = numCells(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
