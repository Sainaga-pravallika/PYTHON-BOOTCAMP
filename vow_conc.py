all conconents countand vowel count


p="pravallika"
vowl="aeiou"
conconents="bcdfghjklmnpqrstvwxyz"
count_vowl=0
count_conconents=0
for i in p:
    if(i in vowl):
        count_vowl+=1 
    elif(i in conconents):
        count_conconents+=1 
print(count_vowl)
print(count_conconents)