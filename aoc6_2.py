from collections import Counter
from itertools import chain

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
            ans_data += " "
        else:
            #print(id_data)
            ans_array.append(ans_data.strip())
            ans_data = ""

    ans_array.append(ans_data)
    ans_array[len(ans_array) - 1] = ans_array[len(ans_array) - 1].rstrip()
    print(ans_array)

    counts = []
    for i in ans_array:
        temp_arr = i.split(" ")

        temp = (set(sub) for sub in temp_arr)
        cntr = Counter(chain.from_iterable(temp))
        res = [chr for chr, count in cntr.items() if count == len(temp_arr)]
        counts.append(len(res))

    print(len(ans_array))
    print(len(counts))
    print(sum(counts))

if __name__ == "__main__":
    main()