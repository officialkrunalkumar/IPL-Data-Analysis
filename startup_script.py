import os


def menu():
    """
    This will create a menu based interface on command line.
    It allows you to enter the choice of yours.
    Then it will call the file accordingly.
    """
    print("Welcome to the IPL Analysis and Story Telling Project")
    print("Please choose any one option at a time...")
    print("1. Total Runs scored by team")
    print("2. Top Batsman for Royal Challengers Bangalore")
    print("3. Foreign Umpire Analysis")
    print("4. Number of Games Played per Year")
    print("5. Stacked Chart of Number of games played by teams by seasons")
    choice = int(input("Enter your choice (1-4) :"))
    if choice == 1:
        os.system('python3 total_runs_scored_by_teams.py')
    elif choice == 2:
        os.system('python3 top_batsman_bangalore.py')
    elif choice == 3:
        os.system('python3 foreign_umpire_analysis.py')
    elif choice == 4:
        os.system('python3 matches_per_year.py')
    elif choice == 5:
        os.system('python3 stacked_chart.py')
    else:
        print("")
        rechoice = ord(input("Wrong Choice! do you want to try again? (y/n)"))
        if rechoice == 89 or rechoice == 121:
            os.system('clear')
            menu()
        else:
            print("Thanks for Using IPL Analysis and Story Telling Project")


if __name__ == '__main__':
    menu()
