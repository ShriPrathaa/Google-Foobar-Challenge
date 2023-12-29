def solution(n):
    s=0
    for i in range(2,20):
        if(i*(i+1)>2*n):
            break
        s+=NumberOfways(n-(i*(i+1)//2),i)
    return s
def NumberOfways(N, K):
    dp = [0] * (N + 1)
    dp[0] = 1
    for row in range(1, K + 1):
        for col in range(1, N + 1):
            if col >= row:
                dp[col] += dp[col - row]
    return dp[N]
