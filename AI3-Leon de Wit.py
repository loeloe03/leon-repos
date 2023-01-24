#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Oriëntatie op AI

Final assignment 3: statistiek

(c) 2019 Hogeschool Utrecht,
Bart van Eijkelenburg en
Tijmen Muller (tijmen.muller@hu.nl)

Opdracht:
Werk onderstaande functies uit. Elke functie krijgt een niet-lege en
ongesorteerde lijst *lst* met gehele getallen (int) als argument.
Voeg commentaar toe om je code toe te lichten.

Je kunt je functies testen met het gegeven raamwerk door het bestand
uit te voeren (of met behulp van `pytest`, als je weet hoe dat werkt).
Lever je werk in op Canvas als alle tests slagen.

Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""

# TODO: Vul hier je naam, klas en studentnummer in.
naam = "Leon"
klas = "V1P"
studentnummer = 1838291


def mean(lst):
    #Het gemiddelde bereken ik door alle resultaten in de lijst op te tellen en vervolgens te delen door het aantal getallen van de lijst.
    return sum(lst) / len(lst)


def rnge(lst):
    #Het bereik van lijst berekeken ik door het grootste getalen van de lijst af te trekken van het kleinste getal van lijst.
    return max(lst) - min(lst)


def median(lst):
    #Om de mediaan te berekenen moeten we eerst controleren of het middelste getal even is. 
    #Dit doe ik door de lijst te sorteren en daarna de lengte van de lijst te delen door twee en te controleren wat er overblijft. Als hier 0 uitkomst weten we dat de lijst een oneven aantal getallen heeft.
    lst.sort()
    
    if len(lst) % 2 != 0:
        # Als de lijst even is return ik het middelste getal.
        
        # Dan berekenen we weer de lengte van de lijst + 1. Vervolgens delen we die door 2 en trekken we er nog 1 vanaf. Omdat we vanaf nul tellen. Dan komen we op het middelste getal uit.
        #De positie van de lijst is dan het middelste getal.
        mediaan = int((len(lst) + 1) / 2 -1)
        return float(lst[mediaan])
    else:
        #Als de lijst een even getal is berekenen we het gemiddelde van de twee middelste getallen.
        #Eerste middelste getal definiëren. Lengte van de lijst / 2 + 1 
        getal_1 = int(len(lst) / 2 - 1)
        
        #Tweede middelste getal definiëren.
        getal_2 = int(len(lst) / 2)
        
        # We gebruiken de positie in de lijst van de middelste getallen en tellen deze op, vervolgens delen we deze door 2. Het gemiddelde returnen we.
        return float((lst[getal_1] + lst[getal_2]) / 2)

def q1(lst):
    # Het eerste kwartiel is de mediaan van de getallen die kleiner zijn dan de mediaan
    
    # Hier kijken we wat de eerste kwartiel is
    
    # Dat doen we door de mediaan te pakken en dan alle getallen die kleiner zijn dan de mediaan te pakken
    mediaan = median(lst)

    # We maken een nieuwe lijst aan met alle getallen die kleiner zijn dan de mediaan
    new_list = []
    
    if len(lst) % 2 == 0:
        numbers = int(len(lst) / 2)
        return median(lst[:numbers])
    else:
        numbers = len(lst) // 2
        return median(lst[:numbers])


def q3(lst):
    # Het derde kwartiel is hetzelfde als het eerste kwartiel alleen dan met de getallen die groter zijn dan de mediaan
    
    # Hier kijken we wat de derde kwartiel is
    
    # Dat doen we door de mediaan te pakken en dan alle getallen die groter zijn dan de mediaan te pakken
    mediaan = median(lst)
    
    # We maken een nieuwe lijst aan met alle getallen die groter zijn dan de mediaan
    new_list = [nummer for nummer in lst if nummer > mediaan]
    return median(new_list)

