with open("input.txt", "r") as file:
    both_lists = file.read().split()
    list1 = []
    list2 = []
    for i, n in enumerate(both_lists):
        if i % 2 == 0:
            list1.append(n)
        else:
            list2.append(n)
    freq_map = dict()
    for n in list2:
        if n in freq_map:
            freq_map[n] += 1
        else:
            freq_map[n] = 1
    total_sim = 0
    for n in list1:
        if n in freq_map:
            total_sim += int(n) * freq_map[n]
    print(total_sim)
