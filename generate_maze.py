from maze_structure.py import CellBlock
from maze_structure.py import Cell
from maze_helper_functions.py import*

# generates the final random maze from a given maze dimensions
def generate_maze(row, col):
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
            cellblock = "".join(cellblock)
            block.printBlock(cellblock)
        
        
    


   