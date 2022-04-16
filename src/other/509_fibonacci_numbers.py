def fib(N):
    dp = [0, 1]
    for i in range(2, 31):
        f = dp[i - 1] + dp[i - 2]
        dp.append(f)
    
    return dp[N]


if __name__ == "__main__":
    fibo = fib(4)
    print(fibo)