def var(lst):
    # Een variantie is de afwijking van de getallen bij elkaar opgeteld
    # Een afwijking is het getal min het gemiddelde
    
    # Hier kijken we wat de variantie is
    # Dat doen we door de afwijkingen van de getallen bij elkaar op te tellen en te delen door het aantal getallen
    # De afwijkingen zijn de getallen die je van het gemiddelde afhaalt
    # De variantie is de afwijkingen bij elkaar opgeteld

    # We pakken de lengte van de lijst
    lengte = len(lst)

    # We pakken het gemiddelde
    gemiddelde = mean(lst)

    # We maken een lege lijst aan
    afwijkingen = []
    
    # We pakken alle getallen uit de lijst
    for nummer in lst:
        # We pakken het getal en trekken daar het gemiddelde vanaf en dan pakken we het kwadraat van dat getal
        # En dat voegen we toe aan de lijst met afwijkingen
        afwijkingen.append((nummer - gemiddelde) ** 2)

    # Hier berekenen we de variantie
    # Door de afwijkingen bij elkaar op te tellen en te delen door het aantal getallen
    variantie = sum(afwijkingen) / lengte
    return variantie


def std(lst):
    # Een standaardafwijking is de wortel van de variantie

    # Hier kijken we wat de standaardafwijking is
    
    # Dat doen we door de variantie te pakken en die te wortelen
    variantie = var(lst)
    
    # We pakken de wortel door de variantie te machtsverheffen met 0.5 
    return variantie ** 0.5


def freq(lst):
    # Een frequentie is hoe vaak een getal voorkomt
    
    # Hier kijken we wat de frequentie is
    # Dat doen we door de getallen bij elkaar op te tellen en te delen door het aantal getallen
    
    # Maak een lege dictionary aan
    freqs = {}

    # Loop over alle getallen in de lijst
    for num in lst:
        
        # Kijk of het getal al in de dictionary zit
        if num in freqs:
            # Als het getal al in de lijst zit dan voegen we er 1 bij op
            freqs[num] += 1
        else:
            # Als het getal nog niet in de lijst zit dan voegen we het toe
            freqs[num] = 1
    return freqs


def modes(lst):
    # De modus is het getal dat het meest voorkomt
    
    # Hier kijken we wat de modus is
    # Dat doen we door te kijken welk getal het meest voorkomt

    # Hier pakken we de frequentie van de getallen
    counts = freq(lst)


    # Hier kijken we welk getal het meest voorkomt
    max_count = max(counts.values())
        
    # Hier kijken we welke getallen het meest voorkomen    

    # Maak een lege lijst aan
    modes = []
    
    # Loop over alle getallen in de lijst
    for number in counts:

        # Als het getal even vaak voorkomt als de max_count dan voegen we het toe aan de modes lijst
        if counts[number] == max_count:
            modes.append(number)
    return sorted(modes)


"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
import os
import sys

def __my_assert_args(function, args, expected_output, check_type=True):
    """
    Controleer of gegeven functie met gegeven argumenten het verwachte resultaat oplevert.
    Optioneel wordt ook het return-type gecontroleerd.
    """
    argstr = str(args).replace(',)', ')')
    output = function(*args)

    # Controleer eerst het return-type (optioneel)
    if check_type:
        msg = f"Fout: {function.__name__}{argstr} geeft geen {type(expected_output)} terug als return-type"
        assert type(output) is type(expected_output), msg

    # Controleer of de functie-uitvoer overeenkomt met de gewenste uitvoer
    msg = f"Fout: {function.__name__}{argstr} geeft {output} in plaats van {expected_output}"
    if type(expected_output) is float:
        # Vergelijk bij float als return-type op 7 decimalen om afrondingsfouten te omzeilen
        assert round(output - expected_output, 7) == 0, msg
    else:
        assert output == expected_output, msg


def test_id():
    assert naam != "", "Je moet je naam nog invullen!"
    assert studentnummer != -1, "Je moet je studentnummer nog invullen!"
    assert klas != "", "Je moet je klas nog invullen!"


