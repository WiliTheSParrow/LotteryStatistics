#   -----------------
# |  HAZI FELADAT II. |
#   -----------------

# Hatos lotto statisztika. Nincs helyes megoldas a 7. szám miatt, amirol mi dontjuk el hogyan dolgozzuk fel.
# Oszloponkent nezzuk a 6 legnagyobb szamot, plusz a Jokert (olyan, mintha lett volna egy hetedik sorsolás).

import csv
from collections import Counter

csv.register_dialect("dialekt", delimiter=';')

with open('hatos.csv', encoding="utf-8", newline='') as fajl:
    csvolvas = csv.reader(fajl, dialect='dialekt')

    elso = []
    masodik = []
    harmadik = []
    negyedik = []
    otodik = []
    hatodik = [] # Ures lista a hatodik szamnak
    joker = [] # Ures lista a joker szamnak

    for sor in csvolvas:

        if len(sor) == 19: # Ha csak 6 szamot sorsoltak, a csv file egy sora 19 tagu.
            elso.append(sor[-6])
            masodik.append(sor[-5])
            harmadik.append(sor[-4])
            negyedik.append(sor[-3])
            otodik.append(sor[-2])
            hatodik.append(sor[-1])

        if len(sor) == 20:
            elso.append(sor[-7]) # Ha sorsoltak Joker szamot is, a csv file egy sora 20 tagu.
            masodik.append(sor[-6])
            harmadik.append(sor[-5])
            negyedik.append(sor[-4])
            otodik.append(sor[-3])
            hatodik.append(sor[-2])
            joker.append(sor[-1])

            if joker[-1] == '': # Abban az esetben, ha a 7.(Joker) szam ures, pop fgv-el kiszedjuk es nem szamolodik bele.
                joker.pop()

sz1 = Counter(elso)
sz2 = Counter(masodik)
sz3 = Counter(harmadik)
sz4 = Counter(negyedik)
sz5 = Counter(otodik)
sz6 = Counter(hatodik)
szj = Counter(joker)

print(sz1.most_common(1)[0][0] +
      ", " +
      sz2.most_common(1)[0][0] +
      ", " +
      sz3.most_common(1)[0][0] +
      ", " +
      sz4.most_common(1)[0][0] +
      ", " +
      sz5.most_common(1)[0][0] +
      ", " +
      sz6.most_common(1)[0][0] +
      ", A leggyakrabban kisorsolt joker szam: " +
      szj.most_common(1)[0][0])

input(' ')