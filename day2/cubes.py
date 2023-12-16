
import sys
from typing import Dict, List, Tuple
from enum import IntEnum

class Colors(IntEnum):
    RED = 0
    GREEN = 1
    BLUE = 2


class Game:
    def __init__(self, id: int) -> None:
        self.id = id
        self.rounds = []
    
    def add_round(self, red: int, green: int, blue: int):
        self.rounds.append((red, green, blue))
    
    def to_string(self) -> str:
        retval = f"{self.id}:"
        for round in self.rounds:
            retval += f" ({round[0], round[1], round[2]}),"
        
        retval.rstrip(',')
        return retval

    def get_max_sum(self) -> int:
        max_sum = 0
        for round in self.rounds:
            sum = round[0] + round[1] + round[2]
            if sum > max_sum:
                max_sum = sum
        return max_sum

    def get_max_color(self, color: Colors) -> int:
        max_of_color = 0
        for round in self.rounds:
            count = round[color]
            if count > max_of_color:
                max_of_color = count
        return max_of_color

    def find_min_set(self) -> Tuple:
        colors = []
        for color_ind in range(3):
            colors.append(self.get_max_color(color_ind))
        return tuple(colors)
    
class Bag:
    def __init__(self, red, green, blue) -> None:
        self.red = red
        self.green = green
        self.blue = blue
        self.count = red + green + blue
    
    def is_game_possible(self, game: Game) -> bool:
        # summation check
        if game.get_max_sum() > self.count:
            return False

        if game.get_max_color(Colors.RED) > self.red:
            return False
        if game.get_max_color(Colors.GREEN) > self.green:
            return False
        if game.get_max_color(Colors.BLUE) > self.blue:
            return False

        return True
    

def power_of_cubes(cubes: Tuple) -> int:
    return cubes[Colors.RED] * cubes[Colors.GREEN] * cubes[Colors.BLUE]


def parse_line(l) -> Game:
    parts = l.strip().split(':')

    retval = Game(int(parts[0].split(' ')[1]))

    rounds = parts[1].split(';')

    for round in rounds:
        red = 0
        green = 0
        blue = 0
        cubes = round.split(',')
        for cube_num_str in cubes:
            n = int(cube_num_str.strip().split(' ')[0])
            if 'red' in cube_num_str:
                red = n
            elif 'green' in cube_num_str:
                green = n
            elif 'blue' in cube_num_str:
                blue = n
        retval.add_round(red, green, blue)
    
    return retval


########## main function slug ############
if __name__ == '__main__':

    if len(sys.argv) > 1:
        # read input
        inp = open(sys.argv[1], 'r')
    else:
        inp = open('input.txt', 'r')
    
    # initial condition given by AOC
    bag = Bag(red=12, green=13, blue=14)
    games = []

    sum_of_ids = 0
    part_2_sum = 0

    for line in inp:
        game = parse_line(line)
        print(game.to_string(), end='')
        if bag.is_game_possible(game):
            sum_of_ids += game.id
            print(" ==> POSSIBLE")
        else:
            print()
        part_2_sum += power_of_cubes(game.find_min_set())
        games.append(game)

    print()
    print(f"part 1: Sum of possible game IDs  = {sum_of_ids}")
    print(f"Part 2: sum of powers of min sets = {part_2_sum}")
    # CLOSE INPUT FILE
    inp.close()