import numpy as np

def read_input(file):
    f = open(file, 'r')
    out = f.readlines()
    f.close()
    return out

def read_map(file):
    out = np.loadtxt(file, dtype=np.str)
    return out

def run_slope(i_step, j_step, i_max, j_max, input):
    treecounter = 0
    i = 0
    j = 0
    i_step = i_step
    j_step = j_step
    i_max = i_max
    j_max = j_max
    input = input
    while i < i_max - 1:
        i = i + i_step
        j = j + j_step
        if j > j_max - 1:
            j = j - j_max
        # print(i, ", ", j)
        testchar = input[i][j]
        # print(testchar)
        if testchar == 'a':
            treecounter += 1

    return treecounter

def main():
    input = read_map("input/3_1_input.txt")
    # print(input)
    # print(input[0][0])
    # maksimi rivimäärä
    i_max = len(input) # 323
    # maksimi sarakemäärä
    j_max = len(input[0]) #31

    ajo_1_3 = run_slope(1,3, i_max, j_max, input)
    ajo_1_1 = run_slope(1, 1, i_max, j_max, input)
    ajo_1_5 = run_slope(1, 5, i_max, j_max, input)
    ajo_1_7 = run_slope(1, 7, i_max, j_max, input)
    ajo_2_1 = run_slope(2, 1, i_max, j_max, input)
    print(ajo_1_3 * ajo_1_1 * ajo_1_5 * ajo_1_7 * ajo_2_1)




    # kasvata riviä kunnes ollaan vikalla rivillä
    # kasvata saraketta kolmella
    # tarkista onko sarake kartan sisällä
        # jos ei, päivitä s.e ollaan vasemmalta katsoen oikeassa sarakkeessa
    # palauta kirjain
    # tarkista, onko puu, jos niin lisää puucounteria yhdellä
    # palauta puucounter


if __name__ == "__main__":
    main()
