from rawdata import matches as m
from rawdata import umpires as u
from collections import defaultdict as dd
from matplotlib import pyplot as p


def read_umpire():
    """
    This function will ready the umpire data namely 1 and 2.
    Then it will try to calculate number of foreign umpires.
    Then it will return umpire data.
    """
    umpire = dd(int)
    umpires_country = dd(int)
    for data in u:
        umpires_country[data['umpire']] = data[" country"]
    for data in m:
        if data['umpire1']:
            if umpires_country[data['umpire1']] != " India":
                umpire[umpires_country[data['umpire1']]] += 1
            if umpires_country[data['umpire2']] != " India":
                umpire[umpires_country[data['umpire2']]] += 1
    return umpire


def plot_graph(umpire):
    """
    This function is used to plot the graph of countries vs umpire.
    This uses pyplot of matplotlib for plotting.
    """
    countries = list(umpire.keys())
    umpires = list(umpire.values())
    p.figure(figsize=(20, 20))
    p.bar(countries, umpires)
    p.xlabel("C o u n t r i e s")
    p.ylabel("U m p i r e s")
    p.title("Foreign Umpire's Analysis")
    p.show()


if __name__ == '__main__':
    umpire = read_umpire()
    plot_graph(umpire)
