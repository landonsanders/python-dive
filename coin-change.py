def count_ways(n, m):
    ways = [0] * (n + 1)
    ways[0] = 1
    
    for coin in m:
        for j in range(coin, n + 1):
            ways[j] = ways[j] + ways[j - coin]
        
    return ways[n]

def count_change(n, m):
    
    coins = [1, 5, 10]
    coin_list = []
    
    for coin in coins:
        count = n / m
        coin_list = coin_list + ([coin,] * count)
        n = n - (count * coin)
    