def test_mean():
    testcases = [
        (([4, 2, 5, 8, 6],), 5.0),
        (([1, 3, 2, 4, 6, 2, 4, 2],), 3.0)
    ]

    for case in testcases:
        __my_assert_args(mean, case[0], case[1])


def test_mean_simulated():
    import random
    import statistics

    for lst_size in range(1, 11):
        lst_test = [random.choice(range(5)) for _ in range(lst_size)]
        __my_assert_args(mean, (lst_test,), statistics.mean(lst_test), False)


def test_rnge():
    testcases = [
        (([4, 2, 5, 8, 6],), 6),
        (([1, 3, 2, 4, 6, 2, 4, 2],), 5)
    ]

    for case in testcases:
        __my_assert_args(rnge, case[0], case[1])


def test_median():
    testcases = [
        (([4, 2, 5, 8, 6],), 5.0),
        (([1, 3, 4, 6, 4, 2],), 3.5),
        (([1, 3, 4, 6, 2, 4, 2],), 3.0),
        (([1, 3, 2, 4, 6, 2, 4, 2],), 2.5)
    ]

    for case in testcases:
        __my_assert_args(median, case[0], case[1])


def test_median_simulated():
    import random
    import statistics

    for lst_size in range(1, 11):
        lst_test = [random.choice(range(5)) for _ in range(lst_size)]
        __my_assert_args(median, (lst_test,), statistics.median(lst_test), False)


def test_q1():
    testcases = [
        (([4, 2, 5, 8, 6],), 3.0),
        (([1,2,4,4,5,6],), 2.0),
        (([1, 3, 4, 6, 4, 2],), 2.0),
        (([1, 3, 5, 6, 1, 4, 2],), 1.0),
        (([5, 7, 4, 4, 6, 2, 8],), 4.0),
        (([0, 5, 5, 6, 7, 7, 12],), 5.0),
        (([1, 4, 3, 5, 6, 2, 4, 1],), 1.5),
        (([3, 5, 7, 8, 9, 11, 15, 16, 20, 21],), 7.0),
        (([1, 2, 5, 6, 7, 9, 12, 15, 18, 19, 27],), 5.0)

    ]

    for case in testcases:
        __my_assert_args(q1, case[0], case[1])


def test_q3():
    testcases = [
        (([4, 2, 5, 8, 6],), 7.0),
        (([1, 3, 4, 6, 4, 2],), 4.0),
        (([1, 3, 5, 6, 2, 4, 1],), 5.0),
        (([5, 7, 4, 4, 6, 2, 8],), 7.0),
        (([0, 5, 5, 6, 7, 7, 12],), 7.0),
        (([1, 4, 3, 5, 6, 2, 4, 1],), 4.5),
        (([3, 5, 7, 8, 9, 11, 15, 16, 20, 21],), 16.0),
        (([1, 2, 5, 6, 7, 9, 12, 15, 18, 19, 27],), 18.0)

    ]

    for case in testcases:
        __my_assert_args(q3, case[0], case[1])


def test_var():
    testcases = [
        (([4, 2, 5, 8, 6],), 4.0),
        (([1, 3, 2, 4, 6, 2, 4, 2],), 2.25)
    ]

    for case in testcases:
        __my_assert_args(var, case[0], case[1])


def test_var_simulated():
    import random
    import statistics

    for lst_size in range(1, 11):
        lst_test = [random.choice(range(5)) for _ in range(lst_size)]
        __my_assert_args(var, (lst_test,), statistics.pvariance(lst_test), False)


def test_std():
    testcases = [
        (([4, 2, 5, 8, 6],), 2.0),
        (([1, 3, 2, 4, 6, 2, 4, 2],), 1.5)
    ]

    for case in testcases:
        __my_assert_args(std, case[0], case[1])


def test_std_simulated():
    import random
    import statistics

    for lst_size in range(1, 11):
        lst_test = [random.choice(range(5)) for _ in range(lst_size)]
        __my_assert_args(std, (lst_test,), statistics.pstdev(lst_test), False)


