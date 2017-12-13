from brrr import skrrrahh

# None -> random sound
skrrrahh()

# number from [0,50] -> sound from dictionary
skrrrahh(10)

# number larger than 50 -> warning and random sound
skrrrahh(51)

# string from acceptable strings -> sound from dictionary
skrrrahh('gucci')

# sound file path -> play wav from path
skrrrahh('brrr/adlibs/bigshaq.wav')
