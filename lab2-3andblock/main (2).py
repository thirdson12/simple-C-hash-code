import hashlib

def merkle_root(transactions):
    if len(transactions) == 0:
        return None
    elif len(transactions) == 1:
        return (transactions[0], hashlib.sha256(transactions[0].encode()).hexdigest())

    merkle = []
    for t in transactions:
        merkle.append((t, hashlib.sha256(t.encode()).hexdigest()))

    while len(merkle) > 1:
        if len(merkle) % 2 != 0:
            merkle.append(merkle[-1])

        new_merkle = []
        for i in range(0, len(merkle), 2):
            new_merkle.append((merkle[i][0] + merkle[i+1][0], hashlib.sha256((merkle[i][1] + merkle[i+1][1]).encode()).hexdigest()))

        merkle = new_merkle

    return merkle[0]

transactions = ['hello', 'world', 'foo', 'bar']

root = merkle_root(transactions)

print(root[0], '(' + root[1][:8] + '...)')
for t in reversed(transactions):
    if t == root[0]:
        break
    if t == transactions[-1]:
        print('  |')
    else:
        print('  |')
        print(t, '(' + hashlib.sha256(t.encode()).hexdigest()[:8] + '...)')
