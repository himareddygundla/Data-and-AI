def zigzag_pattern(n):
    for i in range(3):
        for j in range(n):
            if (i + j) % 2 == 0:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
