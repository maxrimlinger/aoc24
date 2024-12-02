with open("input.txt", "r") as file:
    lines = file.splitlines()
    num_safe = 0
    for line in lines:
        inc = 0
        prev_num = None
        for n in line.split():
            if prev_num is not None:
                if inc == 0:
                    if n > prev_num:
                        inc = 1
                    else if n < prev_num:
                        inc = -1
                    else:
                        break
                else:
                    if n > prev_num and inc == -1:
                        break
                    else if n < prev_num and inc == 1:
                        break
            prev_num = n
