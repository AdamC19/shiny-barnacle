
import sys
from typing import Dict, List, Tuple
import copy

# (y, x)
DIR_TYPES = {
    'N': [-1, 0],
    'E': [0, 1],
    'S': [1, 0],
    'W': [0, -1]
}


PIPE_TYPES = {
    '|': ['N', 'S'],
    '-': ['E', 'W'],
    'L': ['N', 'E'],
    'J': ['N', 'W'],
    '7': ['S', 'W'],
    'F': ['E', 'S']
}


def get_dir_pair(obj: str) -> str:
    if obj == 'N':
        return 'S'
    elif obj == 'S':
        return 'N'
    elif obj == 'E':
        return 'W'
    elif obj == 'W':
        return 'E'
    return ''


def take_step_in_dir(coord: List[int], direc: str) -> List[int]:
    if direc in DIR_TYPES:
        delta = DIR_TYPES[direc]
        new_coord = [coord[0], coord[1]]
        new_coord[0] += delta[0]
        new_coord[1] += delta[1]
        return new_coord
    return [0, 0]


def get_obj_in_dir(pipes: List[List[str]], coord: List[int], direc: str) -> str:
    if direc in DIR_TYPES:
        delta = DIR_TYPES[direc]
        new_coord = [coord[0], coord[1]]
        new_coord[0] += delta[0]
        new_coord[1] += delta[1]
        return pipes[new_coord[0]][new_coord[1]]
    else:
        print(f"Direction {direc} not recognized.")
        return '.'

########## main function slug ############
if __name__ == '__main__':

    if len(sys.argv) > 1:
        # read input
        inp = open(sys.argv[1], 'r')
    else:
        inp = open('input.txt', 'r')
    

    pipes = []

    for line in inp:
        pipes.append(list(line.strip()))

    # CLOSE INPUT FILE
    inp.close()

    start = None
    found = False
    for y in range(len(pipes)):
        for x in range(len(pipes[y])):
            if pipes[y][x] == 'S':
                start = [y, x]
                found = True
                break
        if found:
            break
    
    print(f"Starting index is (y, x) = ({start[0]}, {start[1]})")

    coord = [start[0], start[1]]
    last_move = ''

    back_at_start = False
    steps = 0
    pipes_pt2 = copy.deepcopy(pipes)

    while not back_at_start:

        seg = pipes[coord[0]][coord[1]] # current segment that we're on

        pipes_pt2[coord[0]][coord[1]] = pipes_pt2[coord[0]][coord[1]] + ' '
        if seg == 'S':
            # look around and see which cardinal dirs we can go
            for direc in DIR_TYPES:
                n_obj = get_obj_in_dir(pipes, coord, direc) # gets whatever type of pipe segment is in this direction

                if n_obj == 'S':
                    print(f"Found the end in {steps + 1}!")
                    break
                if get_dir_pair(direc) in PIPE_TYPES[n_obj]:
                    # checks if the pipe seg in this dir faces our segment
                    # if so, progress in this direction
                    last_move = direc
                    coord = take_step_in_dir(coord, direc)
        else:
            moves = PIPE_TYPES[seg]
            if get_dir_pair(moves[0]) == last_move:
                # we'll take moves[1]
                coord = take_step_in_dir(coord, moves[1])
                last_move = moves[1]
            else:
                # we'll take moves[0]
                coord = take_step_in_dir(coord, moves[0])
                last_move = moves[0]

        steps += 1

        back_at_start = (pipes[coord[0]][coord[1]] == 'S')
    
    print(f"The pipe loop is {steps} steps around.")
    print(f"PART 1 solution: {steps / 2} is the farthest you can be from the start.")

    # part 2
    # replace S with actual pipe symbol
    actual_opts = []
    for direc in DIR_TYPES:
        other = get_obj_in_dir(pipes, start, direc)
        if get_dir_pair(direc) in PIPE_TYPES[other]:
            actual_opts.append(direc)
    
    for seg, direcs in PIPE_TYPES.items():
        if actual_opts[0] in direcs and actual_opts[1] in direcs:
            pipes_pt2[start[0]][start[1]] = seg + ' '

    coord = [0, 0]
    seg = pipes_pt2[coord[0]][coord[1]]
    while len(seg) > 1:
        coord = [coord[0], coord[1]]
    
    print(f"Starting with {coord} as our starting tile")
    outside = True
    tiles_outside = 0

    y = coord[0]
    x = coord[1]
    while y < len(pipes_pt2) and x < len(pipes_pt2[y]):
        row = pipes_pt2[y]
        tile = row[x]
        if len(tile) > 1:
            # this is part of the loop
            if '-' not in tile:
                # toggle whether we're inside or outside loop
                outside = not outside
            # else, don't change
        
        if outside and len(tile) == 1:
            tiles_outside += 1
        
        # perform rastering
        if y % 2 == 0:
            x += 1
            if x == len(pipes_pt2):
                x = len(pipes_pt2) - 1
                y += 1
                if y < len(pipes_pt2):
                    # evaluate whether to toggle outside flag as we move vertically
                    next_tile = pipes_pt2[y][x]
                    if len(next_tile) > 1:
                        if '|' not in next_tile:
                            outside = not outside
                    # else:
                    #     outside = not outside
                
        else:
            x -= 1
            if x == -1:
                x = 0
                y += 1
                if y < len(pipes_pt2):
                    # evaluate whether to toggle outside flag as we move vertically
                    next_tile = pipes_pt2[y][x]
                    if len(next_tile) > 1:
                        if '|' not in next_tile:
                            outside = not outside
                    # else:
                    #     outside = not outside
    
    total_tiles = len(pipes_pt2) * len(pipes_pt2[0])
    inside_tiles = total_tiles - (steps + tiles_outside)
    print(f"PART 2: tiles inside the loop: {inside_tiles}")