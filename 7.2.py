getallenlijst = input("vul getallen in met telkens een streep er tussen: ")
def analyzer(inputjeofz):

    splitten_sorteren = inputjeofz.split('-')
    splitten_sorteren.sort()

    grootste_getal = max(splitten_sorteren)
    kleinste_getal = min(splitten_sorteren)
    aantal_getallen = len(splitten_sorteren)
    numbers_int = [int(x) for x in splitten_sorteren]
    numbers_sum = sum(numbers_int)
    gemiddelde = numbers_sum / aantal_getallen

    return ('gesorteerde list van ints:' + str(splitten_sorteren) + '\nGrootste getal: ' + str(grootste_getal)
            + '\nKleinste getal: ' + str(kleinste_getal)+ '\nAantal getallen: ' + str(aantal_getallen) + ' en Som van getallen: '  + str(numbers_sum) + '\nGemiddelde: '
            + str(gemiddelde) )











print(analyzer(getallenlijst))