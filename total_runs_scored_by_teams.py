from rawdata import deliveries as d
from collections import defaultdict as dd
from matplotlib import pyplot as p


def read_team_score():
    teams = dd(int)
    for data in d:
        teams[data["batting_team"]] += int(data["total_runs"])
    return teams


def plot_graph(teams):
    x = list(teams.keys())
    y = list(teams.values())
    p.figure(figsize=(15, 10))
    p.barh(x, y)
    p.xlabel("S c o r e s")
    p.ylabel("T e a m s")
    p.title("Total Runs Scored by Teams")
    p.show()


if __name__ == '__main__':
    teams = read_team_score()
    plot_graph(teams)
