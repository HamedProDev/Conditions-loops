def star_diamond(n):
    mid = n // 2 

    for i in range(n):
        row = ""
        for j in range(n):
            if abs(i - mid) + abs(j - mid) <= mid:
                row += "* "
            else:
                row += "  "
        print(row)
        

star_diamond(5)