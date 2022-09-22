nev = input('írd be a neved: ')
print(f'Hello {nev}!')
print(f'Ó, de szép név az hogy {nev}!')
print(f'Szerintem már most beléd vagyok zúgva {nev}! <3')

valasz = input(f'{nev}, szeretsz programozni? ')
if valasz in {'igen', 'ja', 'persze', 'naná', 'IGEN', 'hogy a fenébe ne!'}:
    print('akkor még itt sokra viheted!')
else:
    print('akkor remélem, majd megszereted idővel...')

szam = int(input(f'Hányszor írjam ki a neved {nev}? '))
for x in range(szam):
    print(f'{nev}', end=' ')