def my_function(sup):
    n = len(sup)
    if n <= 1:
        return True

    else:
        Howdy = []

        for i in range (n):
            row = []
            for j in range (n):
               row.append(i + j)

            Howdy.append(row)

    return Howdy





