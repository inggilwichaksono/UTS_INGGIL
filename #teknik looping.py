# teknik looping

nama_band = ['Payung Teduh',
             'Fourtwnty',
             'Dialog Dini Hari',
             'Mr. Sonjaya',
             'Parahyena']

kumpulan_lagu = ['Akad',
            'Zona Nyaman'
            'Rumahku',
            'Sang Filsuf',
            'Sindoro']
# enumerate

for index,band in enumerate (nama_band):
    print(index,':',band)

# zip

for band,lagu in zip(nama_band,kumpulan_lagu):
    print(band,'menyanyikan lagu yang berjudul:',lagu)
    

