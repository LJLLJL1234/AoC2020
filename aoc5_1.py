import re

def read_input(file):
    f = open(file, 'r')
    out = f.readlines()
    f.close()
    return out

def test_seat(seat):
    retval = False
    try:
        if re.match('^[FB]{7}$',seat[0:7]) is not None:
            if re.match('^[LR]{3}$', seat[7:]) is not None:
                retval = True
    except:
        print("Väärä formaatti!: ", seat)
    return retval

def convert_to_bin(row):
    output = row.replace("F", "0")
    output = output.replace("B", "1")
    output = output.replace("R", "1")
    output = output.replace("L", "0")
    row = output[0:7]
    col = output[7:]
    return [row, col]

def print_row(row):
    return int(row, 2)

def print_col(col):
    return int(col, 2)

def main():
    input = read_input("input/5_1input.txt")

    print(test_seat(input[0]))
    seat_ids = []
    for i in input:
        if test_seat(i) is not True:
            continue
        seat_bin = convert_to_bin(i)
        row = print_row(seat_bin[0])
        col = print_col(seat_bin[1])
        seat_id = 8*row + col
        #print("Rivi on: ", row, ", paikka on: ", col)
        seat_ids.append(seat_id)

    #print(max(seat_ids))
    #print(seat_ids.sort())
    seat_ids.sort()
    print(seat_ids)

    for i in range(0, len(seat_ids) -1):
        if seat_ids[i] +1 != seat_ids[i+1]:
            print("Paikka on: ", seat_ids[i] + 1)
            continue


if __name__ == "__main__":
    main()
