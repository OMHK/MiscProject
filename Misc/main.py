spam = []
x = 0
thestr = ''
for x in range(99):
    print('Car name? or exit')
    n = input()
    if n == 'exit':
        m = x
        x = x - 1
        break
    else:
        spam.append(n)
spam.insert(x,'and')
m2 = ' '.join(map(str,spam))
print(m2)

