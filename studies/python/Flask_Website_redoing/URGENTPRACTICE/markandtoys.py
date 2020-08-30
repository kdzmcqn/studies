def maxtoyprices(n,k,toyPrices):
    toyPrices.sort()
    payment = 0
    toys = 0
    for i in range(n):
        payment += toyPrices[i]
        if payment <= k:
            toys += 1
        else:
            break
    return toys, payment


if __name__ == '__main__':
    n = 7
    k = 50
    toyPrices = [1, 12, 5, 111, 200, 1000 ,10]
    print(maxtoyprices(n,k, toyPrices))