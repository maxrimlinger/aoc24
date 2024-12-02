with open("part1.txt", "r") as file:
    both_lists = file.read().split()
    list1 = []
    list2 = []
    for i, n in enumerate(both_lists):
        if i % 2 == 0:
            list1.append(n)
        else:
            list2.append(n)
    list1.sort()
    list2.sort()
    total_diff = 0
    for n1, n2 in list(zip(list1, list2)):
        # by now you might be thinking "this is incredibly inefficient" and you'd be right
        total_diff += abs(int(n1)-int(n2))
    print(total_diff)
