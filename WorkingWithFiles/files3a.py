with open("files3.txt") as mail:
    count = 0
    number = 0
    for line in mail:
        if not line.startswith("X-DSPAM-Confidence") : continue
        list1 = line.split(":")
        v = list1[1]
        list2 = v.split()
        n = float(list2[0])
        number += n
        count += 1
    av = number / count
    print("Average: ", av)
