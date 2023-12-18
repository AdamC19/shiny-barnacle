
import sys
from typing import Dict, List, Tuple
from enum import IntEnum
import copy

CARD_ORDER = {
    '1': -1,
    '2': 0,
    '3': 1,
    '4': 2,
    '5': 3,
    '6': 4,
    '7': 5,
    '8': 6,
    '9': 7,
    'T': 8,
    'J': 9,
    'Q': 10,
    'K': 11,
    'A': 12
}

class HandType(IntEnum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 5
    FIVE_OF_A_KIND = 6


def get_hand_type(hand: List[str]) -> HandType:
    """Determine hand type from a list of cards"""
    distinct_cards = {}
    for card in hand:
        if card not in distinct_cards:
            distinct_cards[card] = 1
        else:
            distinct_cards[card] += 1

    if len(distinct_cards) == 1:
        return HandType.FIVE_OF_A_KIND

    if len(distinct_cards) == 2:
        # full house or four-of-a-kind
        for c, n in distinct_cards.items():
            if n == 2 or n == 3:
                return HandType.FULL_HOUSE
            elif n == 1 or n == 4:
                return HandType.FOUR_OF_A_KIND
    
    if len(distinct_cards) == 3:
        # three of a kind or two pair
        pairs = 0
        for c, n in distinct_cards.items():
            if n == 3:
                return HandType.THREE_OF_A_KIND
            if n == 2:
                pairs += 1
            if pairs == 2:
                return HandType.TWO_PAIR

    if len(distinct_cards) == 4:
        return HandType.ONE_PAIR

    return HandType.HIGH_CARD



class Hand:
    def __init__(self, hand_str, bid):
        self.hand = list(hand_str)
        self.bid = bid

    @property
    def hand_type(self) -> HandType:
        return get_hand_type(self.hand)

    def to_string(self):
        retval = f"{''.join(self.hand)} ==> {self.hand_type}. BID = {self.bid}"
        return retval


def optimize_hand(hand: Hand) -> Hand:
    """Consider the joker card and optimize the hand"""
    og_hand = hand.hand
    og_type = hand.hand_type

    hand_str = ''.join(og_hand)
    ret_hand = copy.deepcopy(hand)
    if 'J' in hand_str:
        for key in CARD_ORDER.keys():
            new_str = hand_str.replace('J', key)
            test_hand = Hand(new_str, hand.bid)
            if test_hand.hand_type > ret_hand.hand_type:
                ret_hand = copy.deepcopy(test_hand)

    return ret_hand
    

def compare_hands(hand1_og: Hand, hand2_og: Hand, joker_flag=False) -> int:
    """Compare 2 hands
    return -1 if hand2 wins compared to hand1 (hand2 goes first)
    return 1 if hand1 wins compared to hand2 (hand1 goes first)
    return 0 if both are equal
    """
    

    if joker_flag:
        hand1 = optimize_hand(hand1_og)
        hand2 = optimize_hand(hand2_og)
    else:
        hand1 = copy.deepcopy(hand1_og)
        hand2 = copy.deepcopy(hand2_og)
    
    if hand1.hand_type > hand2.hand_type:
        return 1
    elif hand2.hand_type > hand1.hand_type:
        return -1
    else:
        # same type, so find which card is highest starting from the start
        if joker_flag:
            hand1_str = ''.join(hand1_og.hand).replace('J', '1')
            hand2_str = ''.join(hand2_og.hand).replace('J', '1')
            hand1.hand = list(hand1_str)
            hand2.hand = list(hand2_str)

        i = 0
        
        while i < len(hand1.hand) and hand1.hand[i] == hand2.hand[i]:
            i += 1
        
        if i == len(hand1.hand):
            # hands are identical
            return 0
            
        if CARD_ORDER[hand1.hand[i]] > CARD_ORDER[hand2.hand[i]]:
            return 1
        elif CARD_ORDER[hand2.hand[i]] > CARD_ORDER[hand1.hand[i]]:
            return -1


# def partition(arr: List[Hand], low: int, high: int):

def merge_sort(arr: List[Hand], joker_flag=False):
    # print("\r\nSorting array:")
    # for hand in arr:
    #     print(hand.to_string())

    if len(arr) > 1:
        start = 0
        end = len(arr)
        end_a = start + int(len(arr) / 2)
        arr_left = copy.deepcopy(arr[start:end_a])
        arr_right = copy.deepcopy(arr[end_a:end])
        merge_sort(arr_left, joker_flag=joker_flag) # left
        merge_sort(arr_right, joker_flag=joker_flag) # right
        
        # now merge the two sub-arrays

        i = 0
        j = 0
        ii = 0
        while i < len(arr_left) and j < len(arr_right):
            cmp = compare_hands(arr_left[i], arr_right[j], joker_flag=joker_flag)
            if cmp >= 0:
                # first hand goes before second, or 0 in which case it doesn't matter
                arr[ii] = arr_left[i]
                i += 1
            else:
                # second hand goes before first
                arr[ii] = arr_right[j]
                j += 1
            ii += 1

        while i < len(arr_left):
            arr[ii] = arr_left[i]
            ii += 1
            i += 1
        
        while j < len(arr_right):
            arr[ii] = arr_right[j]
            ii += 1
            j += 1


def quick_sort(sub_arr: List[Hand]):
    start = 0
    end = len(sub_arr) - 1

    if len(sub_arr) <= 1:
        return
    else: # len(sub_arr) == 2:
        cmp = compare_hands(sub_arr[start], sub_arr[end])
        if cmp < 0:
            temp = copy.deepcopy(sub_arr[start])
            sub_arr[start] = copy.deepcopy(sub_arr[end])
            sub_arr[end] = temp
        elif cmp > 0:
            # order is already correct
            pass
        end_a = start + int(len(sub_arr) / 2)
        start_b = end_a + 1
        end_b = end
        quick_sort(sub_arr[start:end_a])
        quick_sort(sub_arr[start_b:end_b])


########## main function slug ############
if __name__ == '__main__':

    if len(sys.argv) > 1:
        # read input
        inp = open(sys.argv[1], 'r')
    else:
        inp = open('input.txt', 'r')
    

    hands = []
    for line_raw in inp:
        line = line_raw.strip()
        parts = line.split(' ')
        hands.append(Hand(parts[0], int(parts[1])))

    # CLOSE INPUT FILE
    inp.close()

    for hand in hands:
        print(hand.to_string())

    print()
    print("SORTING...")
    print()
    # sort hands
    hands_pt1 = copy.deepcopy(hands)
    hands_pt2 = copy.deepcopy(hands)
    merge_sort(hands_pt1)
    merge_sort(hands_pt2, joker_flag=True)


    winnings = 0
    winnings_pt2 = 0
    for i in range(len(hands_pt1)):
        rank = len(hands_pt1) - i
        hand = hands_pt1[i]
        hand2 = hands_pt2[i]
        win = (rank) * hand.bid
        win2 = rank * hand2.bid
        # print(f"{hand.to_string()} of rank {rank} wins {win}")
        winnings += win
        winnings_pt2 += win2
    
    print(f"Part 1 total winnings = {winnings}")
    print(f"Part 2 total winnings = {winnings_pt2}")


    