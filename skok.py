subor = open('skok.txt','r')
povod = {}
max = 0
vitaz = []
for riadok in subor:
    udaje=riadok.split()
    povod[udaje[1]] = povod.get(udaje [1],0)+1
    dlzka = 0
    for i in range(5):
        dlzka = max(dlzka, int(udaje[i+2]))
    if dlzka > max:
        max = dlzka                           
        vitaz = [udaje[1]]
    elif dlzka == max:                           
        vitaz.append(udaje[0] )
print ('Zoznam krajin povodu:')
print ('Najdlhsi skok:', max)
for vitaz in vitaz:
    print (vitaz)
