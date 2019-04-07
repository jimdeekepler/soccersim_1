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
        ## self.anzSpieltage = int(len(mannschaften) / 2)
        anzSpieltage = int(len(mannschaften) / 2)

        print("bereite %d Spieltage vor" % anzSpieltage)
        heim_mannschaften = mannschaften[0:anzSpieltage]
        gast_mannschaften = mannschaften[anzSpieltage:]
        self.items = []
        for i in range(anzSpieltage):
            st = spieltag(heim_mannschaften, gast_mannschaften)
            self.items.append(st)
            team = gast_mannschaften.pop(0)
            gast_mannschaften.append(team)


class spieltag(object):
    def __init__(self, heim_mannschaften, gast_mannschaften):
        print("len a: %d  len b: %d" % (len(heim_mannschaften), len(gast_mannschaften)))
        assert len(heim_mannschaften) == len(gast_mannschaften)
        self.spiele = []
        # print(median)
        # print(heimmannschaften)
        # print(gastmannschaften)
        for pos in range(len(heim_mannschaften)):
            sp = spiel(heim_mannschaften[pos], gast_mannschaften[pos])

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
            spiel.heim.tore = spiel.heim.tore + spiel.heim_tore
            spiel.gast.tore = spiel.gast.tore + spiel.gast_tore
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
        print("Partie: %s, %s" % (heim.name, gast.name))  # TODO: alt use __str__ on
                                                             # mannschaft
        self.heim = heim
        self.heim_tore = 0
        self.gast = gast
        self.gast_tore = 0

    def spielen(self):
        self.heim_tore = random.randint(0,6)
        self.gast_tore = random.randint(0,6)

    def __repr__(self):
        return "%-20s : %-20s %2d : %2d" % (self.heim.name, self.gast.name,
                self.heim_tore, self.gast_tore)


def main():
    mannschafts_namen = ["Spvgg. Dettingen", "FC Bayern Rurpolding",
            "SG Eintracht Münzenberg", "VfB Ulm Süd",
            "Türk Güći Ingolstadt", "SV Unterhaching",
            "Rot-Weiss Bad Arolsen", "Preussen Chemnitz",
            "Union Wenigerode", "Werder Langenhagen"]
    mannschaften = []
    for name in mannschafts_namen:
        mannschaften.append(mannschaft(name))

    x = spielplan(mannschaften)
    # Test:
    print("Finished")


if __name__ == "__main__":
    main()


