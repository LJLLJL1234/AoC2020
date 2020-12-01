def read_input(file):
    f = open(file, 'r')
    out = f.readlines()
    f.close()
    return out


def main():
    input = read_input("input/1_1_input.txt")
    print(input)

if __name__ == "__main__":
    main()
