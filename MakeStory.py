import random
import words as w



while True:
    paragraphe=[]
    for phrase in w.templates:
        
        parties=[]
        bechtlasaknoun=phrase.split('{{noun}}')
        #print(bechtlasaknoun)
        parties.append(bechtlasaknoun.pop(0))
        if(len(bechtlasaknoun)>0):
            for i in range(0,len(bechtlasaknoun)):
                parties.append(random.choice(w.nouns)+bechtlasaknoun.pop(0))
        phrasewithnom="".join(parties)
        #print(phrasewithnom)

        partiesv=[]
        bechtlasaknoun=phrasewithnom.split('{{verb}}')
        partiesv.append(bechtlasaknoun.pop(0))
        if(len(bechtlasaknoun)>0):
            for i in range(0,len(bechtlasaknoun)):
                partiesv.append(random.choice(w.verbs)+bechtlasaknoun.pop(0))
        phrasecomplet="".join(partiesv)
       # print(phrasecomplet)
        paragraphe.append(phrasecomplet)

    print("\n".join(paragraphe))
    print('')
    input()
    
    
    
