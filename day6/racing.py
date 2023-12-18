
import sys
from typing import Dict, List, Tuple
import math

########## main function slug ############
if __name__ == '__main__':

    if len(sys.argv) > 1:
        # read input
        inp = open(sys.argv[1], 'r')
    else:
        inp = open('input.txt', 'r')
    
    line_ind = 0
    times = []
    dists = []
    for line_raw in inp:
        parts = line_raw.split(':')
        if line_ind == 0:
            times = [int(n) for n in parts[1].strip().split()]
            big_time = int(''.join(parts[1].strip().split()))
            times.append(big_time)
        else:
            dists = [int(n) for n in parts[1].strip().split()]
            big_dist = int(''.join(parts[1].strip().split()))
            dists.append(big_dist)

        line_ind += 1
    
    # CLOSE INPUT FILE
    inp.close()

    def get_hold_bounds(t, d_win):
        """hold is hold for time, t is race duration"""
        # 0 = hold**2 - t*hold + d_win
        ret1 = (t + math.sqrt(t**2 - 4*d_win))/(2)
        ret2 = (t - math.sqrt(t**2 - 4*d_win))/(2)
        return (ret1, ret2)

    def get_distance(t, hold):
        return hold * (t - hold)

    ways_to_win = []
    part_1_product = 1
    part_2_result = 0
    for i in range(len(times)):
        race_dur = times[i]
        dist_to_beat = dists[i]
        win_bounds = get_hold_bounds(race_dur, dist_to_beat)
        print(f"Winning hold time bounds raw = ({win_bounds[0]:.3f}.., {win_bounds[1]:.3f}..)")
        bound_a = win_bounds[0]
        bound_b = win_bounds[1]
        if bound_a < bound_b:
            win_bounds = (bound_a, bound_b)
        else:
            win_bounds = (bound_b, bound_a)
        
        win_bounds = (int(win_bounds[0] + 1.0), round(win_bounds[1] - 0.5))

        if get_distance(race_dur, win_bounds[0]) <= dist_to_beat:
            win_bounds = (win_bounds[0] + 1, win_bounds[1])
            
        if get_distance(race_dur, win_bounds[1]) <= dist_to_beat:
            win_bounds = (win_bounds[0], win_bounds[1] - 1)

        ways_to_win = win_bounds[1] - win_bounds[0] + 1
        print(f"Winning hold time bounds = {win_bounds}. ({ways_to_win} ways to win)")

        if i < len(times) - 1:
            part_1_product = part_1_product * ways_to_win
        else:
            part_2_result = ways_to_win
        
    print(f"Part 1 product = {part_1_product}")
    print(f"Part 2 result  = {part_2_result}")