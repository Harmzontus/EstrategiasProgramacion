def lucas_tab(n):
    if n == 0:
        return 2
    if n == 1:
        return 1

    lucas = [0] * (n + 1)
    lucas[0] = 2
    lucas[1] = 1

    for i in range(2, n + 1):
        lucas[i] = lucas[i - 1] + lucas[i - 2]

    return lucas[n]

def lucas_memo(n, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]
    
    if n == 0:
        return 2
    if n == 1:
        return 1

    memo[n] = lucas_memo(n - 1, memo) + lucas_memo(n - 2, memo)
    return memo[n]

for i in range(10):
    #print(f"Lucas({i}) - Tabulacion: {lucas_tab(i)}")
    print(f"Lucas({i}) - Memorizacion: {lucas_memo(i)}")
