from csv import DictReader as d

matches = d(open('matches.csv'))
deliveries = d(open('deliveries.csv'))
umpires = d(open('umpires.csv'))
