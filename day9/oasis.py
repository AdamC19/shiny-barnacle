
import sys
from typing import Dict, List, Tuple
import copy

def is_seq_all_zeros(seq: List[int]) -> bool:
    if len(seq) < 1:
        return False
    
    for i in seq:
        if i != 0:
            return False
    return True

def print_seqs(seqs: List[List[int]]):
    pad_spaces = 0
    for seq in seqs:
        print(pad_spaces*' ', end='')
        for num in seq:
            print(f"{num} ", end='')
        print('')
        pad_spaces += 1

########## main function slug ############
if __name__ == '__main__':

    if len(sys.argv) > 1:
        # read input
        inp = open(sys.argv[1], 'r')
    else:
        inp = open('input.txt', 'r')
    

    seqs = []

    for line in inp:
        seqs.append([int(numstr) for numstr in line.split()])

    # CLOSE INPUT FILE
    inp.close()

    predictions = []
    pt2_predictions = []
    for seq in seqs:
        # print(seq)
        new_seqs = [seq]
        new_seq = []
        start_seq = seq
        while not is_seq_all_zeros(new_seq):
            new_seq = []
            for i in range(1, len(start_seq)):
                new_seq.append(start_seq[i] - start_seq[i-1])
            new_seqs.append(new_seq)
            start_seq = new_seq

        # print_seqs(new_seqs)
        # print('')
        
        end_ind = len(new_seqs) - 1
        # new_seqs_pt2 = copy.deepcopy(new_seqs)

        # part 1
        new_seqs[end_ind].append(0)
        for i in range(end_ind - 1, -1, -1):
            sq = new_seqs[i]
            extrap = sq[-1] + new_seqs[i + 1][-1]
            new_seqs[i].append(extrap)
        
        predictions.append(new_seqs[0][-1])

        # part 2
        new_seqs[end_ind] = [0] + new_seqs[end_ind]
        for i in range(end_ind - 1, -1, -1):
            sq = new_seqs[i]
            extrap = sq[0] - new_seqs[i + 1][0]
            new_seqs[i] = [extrap] + new_seqs[i]
        
        pt2_predictions.append(new_seqs[0][0])


    part1_sum = sum(predictions)
    print(f"PART 1: {part1_sum}")
    part2_sum = sum(pt2_predictions)
    print(f"PART 2: {part2_sum}")
