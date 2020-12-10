import numpy as np

def read_input(file):
    f = open(file, 'r')
    out = f.readlines()
    f.close()
    return out

def read_map(file):
    out = np.loadtxt(file, dtype=np.str)
    return out


def main():
    input = read_map("input/3_1_input.txt")
    # print(input)
    # print(input[0][0])
    # maksimi rivimäärä
    i_max = len(input) # 323
    # maksimi sarakemäärä
    j_max = len(input[0]) #31
    j = 0
    treecounter = 0
    for i in range(1, i_max):
        #print (i)
        j = j + 3
        if j > j_max -1:
            j = j - j_max
        print(i, ", ", j)
        testchar = input[i][j]
        print(testchar)
        if testchar == 'a':
            treecounter += 1


    print(treecounter)




    # kasvata riviä kunnes ollaan vikalla rivillä
    # kasvata saraketta kolmella
    # tarkista onko sarake kartan sisällä
        # jos ei, päivitä s.e ollaan vasemmalta katsoen oikeassa sarakkeessa
    # palauta kirjain
    # tarkista, onko puu, jos niin lisää puucounteria yhdellä
    # palauta puucounter


if __name__ == "__main__":
    main()
