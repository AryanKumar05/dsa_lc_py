class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        m=len(s)
        n=len(s[::-1])
        text1=s
        text2=s[::-1]
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1]==text2[j-1]:  #char match
                    dp[i][j]=1+dp[i-1][j-1]
                else:                         #no char match.take best from skipping either 
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[m][n]

    # class Solution:
    # def longestPalindromeSubseq(self, s: str) -> int:
    #     n = len(s)
    #     dp = [[0] * n for _ in range(n)]

    #     # Every single character is a palindrome of length 1
    #     for i in range(n):
    #         dp[i][i] = 1

    #     # Fill table for increasing substring lengths
    #     for length in range(2, n + 1):
    #         for i in range(n - length + 1):
    #             j = i + length - 1
    #             if s[i] == s[j]:
    #                 dp[i][j] = dp[i + 1][j - 1] + 2
    #             else:
    #                 dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    #     return dp[0][n - 1]

        