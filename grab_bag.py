
import sys
from typing import Dict, List, Tuple

########## main function slug ############
if __name__ == '__main__':

    if len(sys.argv) > 1:
        # read input
        inp = open(sys.argv[1], 'r')
    else:
        inp = open('input.txt', 'r')
    

    # CLOSE INPUT FILE
    inp.close()