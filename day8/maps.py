
import sys
from typing import Dict, List, Tuple
import gmpy2
import math

class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.lut = {'L': left, 'R': right}


########## main function slug ############
if __name__ == '__main__':

    if len(sys.argv) > 1:
        # read input
        inp = open(sys.argv[1], 'r')
    else:
        inp = open('input.txt', 'r')
    
    if len(sys.argv) > 2:
        part = int(sys.argv[2])

    line_num = 0

    dirs = None
    dirs_pt2 = []
    nodes = {}
    nodes_pt2 = {}
    for line_raw in inp:
        line = line_raw.strip()
        if line_num == 0:
            dirs = list(line)
            dirs_pt2 = [0 if c == 'L' else 1 for c in dirs]
        elif len(line) > 0:
            parts = line.split(' = ')
            lr_strs = [s.strip() for s in parts[1].strip('()').split(',')]
            node_name = parts[0].strip()
            nodes[node_name] = {'L': lr_strs[0], 'R': lr_strs[1]}
            nodes_pt2[node_name] = (lr_strs[0], lr_strs[1])
            # if line_num == 2:
            #     start_node = node_name

        line_num += 1

    # CLOSE INPUT FILE
    inp.close()

    # for name in nodes:
    #     print(f"{name} = {nodes[name]}")
    
    if part < 2:
        start_node = 'AAA'
        steps = 0
        node = start_node
        dir_ind = 0
        while node != 'ZZZ':
            go_this_way = dirs[dir_ind]
            node = nodes[node][go_this_way]
            steps += 1
            dir_ind += 1
            if dir_ind >= len(dirs):
                dir_ind = 0

        print(f"PART 1: Starting at {start_node}, it took {steps} steps to reach {node}")
    else:
        # PART 2
        print("===== PART 2 =====")
        start_nodes = []
        
        for node in nodes:
            if node.endswith('A'):
                start_nodes.append(node)

        print(f"Starting at nodes: {' '.join(start_nodes)}")
        # now we have all starting nodes. Now iterate over them until we hit end nodes
        
        def all_nodes_done(node_list: List[str]) -> bool:
            for node in node_list:
                if not node.endswith('Z'):
                    return False
            return True
        
        dir_ind = 0
        steps = 0
        loop_steps = {}
        loops_recorded = []
        product = 1
        while not all_nodes_done(start_nodes):
            # if steps % 1000 == 0:
            #     strs = []
            #     for loop_node, n_steps in loop_steps.items():
            #         strs.append(f"{loop_node} = {n_steps}")
            #     print(", ".join(strs))

            this_way = dirs[dir_ind]

            for node_ind in range(len(start_nodes)):
                curr_node = start_nodes[node_ind]

                if curr_node.endswith('Z'):
                    if curr_node not in loop_steps:
                        print(f"Starting record of {curr_node} loop at {steps} steps...")
                        loop_steps[curr_node] = steps # record the starting step-count
                    elif curr_node not in loops_recorded:
                        loop_steps[curr_node] = steps - loop_steps[curr_node]
                        print(f"Closed loop for {curr_node} completed in {loop_steps[curr_node]}.")
                        loops_recorded.append(curr_node)

                start_nodes[node_ind] = nodes[curr_node][this_way]

            if len(loops_recorded) == len(start_nodes) and product == 1:
                # evaluate how many steps it will take to land on all of these bad bois
                
                for node_name, n_steps in loop_steps.items():
                    if gmpy2.is_prime(n_steps):
                        print(f"{node_name}'s loop step count ({n_steps}) is prime.")
                    else:
                        print(f"{node_name}'s loop step count ({n_steps}) is NOT prime.")
                        def all_prime(l):
                            if len(l) < 1:
                                return False
                            for n in l:
                                if not gmpy2.is_prime(n):
                                    return False
                            return True
                        
                        prime_facts = []
                        n = n_steps
                        while not all_prime(prime_facts):
                            while n % 2 == 0:
                                if 2 not in prime_facts: prime_facts.append(2)
                                n = int(n / 2.0)
                            for i in range(3,int(math.sqrt(n))+1,2):
                                # while i divides n , print i ad divide n
                                while n % i == 0:
                                    if i not in prime_facts: prime_facts.append(i)
                                    n = int(n/i)
                            if n > 2:
                                prime_facts.append(n)
                        print(f"It's prime factorization is: {prime_facts}")

                    if product / n_steps != float(int(product/n_steps)):
                        product = product * n_steps
                print(f"Part 2 guess: {product} steps to reach all XXZ nodes...")


            steps += 1
            dir_ind += 1
            if dir_ind >= len(dirs):
                # print(f"After step {steps}: {' '.join(start_nodes)}")
                # we're at the end, so add a note to each node saying where
                # we'll end up 
                dir_ind = 0

        print(f"PART 2: Starting at {len(start_nodes)} nodes, it took {steps} steps to reach all end nodes.")