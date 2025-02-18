# In the UK, the currency is made up of pound and pence. How many different
# ways can 2 pound can be made using any number of coins?

def count_ways(target: int, coins: set) -> int:
    ways = [0] * (target + 1)
    ways[0] = 1   # base case, one way to make 0p

    for coin in coins:
        for amount in range(coin, target + 1):
            ways[amount] += ways[amount - coin]

    return ways[target]

# define the coins
coins = {
    1, 2, 5, 10, 20, 50, 100, 200
}

if __name__ == '__main__':
    result = count_ways(200, coins=coins)
    print(f"The number of ways to make £2: {result}")
    print(count_ways(5, coins=coins))  # 4