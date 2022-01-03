beenged=False

while not beenged:
    nev=input('Add meg a felhasználóneved!')
    jelszo=input('Add meg a jeszavad!')
    if nev=='Bori99' and jelszo=='szívecske':
        print('Beléphetsz!')
        beenged=True
    else:
        print('Belépés megtagadva!')
        
