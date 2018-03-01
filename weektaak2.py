import matplotlib.pyplot as plt
import matplotlib.patches as pat
import numpy as np

def main(): #main functie die alle functies aanroept
    doorgaan = 'y'                                              #geef doorgaan de waarde y
    while doorgaan == 'y':                                      #zo lang doorgaan waarde y heeft
        filename = keuze()                                      #roep keuze functie aan
        if filename != 'FALSE':                                 #als filename niet FALSE is
            completeSeq = seqSamensteller(filename)             #roep de seqSamensteller functie aan
            cutLijst, knipLengte = splitsen(completeSeq)        #roep de splitsen functie aan
            GCLijst = GCberekening(cutLijst)                    #roep de GCberekening functie aan
            plotting(GCLijst, knipLengte, filename)             #roep de plotting functie aan
            output(GCLijst)                                     #roep de output functie aan
            print('-'*80, '\n') 
            doorgaan = input('wil je doorgaan? y/n ')           #geef doorgaan de waarde van invoer      
            print('\n', '-'*80)

def keuze(): #functie die een keuzemenu opzet
    print('welk bestand wil je de GC percentages van? kies het nummer')
    print('1. E.coli-gen.fasta \n2. E.coli-genoom.fasta \n3. HomoSapiens-cds.txt \n4. Homosapiens-cds.fasta \n5. Salmonella-gen.fasta \n6. Salmonella-genoom.fasta \n7. Soybean-chr4.fasta \n8. Soybean-cds.fasta\n')
    print('of een van de virussen')
    print('9. ProteinSIV.txt \n10. GenomeSIV.fasta \n11. CDSSIV.txt')
    print('12. ProteinSIVmnd-2.txt \n13. GenomeSIVmnd-2.fasta \n14. CDSSIVmnd-2.txt')
    print('15. ProteinHIV-2.txt \n16. GenomeHIV-2.fasta \n17. CDSHIV-2.txt')
    print('18. ProteinHIV-1.txt \n19. GenomeHIV-1.fasta \n20. CDSHIV-1.txt\n')
    keuzebestand = input('welk bestand wil je openen? ')        #geef keuzebestand de waarde van invoer
    if keuzebestand == '1':                                     #als keuzebestand 1 is...
        return 'E.coli-gen.fasta'
    elif keuzebestand == '2':                                   #als keuzebestand 2 is...
        return 'E.coli-genoom.fasta'
    elif keuzebestand == '3':                                   #als keuzebestand 3 is...
        return 'HomoSapiens-chr19.fasta'
    elif keuzebestand == '4':                                   #als keuzebestand 4 is...
        return 'HomoSapiens-cds.txt'
    elif keuzebestand == '5':                                   #als keuzebestand 5 is...
        return 'Salmonella-gen.fasta'
    elif keuzebestand == '6':                                   #als keuzebestand 6 is...
        return'Salmonella-genoom.fasta'
    elif keuzebestand == '7':                                   #als keuzebestand 7 is...
        return 'Soybean-chr4.fasta'
    elif keuzebestand == '8':                                   #als keuzebestand 8 is...
        return 'Soybean-cds.txt'
    elif keuzebestand == '9':                                   #als keuzebestand 9 is...
        return 'ProteinSIV.txt'
    elif keuzebestand == '10':                                   #als keuzebestand 10 is...
        return 'GenomeSIV.fasta'
    elif keuzebestand == '11':                                   #als keuzebestand 11 is...
        return 'CDSSIV.txt'
    elif keuzebestand == '12':                                   #als keuzebestand 12 is...
        return 'ProteinSIVmnd-2.txt'
    elif keuzebestand == '13':                                   #als keuzebestand 13 is...
        return 'GenomeSIVmnd-2.fasta'
    elif keuzebestand == '14':                                   #als keuzebestand 14 is...
        return 'CDSSIVmnd-2.txt'
    elif keuzebestand == '15':                                   #als keuzebestand 15 is...
        return 'ProteinHIV-2.txt'
    elif keuzebestand == '16':                                   #als keuzebestand 16 is...
        return 'GenomeHIV-2.fasta'
    elif keuzebestand == '17':                                   #als keuzebestand 17 is...
        return 'CDSHIV-2.txt'
    elif keuzebestand == '18':                                   #als keuzebestand 18 is...
        return 'ProteinHIV-1.txt'
    elif keuzebestand == '19':                                   #als keuzebestand 19 is...
        return 'GenomeHIV-1.fasta'
    elif keuzebestand == '20':                                   #als keuzebestand 20 is...
        return 'CDSHIV-1.txt'
    else:                                                       #anders...
        print('dat is geen optie, probeer het opnieuw')
        print('-'*80, '\n')
        return 'FALSE'

