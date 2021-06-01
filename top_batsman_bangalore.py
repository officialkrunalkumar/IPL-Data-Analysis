from rawdata import deliveries as d
from matplotlib import pyplot as p
from collections import defaultdict as dd


def read_team_data():
    teams = dd(int)
    for data in d:
        if data['batting_team'] == "Royal Challengers Bangalore":
            teams[data['batsman']] += int(data['total_runs'])
    return teams


def plot_graph(teams):
    scoring = sorted(list(teams.values()), reverse=True)[:6]
    players = []
    for number in range(0, 6):
        for data in teams.keys():
            if teams[data] == scoring[number]:
                players.append(data)
    p.figure(figsize=(20, 20))
    p.bar(players, scoring)
    p.xlabel("P l a y e r s")
    p.ylabel("S c o r e s")
    p.title("Top Batsman of Royal Challengers Bangalore")
    p.show()


if __name__ == '__main__':
    teams = read_team_data()
    plot_graph(teams)
