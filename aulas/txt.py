t = open('count.txt', 'w')

for c in range(1, 101):
    t.write(str(c) + '\n')
t.close()

t = open('count.txt', 'r')

for linha in t:
    print (linha.strip())
