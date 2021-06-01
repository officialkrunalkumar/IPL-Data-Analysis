from rawdata import matches as m
from collections import OrderedDict as od
from matplotlib import pyplot as p


def matches_per_year():
    matches_played = {}
    for match in m:
        if match['season'] in matches_played:
            matches_played[match['season']] += 1
        else:
            matches_played[match['season']] = 1
    matches_played = od(sorted(matches_played.items(), key=lambda x: x[0]))
    return matches_played


def plot_graph(matches_played):
    p.title("Number of Matches Played Per Year")
    p.xlabel("Y e a r s")
    p.ylabel("M a t c h e s")
    x = matches_played.keys()
    y = matches_played.values()
    p.bar(x, y)
    p.show()


if __name__ == '__main__':
    matches_played = matches_per_year()
    plot_graph(matches_played)
