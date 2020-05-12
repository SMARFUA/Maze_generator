import curses
import random
import time
import termcolor
import os
os.system('color')


class CellBlock:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.strlen = (self.col)*self.row;
        self.cell_units = []
        self.walls = []
        
    def getBlock(self):
        block = ""
        first_str = []
        rest_str = []
        for i in range(self.col):
            first_str += "_"
            if (i%2==0):
                rest_str+= "|"
            else:
                rest_str+= "_"
        block = first_str
        for i in range(self.row - 1):
            block+= rest_str
        return "".join(block)
        
    def printBlock(self, block):
        ind1 = 0
        ind2 = self.col
        for i in range(self.col):
            print(block[ind1:ind2])
            ind1 += self.col
            ind2 += self.col

                
        
    def getCells(self):
        self.cell_units = []
        block = self.getBlock()
        for i in range(self.strlen):
            if (i>self.col and block[i] == "_"):
                self.cell_units += [i]
        return self.cell_units
        
    def getWalls(self):
        cells = self.getCells()
        self.walls = cells[0:(self.col//2)*(self.row - 2)]
        for i in range(len(cells) -1):
            if (cells[i+1] - cells[i] ==2):
                self.walls += [cells[i]+1]
        return self.walls
        
        
    def getWall(self, cell):
        walls = []
        if (cell< 2*self.col):
            wall = [cell-1, cell, cell+1, cell-self.col]
        if (cell > 2*self.col):
            wall = [cell, cell -1,cell-self.col, cell + 1]
        return wall
    
    def getCell(self, wall):
        cell = []
        block = self.getBlock()
        if (block[wall] == "|"):
            cell = [wall -1, wall + 1]
        if (block[wall] == "_"):
            cell = [wall, wall + self.col]
        return cell
            
            
class Cell:
    def __init__(self, walls, connected_cells):
        self.walls = walls
        self.join_cells  = connected_cells

        
    
def CellDict(cellRow, cellCol):
    block = CellBlock(cellRow, cellCol)
    cells = block.getCells()
    dict = {}
    for i in range(len(cells)):
        dict[cells[i]] = Cell(block.getWall(cells[i]), [cells[i]])
    return dict
    
def add_nested_neighbours(cell1,cell2, neighbours, dict):
        for i in range(len(neighbours)):
            nested_neighbours = dict[neighbours[i]].join_cells
            nested_neighbours += [cell1, cell2]
            nested_neighbours = list(set(nested_neighbours))
           
            
                
def union(set1, set2):
    new_set = set1
    i = 0
    for i in range(len(set2)):
        if set2[i] not in new_set:
            new_set.append(set2[i])
    return new_set
    
def duplicate_present(set1, set2):
    for i in range(len(set1)):
        if set1[i] in set2:
            return True
    return False
    
def random_sequence(list):
    index_list = random.sample(range(len(list)), len(list))
    new_list = []
    for i in range(len(index_list)):
        new_list += [list[index_list[i]]]
    return new_list
    


def game(row, col):
    block = CellBlock(row, col)
    cellblock = block.getBlock()
    walls = random_sequence(block.getWalls())
    dict = CellDict(row, col)
    block.printBlock(block.getBlock())
    for i in range(len(walls)):
        neighbours = block.getCell(walls[i])
        first_join_cells = dict[neighbours[0]].join_cells
        second_join_cells = dict[neighbours[1]].join_cells
        if (duplicate_present(first_join_cells, second_join_cells) == False):
            union_neighbours = union(first_join_cells, second_join_cells)
            dict[neighbours[0]].join_cells = union_neighbours
            dict[neighbours[1]].join_cells = union_neighbours
            add_nested_neighbours(neighbours[0],neighbours[1],union_neighbours,
            dict)
            cellblock = list(cellblock)
            cellblock[walls[i]] = " "
            cellblock[walls[i+1]] = cellblock.replace(cellblock[walls[i+1]],termcolor.colored(cellblock[walls[i+1]], 'red'))
            cellblock = "".join(cellblock)
            block.printBlock(cellblock)
        
        
    


   