def seqSamensteller(filename): #functie die de sequenties samenstelt en de header van de sequentie scheidt
    try:                                                                                #probeer...
        file = open(filename)                                   
    except FileNotFoundError:                                                           #als het bestand niet bestaat...
        print('dit bestand bestaat niet')
        quit()                                                                          #beëindig het programma
    completeSeq = ''                                                                    #geef completeSeq een lege string
    for line in file.readlines():                                                       #loop door het bestand
        if line[0] == '>':                                                              #als het eerste teken > is...
            line = line.rstrip()                                                        #strip de line
            header = line                                                               #geef header de inhoud van line
        else:                                                                           #anders...
            line = line.rstrip()                                                        #strip de line
            completeSeq = completeSeq + line                                            #voeg de line toe aan completeSeq
    print('de sequentie van ', filename, 'heeft een lengte van ', len(completeSeq))
    return completeSeq

def splitsen(completeSeq): #functie die de sequentie in stukjes knipt van aangegeven lengte
    cuts = ''                                                                               #geeft cuts een lege string
    cutLijst = []                                                                           #maak een lege lijst genaamd cutLijst
    lengte = len(completeSeq)                                                               #geef lengte de waarde van de lengte van completeSeq
    if lengte / 100 <= 20:                                                                  #als lengte gedeeld door 100 minder of gelijk is aan 20...
        knipLengte = 50                                                                     #geef knipLengte de waarde 50
    elif lengte / 100 <= 100:                                                               #als lengte gedeeld door 100 minder of gelijk is aan 100...
        knipLengte = 100                                                                    #geef knipLengte de waarde 100
    elif lengte / 100 <= 1000:                                                              #als lengte gedeeld door 100 minder of gelijk is aan 1000...
        knipLengte = 1000                                                                   #geef knipLengte de waarde 1000
    elif lengte / 100 <= 10000:                                                             #als lengte gedeeld door 100 minder of gelijk is aan 10000...
        knipLengte = 10000                                                                  #geef knipLengte de waarde 10000
    else:                                                                                   #anders
        knipLengte = 100000                                                                 #geef knipLengte de waarde 100000
    print('-'*80)
    print('je kniplengte is momenteel ', knipLengte)
    overRide = input('wil je een andere kniplengte forceren? y/n ')                         #geef overRide de waarde van invoer
    if overRide == 'y':                                                                     #als overRide y is...
        try:                                                                                #probeer...
            knipLengte = int(input('geef aan hoe lang je de kniplengte wil hebben. '))      #geef knipLengte de waarde van invoer
        except ValueError:                                                                  #als de waarde van invoer niet klopt...
            print('onjuiste invoer') 
    for i in completeSeq:                                                                   #loop door completeSeq
        if len(cuts) <= knipLengte -1:                                                      #als de lengte van cuts minder of gelijk is aan knipLengte - 1
            cuts+=i                                                                         #voeg i toe aan cuts
        else:                                                                               #anders...
            cutLijst.append(cuts)                                                           #voeg cuts toe aan cutLijst
            cuts = ''                                                                       #maak cuts leeg
    return cutLijst, knipLengte                             

def GCberekening(cutLijst): #berekent GC percentages
    GCLijst = []                                #maak een lege lijst genaamd GCLijst
    aantalGC = 0                                #zeg aantalGD op 0
    for line in cutLijst:                       #loop door cutLijst
        for i in line:                          #loop door de line
            if i == 'G' or i == 'C':            #als i waarde G of C heeft...
                aantalGC+=1                     #verhoog aantalGC met 1
        GCPer = aantalGC / len(line) * 100      #reken het aantal GC om naar percentages en geef deze waarde aan GCPer
        GCLijst.append(GCPer)                   #voeg GCPer toe aan GCLijst
        aantalGC = 0                            #zet aantalGC op 0
    return GCLijst

def plotting(GCLijst, knipLengte, filename): #plot de data van GCLijst
    Xlijst = []
    x=0
    for i in GCLijst:
        Xlijst.append(x)
        x+=1
        
    diagram = plt.bar (Xlijst, GCLijst)
    plt.xticks(Xlijst)
    maxGC = (GCLijst.index(max(GCLijst)))
    minGC = (GCLijst.index(min(GCLijst)))
    diagram[maxGC].set_color('lightgreen')
    diagram[minGC].set_color('red')
    plt.axis([-1, len(Xlijst), 0, 100])
    plt.title('GC Percentages per meetfragment')
    plt.xlabel('meetfragment')
    plt.ylabel('GC percentage')
    rood = pat.Patch(color='red', label='laagste meting')
    groen = pat.Patch(color='lightgreen', label='hoogste meting')
    plt.legend(handles=[rood, groen])
    plt.show()

def output(GCLijst): #geeft output dmv wiskundige functies
    lijst = GCLijst
    lijst.sort()
    totaal, kwadTot = 0, 0 
    variLijst = []
    for i in lijst:
        totaal+=i
    gemiddelde = totaal/len(lijst)
    for i in lijst:
        variNum = i - gemiddelde
        variLijst.append(variNum)
    for i in variLijst:
        kwad = i*i
        kwadTot+=kwad
    variKwad = kwadTot / (len(variLijst)-1)
    variantie = np.sqrt(variKwad)
    mediaan = np.median(lijst)
    print('het gemiddelde GC percentage is: ', round(gemiddelde, 4))
    print('de variantie is: ', round(variantie, 4))
    print('de mediaan is: ', mediaan)
     
main() #roep main functie aan 














