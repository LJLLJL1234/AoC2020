import re

def read_input(file):
    f = open(file, 'r')
    out = f.readlines()
    f.close()
    return out

def main():
    input = read_input("input/6_1input.txt")
    ans_array = []
    ans_data = ""
    for i in input:
        if i != "\n":
             # print(i.rstrip())
            ans_data += str(i.rstrip())
            #ans_data += " "
        else:
            #print(id_data)
            ans_array.append(ans_data.strip())
            ans_data = ""

    ans_array.append(ans_data)
    print(ans_array)

    yes_count = 0
    for i in ans_array:
        yes_count += len(''.join(set(i)))

    print(yes_count)
if __name__ == "__main__":
    main()