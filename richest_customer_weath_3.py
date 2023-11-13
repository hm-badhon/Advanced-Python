class Solution():
    def maximumWealth(_, accounts):
        len_accounts = len(accounts)
        sum_accounts = [] 
        for i in range(len_accounts):
            if accounts[i]:  # Check if the sublist is not empty
                sum_accounts.append(sum(accounts[i]))
            else:
                # Handle empty sublists if necessary
                sum_accounts.append(0)

        return max(sum_accounts)

if __name__ == "__main__":
    solution = Solution()
    accounts = [[7, 1, 2], [8, 5, 6], [1, 2, 9]]
    result = solution.maximumWealth(accounts)
    print(result)
