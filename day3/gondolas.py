
import sys
from typing import Dict, List, Tuple

########## main function slug ############
if __name__ == '__main__':

    if len(sys.argv) > 1:
        # read input
        inp = open(sys.argv[1], 'r')
    else:
        inp = open('input.txt', 'r')

    
    lines = []
    for line_raw in inp:
        lines.append(line_raw.strip())
    
    # CLOSE INPUT FILE
    inp.close()

    row = 0
    part_nums = []
    gear_ratios = []
    for line in lines:
        print(f"Processing line {row}: {line}")
        for col in range(len(line)):
            adj_nums = []
            if not line[col].isdecimal() and line[col] != '.':
                # this is a symbol, get all adjacent numbers
                # print(f"Symbol found at ({col}, {row})")
                # check NORTH
                if row - 1 >= 0:
                    north_line = lines[row - 1]

                    # check if character right above is a number
                    if north_line[col].isdecimal():
                        start_num = col
                        # find the start of this number by walking West
                        while north_line[start_num - 1].isdecimal():
                            start_num -= 1

                        end_num = col + 1
                        # find the end of this number by walking East
                        while north_line[end_num].isdecimal():
                            end_num += 1
                        
                        num_str = north_line[start_num:end_num]
                        if len(num_str) > 0:
                            adj_nums.append(int(num_str))
                            # print(f"Appending number {num_str}")
                            part_nums.append(int(num_str))
                            north_line = north_line[:start_num] + '.'*(end_num - start_num) + north_line[end_num:]

                    else:
                        # start with NW quadrant and walk West
                        west_col = col - 1
                        nw_str = ''
                        while west_col >= 0 and north_line[west_col].isdecimal():
                            nw_str = north_line[west_col] + nw_str
                            north_line = north_line[:west_col] + '.' + north_line[west_col + 1:]
                            west_col -= 1

                        if len(nw_str) > 0:
                            adj_nums.append(int(nw_str))
                            # print(f"Appending number {nw_str}")
                            part_nums.append(int(nw_str))

                        # now go to NE quadrant and walk East
                        east_col = col + 1
                        ne_str = ''
                        while east_col < len(north_line) and north_line[east_col].isdecimal():
                            ne_str = ne_str + north_line[east_col]
                            north_line = north_line[:east_col] + '.' + north_line[east_col + 1:]
                            east_col += 1
                        
                        if len(ne_str) > 0:
                            adj_nums.append(int(ne_str))
                            # print(f"Appending number {ne_str}")
                            part_nums.append(int(ne_str))

                    lines[row - 1] = north_line # do this to ensure we track what numbers we've counted

                # check WEST
                west_ind = col - 1
                west_str = ''
                while west_ind >= 0 and line[west_ind].isdecimal():
                    west_str = line[west_ind] + west_str
                    line = line[:west_ind] + '.' + line[west_ind + 1:]
                    west_ind -= 1

                if len(west_str) > 0:
                    adj_nums.append(int(west_str))
                    # print(f"Appending number {west_str}")
                    part_nums.append(int(west_str))

                # check EAST
                east_ind = col + 1
                east_str = ''
                while east_ind < len(line) and line[east_ind].isdecimal():
                    east_str = east_str + line[east_ind]
                    line = line[:east_ind] + '.' + line[east_ind + 1:]
                    east_ind += 1

                if len(east_str) > 0:
                    adj_nums.append(int(east_str))
                    # print(f"Appending number {east_str}")
                    part_nums.append(int(east_str))

                # check SOUTH
                if row + 1 < len(lines):
                    south_line = lines[row + 1]

                    # check if character right below is a number
                    if south_line[col].isdecimal():
                        start_num = col
                        # find the start of this number by walking West
                        while south_line[start_num - 1].isdecimal():
                            start_num -= 1

                        end_num = col + 1
                        # find the end of this number by walking East
                        while south_line[end_num].isdecimal():
                            end_num += 1
                        
                        num_str = south_line[start_num:end_num]
                        if len(num_str) > 0:
                            adj_nums.append(int(num_str))
                            # print(f"Appending number {num_str}")
                            part_nums.append(int(num_str))
                            south_line = south_line[:start_num] + '.'*(end_num - start_num) + south_line[end_num:]

                    else:
                        # start with SW quadrant and walk West
                        west_col = col - 1
                        sw_str = ''
                        while west_col >= 0 and south_line[west_col].isdecimal():
                            sw_str = south_line[west_col] + sw_str
                            south_line = south_line[:west_col] + '.' + south_line[west_col + 1:]
                            west_col -= 1

                        if len(sw_str) > 0:
                            adj_nums.append(int(sw_str))
                            # print(f"Appending number {sw_str}")
                            part_nums.append(int(sw_str))

                        # now go to NE quadrant and walk East
                        east_col = col + 1
                        se_str = ''
                        while east_col < len(south_line) and south_line[east_col].isdecimal():
                            se_str = se_str + south_line[east_col]
                            south_line = south_line[:east_col] + '.' + south_line[east_col + 1:]
                            east_col += 1
                        
                        if len(se_str) > 0:
                            adj_nums.append(int(se_str))
                            # print(f"Appending number {se_str}")
                            part_nums.append(int(se_str))

                    lines[row + 1] = south_line # do this to ensure we track what numbers we've counted

                if line[col] == '*' and len(adj_nums) == 2:
                    ratio = adj_nums[0] * adj_nums[1]
                    print(f"Adding a new gear ratio: {adj_nums[0]} x {adj_nums[1]} = {ratio}")
                    gear_ratios.append(ratio)
        # finally, increment row
        row += 1
    
    part_1_sum = sum(part_nums)
    print(f"Part 1: sum of part numbers = {part_1_sum}")
    part_2_sum = sum(gear_ratios)
    print(f"Part 2: sum of gear ratios = {part_2_sum}")