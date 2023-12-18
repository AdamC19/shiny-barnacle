
import sys
from typing import Dict, List, Tuple


class Range:
    def __init__(self, src_start, dst_start, rng):
        self.src_start = src_start
        self.dst_start = dst_start
        self.src_stop = src_start + rng # non-inclusive

    def is_num_in_range(self, num) -> bool:
        return num >= self.src_start and num < self.src_stop

    def get_dest(self, src) -> int:
        diffy = src - self.src_start
        return self.dst_start + diffy

class Mapping:
    def __init__(self, src_str, dest_str):
        self.src = src_str
        self.dest = dest_str

        self.map = {}
        self.ranges = []

    def add_range(self, src_start, dest_start, rng):
       
        # flesh out map with emptiness up to src_start + rng
        # we will next overwrite the src_start to src_end
        # while len(self.map) < src_start + rng:
        #     src = len(self.map)
        #     self.map.append((src, src)) # default to mapping to the same number
        self.ranges.append(Range(src_start, dest_start, rng))
        
        # dest = dest_start
        # for src in range(src_start, src_start + rng):
        #     self.map[src] = dest
        #     dest += 1

    def get_dest(self, src):
        for rng in self.ranges:
            if rng.is_num_in_range(src):
                return rng.get_dest(src)

        return src # if we made it this far, there's no range that fits

    def to_string(self):
        retval = f"{self.src}\t{self.dest}\n"
        # for src, dst in self.map.items():
        #     retval += f"{src}\t{dst}\n"
        return retval

########## main function slug ############
if __name__ == '__main__':

    if len(sys.argv) > 1:
        # read input
        inp = open(sys.argv[1], 'r')
    else:
        inp = open('input.txt', 'r')
    
    src = ''
    dst = ''
    mappings = []
    seeds = []
    for line_raw in inp:
        line = line_raw.strip()
        print(line)
        if len(line) > 0:
            if line.startswith('seeds'):
                numstr = line.split(':')[1].strip()
                seeds = [int(n) for n in numstr.split()]
            elif line.endswith(':'):
                parts = line.split(' ')
                src_to_dest = parts[0].split('-to-')
                src = src_to_dest[0]
                dst = src_to_dest[1]
                mappings.append(Mapping(src, dst))
            else:
                nums = [int(n_str) for n_str in line.split()]
                dst_start = nums[0]
                src_start = nums[1]
                rng = nums[2]
                mappings[-1].add_range(src_start, dst_start, rng)

    # CLOSE INPUT FILE
    inp.close()

    print(f"SEEDS = {seeds}")

    # PART 1
    loc_nums = []
    for seed in seeds:
        key = seed
        for mapping in mappings:
            print(f"{mapping.src}({key}) --> {mapping.dest}(?)")
            key = mapping.get_dest(key)
            print(f"{mapping.dest} = {key}")

        loc_nums.append(key)
    
    print(f"{loc_nums}")

    print(f"Part 1: Lowest location number = {min(loc_nums)}")
    
    lowest_loc_nums = []
    for i in range(0, len(seeds), 2):
        start = seeds[i]
        end = seeds[i] + seeds[i+1]
        lowest = sys.maxsize
        for seed in range(start, end):
            key = seed
            for mapping in mappings:
                # print(f"{mapping.src}({key}) --> {mapping.dest}(?)")
                key = mapping.get_dest(key)
                # print(f"{mapping.dest} = {key}")
            if key < lowest:
                lowest = key
        lowest_loc_nums.append(lowest)

    # PART 2
    print(f"Part 2: Lowest location number = {min(lowest_loc_nums)}")