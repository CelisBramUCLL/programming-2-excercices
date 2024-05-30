def cycle(iter):
    i = 0
    while True:
        yield iter[i]
        i += 1
        if i == len(iter):
            i = 0
