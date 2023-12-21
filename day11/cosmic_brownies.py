
import sys
from typing import Dict, List, Tuple


def print_galaxy(img):
    for row in img:
        print(''.join(row))



########## main function slug ############
if __name__ == '__main__':

    if len(sys.argv) > 1:
        # read input
        inp = open(sys.argv[1], 'r')
    else:
        inp = open('input.txt', 'r')
    
    og_img = []
    for raw_line in inp:
        line = raw_line.strip()
        og_img.append(list(line))

    # CLOSE INPUT FILE
    inp.close()

    # print_galaxy(og_img)
    # print()

    exp_img = []

    rows_to_expand = []
    for row_ind in range(len(og_img)):
        row = og_img[row_ind]
        exp_img.append(row)
        if '#' not in row:
            # row is empty of galaxies, append it again to double this gap's size
            exp_img.append(row)
            rows_to_expand.append(row_ind)

    cols_to_expand = []
    for col_ind in range(len(og_img[0])):
        is_galaxy_here = False
        for row_ind in range(len(og_img)):
            is_galaxy_here = is_galaxy_here or og_img[row_ind][col_ind] == '#'
            if is_galaxy_here:
                break
        if not is_galaxy_here:
            cols_to_expand.append(col_ind)
    
    # now actually expand the columns
    for row_ind in range(len(exp_img)):
        og_row = exp_img[row_ind]
        new_row = []
        for col_ind in range(len(og_row)):
            new_row.append(og_row[col_ind])
            if col_ind in cols_to_expand:
                new_row.append('.')
        exp_img[row_ind] = new_row
    
    # print_galaxy(exp_img)
    # print()

    # now number the galaxies and record coordinates
    galaxies = {}
    galaxy_num = 0
    for y in range(len(exp_img)):
        row = exp_img[y]
        for x in range(len(row)):
            if exp_img[y][x] == '#':
                galaxy_num += 1
                exp_img[y][x] = f'{galaxy_num}'
                galaxies[galaxy_num] = [y, x]
    
    galaxies_pt2 = {}
    galaxy_num = 0
    for y in range(len(og_img)):
        row = og_img[y]
        for x in range(len(row)):
            if og_img[y][x] == '#':
                galaxy_num += 1
                og_img[y][x] = f'{galaxy_num}'
                galaxies_pt2[galaxy_num] = [y, x]
    
    print_galaxy(og_img)
    print()

    ints = list(range(1, galaxy_num + 1))
    print(ints)
    pairs = []
    while len(ints) > 0:
        pair_with = ints.pop(0)
        for n in ints:
            pairs.append([pair_with, n])

    print(pairs)
    print(f"We have {len(pairs)} pairs of galaxies")

    # compute distances
    # PART 1
    paths = []
    for pair in pairs:
        gal_a = pair[0]
        gal_b = pair[1]
        coord_a = galaxies[gal_a]
        coord_b = galaxies[gal_b]

        delta_y = abs(coord_a[0] - coord_b[0])
        delta_x = abs(coord_a[1] - coord_b[1])
        path_len = delta_y + delta_x
        # print(f"Shortest path from {gal_a} to {gal_b} is {path_len} steps")
        paths.append(path_len)
    
    print(f"PART 1 SUM: {sum(paths)}")

    EMPTY_SPACE = 1000000
    paths = []
    for pair in pairs:
        gal_a = pair[0]
        gal_b = pair[1]
        coord_a = galaxies_pt2[gal_a]
        coord_b = galaxies_pt2[gal_b]

        delta_y = abs(coord_a[0] - coord_b[0])
        add_rows = 0
        for y in rows_to_expand:
            if y > min(coord_a[0], coord_b[0]) and y < max(coord_a[0], coord_b[0]):
                add_rows += 1
        delta_y = delta_y + add_rows * (EMPTY_SPACE - 1)

        delta_x = abs(coord_a[1] - coord_b[1])
        add_cols = 0
        for x in cols_to_expand:
            if x > min(coord_a[1], coord_b[1]) and x < max(coord_a[1], coord_b[1]):
                add_cols += 1
        delta_x = delta_x + add_cols * (EMPTY_SPACE - 1)

        path_len = delta_y + delta_x
        paths.append(path_len)
    
    print(f"PART 2 SUM: {sum(paths)}")