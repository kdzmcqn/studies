def minimumswap(status):
    return min(countswap(status,'S'),countswap(status,'R'))

def countswap(status, initial):
    count = 0
    for i in range(len(status)):
        if status[i] != initial:
            count += 1
        initial = swap(initial)
    return count

def swap(initial):
    return 'S' if (initial == 'R') else 'R'

if __name__ == '__main__':
    status = 'SRRRS'
    print(minimumswap(status))