import datetime

nu = datetime.datetime.today()
s = nu.strftime("%a %d %b %Y, %H:%M:%S")
naam = input('Wat is je naam? ')

outfile = open('pe_6_4_hardlopers.txt', 'a')
outfile.write('{}, {}\n'.format(s, naam))
outfile.close()
