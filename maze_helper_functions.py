
from maze_structure.py import CellBlock
from maze_structure.py import Cell

# Returns a cell dictionary of Cell structures
def CellDict(cellRow, cellCol):
    block = CellBlock(cellRow, cellCol)
    cells = block.getCells()
    dict = {}
    for i in range(len(cells)):
        dict[cells[i]] = Cell(block.getWall(cells[i]), [cells[i]])
    return dict
 
# Updates the neighbour of the neighbour cells   
def add_nested_neighbours(cell1,cell2, neighbours, dict):
        for i in range(len(neighbours)):
            nested_neighbours = dict[neighbours[i]].join_cells
            nested_neighbours += [cell1, cell2]
            nested_neighbours = list(set(nested_neighbours))
           
            
# Returns Union of two sets               
def union(set1, set2):
    new_set = set1
    i = 0
    for i in range(len(set2)):
        if set2[i] not in new_set:
            new_set.append(set2[i])
    return new_set

# Returns true if an entry is present in both sets    
def duplicate_present(set1, set2):
    for i in range(len(set1)):
        if set1[i] in set2:
            return True
    return False

# Returns a random new list from entries of lst
def random_sequence(lst):
    index_list = random.sample(range(len(lst)), len(lst))
    new_list = []
    for i in range(len(index_list)):
        new_list += [list[index_list[i]]]
    return new_list
