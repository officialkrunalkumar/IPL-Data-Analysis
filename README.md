# IPL Data Analysis

IPL Data collected from Kaggle and analysis is made using Python's functionality to create a story telling scenario.

### Mountblue's first project using python's matplotlib

Run `Setup.sh` file to make the project RUN.

setup shell script will first try to check whether virtual environment exists or not.

if it is already exists, then it will activate it.
otherwise, it will create virtual environment first and then initialize it.

Once, virtual environment is created, it will try to install the requirements.

then, if all goes well, it will call the `startup_script.py` python script.

It will give you a menu, where you can enter your choice and get the output.

few things, about files...

1) `rawdata.py` :-  It is the base file which reads the data from csv using DictReader (Dictionary Reader).
2) `startup_script.py` :- It will present Menu, and allow you to enter your choice.
3) `total_runs_scored_by_teams.py` :- This file will draw a graph using pyplot runs made by team vs years in IPL.
4) `top_batsman_bangalore.py` :- This will graph the players vs their scores from Royal Challengers Bangalore.
5) `foreign_umpire_analysis.py` :- It will give the analytical graph which shows the analysis of foreign umpires.
6) `matches_per_year.py` :- It graphs the number of matches played per year.
7) `matches.csv` :- It contains the data of matches.
8) `deliveries.csv` :- It contains the data of players and scores.
9) `umpires.csv` :- It contains the umpire related data.