a = int(input('Digite 1 número: '))
b = int(input('Digite 1 número: '))
c = int(input('Digite 1 número: '))
if a > b and a > c:
    print('{} é o maior número!'.format(a))
elif b > a and b > c:
    print('{} é o maior número!'.format(b))
else:
    print('{} é o maior número!'.format(c))