def kwadraten_som(grondgetallen):
  som = 0
  for getal in grondgetallen:
    if getal > 0:
      som += getal **2
  return som
print(kwadraten_som([4, 3, -5]))

