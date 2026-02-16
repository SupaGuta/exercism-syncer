def find_fewest_coins(coins: list[int], target: int) -> list[int]:
    if target == 0: return []
    if target < 0:  raise ValueError("target can't be negative")

    # Work with a deterministic order (also avoids redundant work if duplicates exist)
    coins = sorted(set(coins), reverse=True)

    # Dynamic Programming algorithm
    inf = target + 1
    dp_count = [inf] * (target + 1) # minimum number of coins to make amount A (inf if impossible)
    dp_prev = [None] * (target + 1)  # which coin was last used to reach this amount

    dp_count[0] = 0
    for amount in range(1, target + 1):
        for coin in coins:
            if coin > amount:
                continue
            prev = amount - coin
            if dp_count[prev] + 1 < dp_count[amount]:
                dp_count[amount] = dp_count[prev] + 1
                dp_prev[amount] = coin

    if dp_prev[target] is None: raise ValueError("can't make target with given coins")

    # Reconstruct solution
    out = []
    amount = target
    while amount > 0:
        coin = dp_prev[amount]
        out.append(coin)
        amount -= coin

    return sorted(out)
