from rawdata import matches as m
import numpy as np
from collections import defaultdict as dd
from matplotlib import pyplot as p


def stacked_chart():
    """
    This function will calculate the number of matches played
    by teams per season. Then using pyplot of matplotlib, it 
    will simply plot the stacked chart.
    """
    teams = dd(int)
    for row in m:
        if row['season'] not in teams:
            teams[row['season']] = dd(int)
            teams[row['season']][row['team1']] = 1
            teams[row['season']][row['team2']] = 1
        else:
            teams[row['season']][row['team1']] += 1
            teams[row['season']][row['team2']] += 1
    seasons = sorted(list(teams.keys()))
    team_names = [
            'Royal Challengers Bangalore',
            'Rising Pune Supergiant',
            'Deccan Chargers',
            'Mumbai Indians',
            'Kochi Tuskers Kerala',
            'Delhi Daredevils',
            'Gujarat Lions',
            'Sunrisers Hyderabad',
            'Rajasthan Royals',
            'Pune Warriors',
            'Kolkata Knight Riders',
            'Chennai Super Kings',
            'Kings XI Punjab',
        ]
    color_ = [
            'red', 'blue', 'green', 'gold', 'brown',
            'mediumpurple', 'orange', 'cyan', 'lime',
            'yellow', 'gainsboro', 'violet', 'black']
    team_play_matches = []
    for team in team_names:
        team_play_match = []
        for year in seasons:
            if year in teams and team in teams[year]:
                team_play_match.append(teams[year][team])
            else:
                team_play_match.append(0)
        team_play_matches.append(team_play_match)
    y = 0
    p.figure(figsize=(20, 10))
    for indx in range(len(color_)):
        if indx > 0:
            p.bar(seasons, team_play_matches[indx],
                  bottom=np.array(y), color=color_[indx])
        else:
            p.bar(seasons, team_play_matches[indx], color=color_[indx])
            y = np.zeros(len(seasons))
        y += np.array(team_play_matches[indx])
    p.xlabel("Y e a r s")
    p.ylabel("Matches Played by Teams")
    p.title("Number of Matches Played by Teams by Season")
    p.legend(team_names, loc='upper right', ncol=2)
    p.show()


if __name__ == "__main__":
    stacked_chart()
