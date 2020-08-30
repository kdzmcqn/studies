def bubblesort(n):
    swapcount = 0
    run = True
    while run:
        run = False
        for j in range(len(n)-1):
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
                swapcount +=1
                run = True
    return swapcount , n

if __name__ == '__main__':
    n = [4,3,2,1]
    print(bubblesort(n))