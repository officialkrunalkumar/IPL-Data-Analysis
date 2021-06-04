from rawdata import matches as m
import numpy as np
from collections import defaultdict as dd
from matplotlib import pyplot as plt


def read_csv():
    teams = dd(int)
    for row in m:
        if row['season'] not in teams:
            teams[row['season']] = dd(int)
            teams[row['season']][row['team1']] = 1
            teams[row['season']][row['team2']] = 1
        else:
            teams[row['season']][row['team1']] += 1
            teams[row['season']][row['team2']] += 1
    return teams


def matches_record_lists(teams):
    years = sorted(list(teams.keys()))
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
    team_play_matches = []
    for tm in team_names:
        team_play_matche = []
        for yr in years:
            if yr in teams and tm in teams[yr]:
                team_play_matche.append(teams[yr][tm])
            else:
                team_play_matche.append(0)
        team_play_matches.append(team_play_matche)
    color_ = [
            'red', 'blue', 'green', 'gold', 'lightgray',
            'mediumpurple', 'orange', 'cyan', 'lime',
            'yellow', 'gainsboro', 'violet', 'bisque']
    plt.figure(figsize=(20, 10))
    y = 0
    # Plot the stack bar chart
    for indx in range(len(color_)):

        if indx > 0:
            plt.bar(years, team_play_matches[indx],
                    bottom=np.array(y), color=color_[indx])
        else:
            plt.bar(years, team_play_matches[indx], color=color_[indx])

            # Here, 'y' use as a flag list, in which all values are '0'
            y = np.array([0 for indx in range(len(years))])
        y += np.array(team_play_matches[indx])

    # x-axis and y-axis labels
    plt.xlabel('Years/Season')
    plt.ylabel('Number of matches played by team')

    # Title on bar graph
    plt.title('Matches plyaed by team by season')

    # Legend on right top corner
    plt.legend(team_names, loc='upper right', ncol=2)

    # Function to show the plot
    plt.show()


if __name__ == "__main__":

    teams = read_csv()
    matches_record_lists(teams)
