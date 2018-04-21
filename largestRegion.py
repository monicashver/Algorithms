#!/bin/python3

import sys

  
def findRegionSize(matrix, i, j):
    # counted => set to 0
    # matrix[i][j] = 0
    # count = 1
    #print("i", i,"j",  j)
    if(j >= len(matrix[0]) or i >= len(matrix) or i < 0 or j < 0):
        return 0
    elif(matrix[i][j] == 0):
        return 0
    else:
        matrix[i][j] = 0
        count = 1
        
        count += findRegionSize(matrix, i + 1, j) + findRegionSize(matrix, i + 1, j + 1) + findRegionSize(matrix, i, j + 1) + findRegionSize(matrix, i - 1, j) + findRegionSize(matrix, i, j - 1) + findRegionSize(matrix, i - 1, j - 1) + findRegionSize(matrix, i - 1, j + 1) + findRegionSize(matrix, i + 1, j - 1)
    return count
    
    
    
    
    
def connectedCell(matrix):
    # Complete this function
    #print(matrix)
    max_region = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if(matrix[i][j] == 1):
                reg_size = findRegionSize(matrix, i, j)
                #print(reg_size)
                if(reg_size > max_region):
                    max_region = reg_size
                    
    return max_region
if __name__ == "__main__":
    n = int(input().strip())
    m = int(input().strip())
    matrix = []
    for matrix_i in range(n):
        matrix_t = [int(matrix_temp) for matrix_temp in input().strip().split(' ')]
        matrix.append(matrix_t)
    result = connectedCell(matrix)
    print(result)