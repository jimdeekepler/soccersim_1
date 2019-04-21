#!/usr/bin/env python
# +encoding: utf8

from __future__ import print_function

import random

# no. of teams
# jeder gegen jeden?
# hin und rückspiel?
# now what?

# spielplan erstellen
# spielplan besteht aus mehreren spieltagen
# spieltag enthält 'begegnungen' oder spiele
# spiel hat: heim, gast, tore heim, tore gast
# nach jedem spieltag wird die tabelle aktualisiert

# ablauf:
# spielplan erstellen
# ... und das geht so: (häh?)
#     -> anzahl der mannschaften muss gerade sein! (TODO:wirklich?)
#     halbiere die mannschaftsliste und nimm die erste hälfte für die
#       heim mannschaften
#     nimm die zweite hälfte für die gast mannschaften (1. spieltag steht)
#     (TODO: wie gehts weiter ???)

# tabelle anzeigen, 1. spieltag anzeigen
# spieltag auswürfeln
# tabelle aktualisieren
# ...
# game over


class mannschaft(object):
    def __init__(self, name):
        self.name = name
        self.punkte = 0
        self.tore = 0

    def __repr__(self):
        pass


class spielplan(object):
    def __init__(self, mannschaften):
        self.mannschaften = mannschaften
        anzSpieltage = len(mannschaften) - 1

        print("bereite %d Spieltage vor" % anzSpieltage)
        self.items = []
        for spieltag_no in range(1, anzSpieltage):
            st = spieltag(spieltag_no, mannschaften)
            self.items.append(st)


class spieltag(object):
    def __init__(self, spieltag_no, mannschaften):
        print("bereite Spieltag %d vor" % (spieltag_no, ))
        self.spiele = []

        modul = len(mannschaften) - 1

        teams = []
        for pos in range(1, len(mannschaften)):
            # k = pos
            # (k + l) % modul == i
            # l = i * modul - k
            if pos in teams:
                continue
            l = (-(pos - spieltag_no) % modul)
            if l <= 0:
                l = modul - l
            if l == pos:
                l = modul + 1

            # print("pos, l, spieltag, (pos+l), modul, (pos+l)%modul")
            # print(pos, l, spieltag_no, (pos+l), modul, (pos+l)%modul )
            assert 0 < pos and pos <= modul
            assert 0 < l and l <= modul + 1
            teams.append(pos)
            teams.append(l)
            # if (pos == l or (pos + l) % modul != spieltag_no):
            #     l = modul + 1
            
            sp = spiel(mannschaften[pos - 1], mannschaften[l - 1])

            # TODO: maybe later?
            sp.spielen()
            self.spiele.append(sp)

        print(self)
        # print(st)
        self.print_and_calc_tabelle()
        print("\n\n\n")

    def print_and_calc_tabelle(self):
        tabelle = []
        for spiel in self.spiele:
            spiel.heim.tore = spiel.heim.tore + spiel.heim_tore - spiel.gast_tore
            spiel.gast.tore = spiel.gast.tore + spiel.gast_tore - spiel.heim_tore
            heim_punkte = gast_punkte = 0
            if spiel.heim_tore == spiel.gast_tore:
                heim_punkte = gast_punkte = 1
            elif spiel.heim_tore > spiel.gast_tore:
                heim_punkte = 3
                gast_punkte = 0
            elif spiel.heim_tore < spiel.gast_tore:
                heim_punkte = 0
                gast_punkte = 3
            else:
                raise runtime_error("impossible state??")
            spiel.heim.punkte = spiel.heim.punkte + heim_punkte
            spiel.gast.punkte = spiel.gast.punkte + gast_punkte
            tabelle.append(spiel.heim)
            tabelle.append(spiel.gast)

        # TODO: sort by punkte desc, anzahl_spiele?
        tabelle.sort(key=lambda x: x.tore, reverse=True)
        tabelle.sort(key=lambda x: x.punkte, reverse=True)
        # print(tabelle)
        pos = 0
        for x in tabelle:
            if pos == 0 or tabelle[pos - 1].tore != x.tore or tabelle[pos - 1].punkte != x.punkte:
                pos += 1
            print("%-3d%-25s\t%2d\t%2d" % (pos, x.name, x.tore, x.punkte))

    def __repr__(self):
        return "\n".join(map(str, self.spiele))


class spiel(object):
    def __init__(self, heim, gast):
        self.heim = heim
        self.heim_tore = 0
        self.gast = gast
        self.gast_tore = 0

    def spielen(self):
        self.heim_tore = random.randint(0,6)
        self.gast_tore = random.randint(0,6)

    def __repr__(self):
        return "%-28s : %-28s %2d : %2d" % (self.heim.name[:28], self.gast.name[:28],
                self.heim_tore, self.gast_tore)


def main():
    mannschafts_namen = ["Spvgg. Dettingen", "FC Bayern Rurpolding",
            "SG Eintracht Münzenberg", "VfB Ulm Süd",
            "Türk Güći Ingolstadt", "SV Unterhaching",
            "Rot-Weiss Bad Arolsen", "Preussen Chemnitz",
            "Union Wenigerode", "Werder Langenhagen"]
    random.shuffle(mannschafts_namen)
    mannschaften = []
    for name in mannschafts_namen:
        mannschaften.append(mannschaft(name))

    x = spielplan(mannschaften)
    # Test:
    print("Finished")


if __name__ == "__main__":
    main()


