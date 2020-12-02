def read_input(file):
    f = open(file, 'r')
    out = f.readlines()
    f.close()
    return out


def main():
    input = read_input("input/1_1_input.txt")
    print(input)
    for i in input:

        for j in input:
            if i != j:
                testsum = int(i) + int(j)
                #print(testsum)
                if testsum == 2020:
                    print("Löytyi! i on: ", i, " ja j on: ", j )
                    print("checksum: ", int(i)*int(j))
                    exit()


if __name__ == "__main__":
    main()
