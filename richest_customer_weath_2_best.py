
class Solution():
    def maximumWealth(_,accounts):
        sum_accounts = [sum(account) for account in accounts]
        return max(sum_accounts)

if __name__ == "__main__":
    # create an instance of the solution class 
    solution = Solution()
    accounts = [[7,1,2],[8,5,6],[1,2,9]]
    # call the maximumweath   method and print the restult
    result = solution.maximumWealth(accounts)
    print(result)
