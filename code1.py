def main():
    sequentie = lees_bestand()
    honderd = splitten(sequentie)
    percentage = tellen(honderd)
    

def lees_bestand():
    bestand = open("Homosapiens-gen.fasta")
    sequentie = ''
    for regel in bestand:
        regel = regel.replace("\n", "")
        if not regel.startswith(">"):
            sequentie += regel
    #print(sequentie)
    return sequentie


def splitten(sequentie):
    for n in range(0,(len(sequentie)),100):
        honderd = sequentie[n:n+100]
        print(honderd)
    return honderd   


def tellen(honderd):
    print("honderd", honderd)
    teller = 0
    for char in honderd:
        for letter in char:
            if char == "C" or char == "G":
                
                teller += 1
                lengte = len(honderd)
                percentage = teller / lengte * 100
                #print("dit is", teller)
                #print(lengte)
                #print("dit is het percentage", percentage)
    return percentage
    
#piekenpatroon van elke 100 nucletide    

main()
