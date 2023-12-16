
import sys
from typing import Dict, List, Tuple


class Scratchcard:
    def __init__(self, id, this_card, next_card=None):
        self.id = id
        self.card = (this_card[0], this_card[1])
        self.next_card = next_card
        self.instances = 1

    def get_winning_nums(self):
        """Get count of winning numbers we have"""
        win_num_count = 0
        for win_num in self.card[0]:
            if win_num in self.card[1]:
                win_num_count += 1
        return win_num_count

    def to_string(self):
        return f"Card #{self.id} has {self.instances}-many copies"

########## main function slug ############
if __name__ == '__main__':

    if len(sys.argv) > 1:
        # read input
        inp = open(sys.argv[1], 'r')
    else:
        inp = open('input.txt', 'r')
    
    cards = []
    cards_ll_head = Scratchcard(0, ([], []))
    cards_ll = cards_ll_head
    card_id = 0
    for line in inp:
        card_id += 1
        parts = line.strip().split('|')
        nums_we_have = [int(n_str) for n_str in parts[1].strip().split()]
        winning_nums = [int(n_str) for n_str in parts[0].split(':')[1].strip().split()]
        
        if cards_ll.id == 0:
            cards_ll.id = card_id
            cards_ll.card = (winning_nums, nums_we_have)
        else:
            new_card = Scratchcard(card_id, (winning_nums, nums_we_have))
            cards_ll.next_card = new_card
            cards_ll = cards_ll.next_card

        cards.append((winning_nums, nums_we_have))

    # CLOSE INPUT FILE
    inp.close()

    part_1_sum = 0
    card_num = 0
    for card in cards:
        card_num += 1
        win_num_count = 0
        for win_num in card[0]:
            if win_num in card[1]:
                win_num_count += 1
        points = 0
        if win_num_count > 0:
            points = (1 << (win_num_count - 1))
            print(f"Card #{card_num} is worth {points} pts")

        part_1_sum += points
    
    print(f"Part 1 sum = {part_1_sum}")

    
    # PART 2 Generate copies
    card = cards_ll_head
    while card is not None:
        win_count = card.get_winning_nums()

        # foreach instance (copy) of a card, make more copies of other cards
        for i in range(card.instances):
            next_card = card.next_card
            ii = win_count
            while ii > 0:
                next_card.instances += 1
                ii -= 1
                next_card = next_card.next_card

        card = card.next_card

    # PART 2 count up all copies
    card = cards_ll_head
    copies = 0
    while card is not None:
        print(card.to_string())
        copies += card.instances
        card = card.next_card

    print(f"Part 2 number of scratch cards = {copies}")