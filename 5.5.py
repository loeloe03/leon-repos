grondgetallen = [1,2,3,-4,5,-2,7,8,9,-3]


def kwadraten_som(grondgetallen):
    for pos in grondgetallen:
        if pos > 0:
            return grondgetallen

uitkomst = (kwadraten_som(grondgetallen)) **2
print(uitkomst)--