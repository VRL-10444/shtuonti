import random

def sukupuoli():
    sukupuoli = input("Sukupuoli: ");
    if sukupuoli != "tamma" and sukupuoli != "ori" and sukupuoli != "ruuna":
        sukupuoli = random.randint(1,2);
    if sukupuoli == 1:
        sukupuoli = "tamma";
    if sukupuoli == 2:
        sukupuoli = "ori";
    return sukupuoli;
    
def saka():
    min = input("Minimisäkäkorkeus: ")
    max = input("Maksimisäkäkorkeus: ")
    min = int(min);
    max = int(max);
    return random.randint(min, max);
    
def pohjavari():
    arvonta = random.randint(1, 100);
    pohjavari = ""
    if arvonta > 0 and arvonta < 30:
        pohjavari = "rautias (eeaa)"
    elif arvonta > 29 and arvonta < 58:
        pohjavari = "rautias (eeAA)"
    elif arvonta > 57 and arvonta < 89:
        pohjavari = "rautias (eeAa)"
    elif arvonta > 88 and arvonta < 91:
        pohjavari = "ruunikko (EeAa)"
    elif arvonta > 90 and arvonta < 93:
        pohjavari = "ruunikko (EeAA)"
    elif arvonta > 92 and arvonta < 95:
        pohjavari = "ruunikko (EEAa)"
    elif arvonta > 94 and arvonta < 97:
        pohjavari = "ruunikko (EEAA)"
    elif arvonta > 96 and arvonta < 99:
        pohjavari = "musta (Eeaa)"
    elif arvonta > 98 and arvonta <= 100:
        pohjavari = "musta (EEaa)"
    return pohjavari;
    
def hallakko():
    arvonta = random.randint(1, 100);
    if arvonta > 0 and arvonta < 50:
        return " ja kantaa non-dun 1 geeniä (nd1/nd2) eli sillä voi näkyä joitakin hallakon piirteitä, kuten siima"
    elif arvonta >= 50 and arvonta < 61:
        return " ja kantaa non-dun 1 geeniä (nd1/nd1) eli sillä voi näkyä joitakin hallakon piirteitä, kuten siima"
    else:
        return ""
    
def voikko():
    arvonta = random.randint(1, 200);
    if arvonta > 0 and arvonta < 5:
        return "   Lisäksi hevonen on yksinkertainen voikko (CR/n) \n";
    elif arvonta == 5:
        return "   Lisäksi hevonen on tuplavoikko (CR/CR) \n";
    else:
        return ""

def hopea():
    arvonta = random.randint(1, 200);
    if arvonta == 1:
        return "   Lisäksi hevonen on hopeavärinen (rn/m) tai hopeaa kantava rautias (Z/n) \n";
    else:
        return ""
        
def kimo():
    arvonta = random.randint(1, 200);
    if arvonta > 0 and arvonta < 6:
        return "   Lisäksi hevonen on kimo (G/n) \n";
    if arvonta == 6:
        return "   Lisäksi hevonen on kimo (G/G) \n"
    else:
        return ""
        
def splashed():
    arvonta = random.randint(1, 200);
    if arvonta == 1:
        return "   Lisäksi hevonen on splashed white -kirjava (SW1/n) \n";
    else:
        return ""
        
def rabicano():
    arvonta = random.randint(1, 500);
    if arvonta == 1:
        return "   Lisäksi hevonen on rabicano (genetiikka tuntematon) \n";
    else:
        return ""
        
def paista():
    arvonta = random.randint(1, 200);
    if arvonta == 1:
        return "   Lisäksi hevonen on päistärikkö (RN/n) \n";
    else:
        return ""

def w20():
    arvonta = random.randint(1, 200);
    if arvonta == 1:
        return "   Lisäksi hevonen on W20 -kirjava \n\n";
    else:
        return " \n "
        
def temp():
    arvonta = random.randint(1, 5);
    if arvonta == 1:
        return "todella helppo"
    if arvonta == 2:
        return "helppo"
    if arvonta == 3:
        return "keskiverto"
    if arvonta == 4:
        return "haastava"
    if arvonta == 5:
        return "todella haastava"

def koulu():
    arvonta = random.randint(1, 5);
    if arvonta == 1:
        return "todella helppo"
    if arvonta == 2:
        return "helppo"
    if arvonta == 3:
        return "keskiverto"
    if arvonta == 4:
        return "haastava"
    if arvonta == 5:
        return "todella haastava"
    
def main():
    print("SUOMENHEVOSTEN TUONTIKONE \n Määrittelee hevosen temperamentin ja koulutettavuuden satunnaisesti, arpoo hevosen sukupuolen annetulta väliltä sekä halutessa hevosen sukupuolen. Arpoo värin IRL suomenhevosten värijakauman mukaan jopa hieman anteliaasti, vaikka erikoisvärit harvinaisia ovatkin \n Konetta voidaan käyttää myös muiden rotujen kanssa, mutta värijakauma on tehty suomenhevosen mukaan. Muille roduille on mahdollista tehdä vastaavia, toiveita voi esittää keskustassa @K10444 \n\n")
    
    print("OHJEET: \n - Halutessasi valita sukupuolen, syötä haluttu sukupuoli (tamma, ori tai ruuna). Muutoin anna mikä tahansa syöte, ja kone arpoo tamman ja orin välillä. \n - Säkäkorkeutta määrittäessä syötä VAIN numero ja varmista, että minimiraja on maksimia pienenpi \n - Ohjelman lopussa kysytään haluatko uuden hevosen, jos, kirjoita kyllä.\n\n");
    
    print("_____________________________________________________________________ \n")
    
    uusheppa = "kyllä";
    
    while uusheppa == "kyllä":
        skp = sukupuoli()
        cm = saka()
        pohja = pohjavari()
        hlko = hallakko()
        vkk = voikko()
        hp = hopea()
        km = kimo()
        sw = splashed()
        rab = rabicano()
        paist = paista()
        w = w20()

        print("_____________________________________________________________________ \n")
    
        print("Hevosesi on ", end = "");
        print(cm, end = "");
        print(" senttinen ", end = "");
        print(skp, end = "");
        print(".");
    
        print("Se on pohjaväriltään ", end = "");
        print(pohja, end = "");
        print(hlko);
        print(vkk, end = "");
        print(hp, end = "");
        print(km, end = "");
        print(sw, end = "");
        print(paist, end = "");
        print(w, end = "");
        print(rab, end = "")
    
        temperamentti = temp();
        koulutettavuus = koulu();
    
        print ("Hevonen on yleiseltä tempperamentiltaan ", end = "")
        print(temperamentti, end = "");
        print (" ja koulutettavuudeltaan ", end = "")
        print(koulutettavuus);
        
        print("_____________________________________________________________________ \n")
        
        uusheppa = input("Haluatko uuden hevosen? ")
    
if __name__ == "__main__":
    main()