def test_freq():
    testcases = [
        (([4, 2, 5, 8, 6],), {2: 1, 4: 1, 5: 1, 6: 1, 8: 1}),
        (([1, 3, 4, 6, 4, 2],), {1: 1, 2: 1, 3: 1, 4: 2, 6: 1}),
        (([1, 3, 5, 6, 2, 4, 1],), {1: 2, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}),
        (([1, 4, 3, 5, 6, 2, 4, 1],), {1: 2, 2: 1, 3: 1, 4: 2, 5: 1, 6: 1})
    ]

    for case in testcases:
        __my_assert_args(freq, case[0], case[1])


def test_modes():
    testcases = [
        (([4, 2, 5, 8, 6],), [2, 4, 5, 6, 8]),
        (([1, 3, 4, 6, 4, 2],), [4]),
        (([1, 3, 4, 6, 2, 4, 2],), [2, 4]),
        (([1, 3, 2, 4, 6, 2, 4, 2],), [2])
    ]

    for case in testcases:
        __my_assert_args(modes, case[0], case[1])

def test_modes_simulated():
    if sys.version_info[0] >= 3 and sys.version_info[1] >= 8:
        import random
        import statistics
        for lst_size in range(1, 11):
            lst_test = [random.choice(range(5)) for _ in range(lst_size)]
            __my_assert_args(modes, (lst_test,), sorted(statistics.multimode(lst_test)))


def __main():
    """ Test alle functies. """
    # Noodzakelijk voor gekleurde tekst binnen een Windows terminal
    os.system("")

    try:
        print("\x1b[32m")   # Groene tekstkleur
        test_id()

        test_mean()
        test_mean_simulated()
        print("Je functie mean(lst) werkt goed!")

        test_rnge()
        print("Je functie rnge(lst) werkt goed!")

        test_median()
        test_median_simulated()
        print("Je functie median(lst) werkt goed!")

        test_q1()
        print("Je functie q1(lst) werkt goed!")

        test_q3()
        print("Je functie q3(lst) werkt goed!")

        test_var()
        test_var_simulated()
        print("Je functie var(lst) werkt goed!")

        test_std()
        test_std_simulated()
        print("Je functie std(lst) werkt goed!")

        test_freq()
        print("Je functie freq(lst) werkt goed!")

        test_modes()
        test_modes_simulated()
        print("Je functie modes(lst) werkt goed!")

        print("\nGefeliciteerd, alles lijkt te werken!")
        print("Lever je werk nu in op Canvas...")

        def hist(freqs):
            v_min = min(freqs.keys())
            v_max = max(freqs.keys())

            histo = str()
            for i in range(v_min, v_max + 1):
                histo += "{:5d} ".format(i)
                if i in freqs.keys():
                    histo += "█" * freqs[i]
                histo += '\n'

            return histo

        print("\x1b[0m")
        s = input("Geef een reeks van gehele getallen (gescheiden door een spatie): ")
        userlst = [int(c) for c in s.split()]

        print("\nHet gemiddelde is {:.2f}".format(mean(userlst)))
        print("De modi zijn {}".format(modes(userlst)))
        print("De mediaan is {:.2f}".format(median(userlst)))
        print("Q1 is {:.2f}".format(q1(userlst)))
        print("Q3 is {:.2f}".format(q3(userlst)))

        print("Het bereik is {}".format(rnge(userlst)))
        print("De variantie is {:.2f}".format(var(userlst)))
        print("De standaardafwijking is {:.2f}".format(std(userlst)))

        print("\nHistogram (gekanteld):\n\n" + hist(freq(userlst)))

    except AssertionError as ae:
        print("\x1b[31m")   # Rode tekstkleur
        if not ae:
            print("Je code veroorzaakt onderstaande AssertionError:")
            raise ae
        else:
            print(ae)

    print("\x1b[0m")    # Reset tekstkleur


if __name__ == '__main__':
    __main()