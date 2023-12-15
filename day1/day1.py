
import sys

digit_map = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def find_first_digit(s):
    for i in range(len(s)):
        if s[i].isnumeric():
            return s[i]
        else:
            for ii in range(len(digit_map)):
                dig = digit_map[ii]
                if s[i : i + len(dig)] == dig:
                    # substring in s matches digit string at index ii
                    # return ii
                    return f'{ii}'
            
    return '0' # why has this happened lol

def find_last_digit(s):
    len_s = len(s)
    for ind in range(len_s):
        i = (len_s - 1) - ind
        if s[i].isnumeric():
            return s[i]
        else:
            for ii in range(len(digit_map)):
                dig = digit_map[ii]
                if i + len(dig) <= len_s and s[i : i + len(dig)] == dig:
                    # substring in s matches digit string at index ii
                    # return ii
                    return f'{ii}'
    return '0'

########## main function slug ############
if __name__ == '__main__':

    if len(sys.argv) > 1:
        # read input
        inp = open(sys.argv[1], 'r')
    else:
        inp = open('input.txt', 'r')
    
    outp = open('output.txt', 'w')

    sum = 0

    for line in inp:
        result = ''

        # approach from the front
        for c in line:
            if c.isnumeric():
                result += c
                break
        
        # approach from the end
        for c in reversed(line):
            if c.isnumeric():
                result += c
                break
        
        # print('{} ==> {}'.format(line.strip(), result))
        outp.write(result + '\n')
        try:
            sum += int(result)
        except ValueError:
            sum += 0
    
    print(f"Sum of all calibration value = {sum}")

    inp.close()

    # PART 2 BEGINS
    print("===== PART 2 =====")
    if len(sys.argv) > 1:
        # read input
        inp = open(sys.argv[1], 'r')
    else:
        inp = open('input.txt', 'r')
    
    sum = 0

    for line in inp:
        result = find_first_digit(line.strip())
        result += find_last_digit(line.strip())
        sum += int(result)
    
    print(f"Part 2 sum of all calibration values = {sum}")