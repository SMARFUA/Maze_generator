import os.path
import sys
sys.path.append(os.path.join(os.path.dirname("/Users/samkamarfua/Desktop/3B SPRING 2020/"), '..'))

# A class to represent the Maze structure
class CellBlock:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.strlen = (self.col)*self.row;
        self.cell_units = []
        self.walls = []
    
    # Returns Maze structure in the form of strings
    def getBlock(self):
        block = ""
        first_str = []
        rest_str = []
        for i in range(self.col):
            first_str += "_"
            if (i%2 == 0):
                rest_str += "|"
            else:
                rest_str+= "_"
        block = first_str
        for i in range(self.row - 1):
            block += rest_str
        return "".join(block)
     
    # Prints the Maze structure   
    def printBlock(self, block):
        ind1 = 0
        ind2 = self.col
        for i in range(self.col):
            print(block[ind1:ind2])
            ind1 += self.col
            ind2 += self.col

                
    # Returns the list of indices of cells in Maze structure made of strings  
    def getCells(self):
        self.cell_units = []
        block = self.getBlock()
        for i in range(self.strlen):
            if (i>self.col and block[i] == "_"):
                self.cell_units += [i]
        return self.cell_units
    
    # Returns the list of indices of walls in Maze structure made of strings    
    def getWalls(self):
        cells = self.getCells()
        self.walls = cells[0:(self.col//2)*(self.row - 2)]
        for i in range(len(cells) -1):
            if (cells[i+1] - cells[i] ==2):
                self.walls += [cells[i]+1]
        return self.walls
        
    # Returns a list of walls surrounding a given cell 
    def getWall(self, cell):
        walls = []
        if (cell< 2*self.col):
            wall = [cell-1, cell, cell+1, cell-self.col]
        if (cell > 2*self.col):
            wall = [cell, cell -1,cell-self.col, cell + 1]
        return wall
    
    # Returns a list of cells divied by a given wall
    def getCell(self, wall):
        cell = []
        block = self.getBlock()
        if (block[wall] == "|"):
            cell = [wall -1, wall + 1]
        if (block[wall] == "_"):
            cell = [wall, wall + self.col]
        return cell
            
 
# class to represent a cell structure present in maze containing list of 
# surrounding walls and list of connected cells

class Cell:
    def __init__(self, walls, connected_cells):
        self.walls = walls
        self.join_cells  = connected_cells
