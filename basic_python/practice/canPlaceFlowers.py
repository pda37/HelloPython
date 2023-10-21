def canPlaceFlowers(flowerbed, n):
    if n > (len(flowerbed)+1)/2:
        return False
    else:
        flowerbed.insert(0, 0)
        flowerbed.append(0)
        print(flowerbed)
        m = 0
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                m += 1
        print(m, flowerbed)
        return m >= n


print(canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2))
