n=int(input('n = '))

result = []
for i in range(1,n+1):
    if i%3==0:
        result.append('buzz')
    if i%5==0:
        result.append('buzz')
    else:
        result.append(i)

print(result)