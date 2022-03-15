import shelve


from moves import move1, move2, move3, move4


with shelve.open('dance.db') as db:
    db['1'] = move1
    db['2'] = move2
    db['3'] = move3
    db['4'] = move4

# wait spme time

with shelve.open('dance.db') as db:
    print(db['1'])
    print(list(db.keys()))
