accounts = [[7,1,2],[8,5,6],[1,2,9]]
len_accounts=len(accounts)
sum_accounts =[]

for i in range(len_accounts):
    sum_accounts.append(sum(accounts[i]))

print(sum_accounts)

max_wealth = max(sum_accounts)
print(max_wealth)
