#! /usr/bin/python
import urllib, itertools, sys, csv

def getRandFromLottery():
    url = "https://data.ny.gov/resource/hsys-3def.csv" #New York lottery win-4
    response = urllib.urlopen(url)
    reader = csv.DictReader(response)           
    l = [reader.next()['Midday Win 4 #'] for _ in range(3)]
    response.close()
    rand = int(''.join(l))
    return rand

def shitutOrderFromRand(rand, ignore):
    vals = {'Sebastian', 'Kyoto', 'Agadir', 'Zozobra', 'Ad Haetzem', 'Meat Bar', 'Joya', 'Pat Qua - Aharoni', 'El Gaucho'}
    vals.remove(ignore)
    permutations = tuple(itertools.permutations(vals,5))
    adjusted = rand % len(permutations)
    return permutations[adjusted]

print shitutOrderFromRand(getRandFromLottery(), sys.argv[1])
