from tabulate import tabulate
import os
import sys
import maskpass

# A dictionary to store user accounts (username: password)
accounts = {"admin": "admin",
            "user": "user"}

# Initial data
players = [
    {"id": 1, "name": "Haaland", "position": "ST", "rating": 91, "price": 2300000, "stock": 1,
     "nation": "Norway", "team": "Manchester City", "league": "Premier League"},
    {"id": 2, "name": "Mbappé", "position": "ST", "rating": 90, "price": 2100000, "stock": 1,
     "nation": "France", "team": "Real Madrid", "league": "La Liga"},
    {"id": 3, "name": "Bellingham", "position": "CM", "rating": 88, "price": 1200000, "stock": 2,
     "nation": "England", "team": "Real Madrid", "league": "La Liga"},
    {"id": 4, "name": "Vinícius", "position": "LW", "rating": 89, "price": 1500000, "stock": 2,
     "nation": "Brazil", "team": "Real Madrid", "league": "La Liga"},
    {"id": 5, "name": "De Bruyne", "position": "CAM", "rating": 91, "price": 1800000, "stock": 1,
     "nation": "Belgium", "team": "Manchester City", "league": "Premier League"},
    {"id": 6, "name": "Salah", "position": "RW", "rating": 89, "price": 1600000, "stock": 2,
     "nation": "Egypt", "team": "Liverpool", "league": "Premier League"},
    {"id": 7, "name": "Rodri", "position": "CDM", "rating": 89, "price": 900000, "stock": 3,
     "nation": "Spain", "team": "Manchester City", "league": "Premier League"},
    {"id": 8, "name": "Valverde", "position": "CM", "rating": 88, "price": 1100000, "stock": 2,
     "nation": "Uruguay", "team": "Real Madrid", "league": "La Liga"},
    {"id": 9, "name": "Bernardo", "position": "CAM", "rating": 88, "price": 1000000, "stock": 2,
     "nation": "Portugal", "team": "Manchester City", "league": "Premier League"},
    {"id": 10, "name": "Kane", "position": "ST", "rating": 90, "price": 1400000, "stock": 1,
     "nation": "England", "team": "Bayern Munich", "league": "Bundesliga"}
]

NATIONS = ["England","Spain","Germany","Italy","France","Portugal","Netherlands","Argentina","Brazil","Belgium"]

LEAGUES = ['Premier League', 'La Liga', 'Bundesliga', 'Serie A', 'Ligue 1', 'Liga Portugal', 'Eredivisie', 'Liga Profesional', 'Brasileirão', 'Pro League']

POSITIONS = ['GK', 'LB', 'CB', 'RB','RWB','LWB','CAM','CDM','CM','RM','LM','ST','RW','LW']

CLUBS = {
    "Premier League": [
        "Arsenal",
        "Chelsea",
        "Liverpool",
        "Manchester City",
        "Manchester United",
        "Tottenham"
    ],
    "La Liga": [
        "Atletico Madrid",
        "Barcelona",
        "Real Madrid",
        "Sevilla",
        "Valencia",
        "Villarreal"
    ],
    "Bundesliga": [
        "Bayern Munich",
        "Borussia Dortmund",
        "RB Leipzig",
        "Bayer Leverkusen",
        "Wolfsburg",
        "Frankfurt"
    ],
    "Serie A": [
        "AC Milan",
        "Inter Milan",
        "Juventus",
        "Napoli",
        "Roma",
        "Lazio"
    ],
    "Ligue 1": [
        "PSG",
        "Lyon",
        "Marseille",
        "Monaco",
        "Lille",
        "Nice"
    ],
    "Liga Portugal": [
        "Benfica",
        "Porto",
        "Sporting CP",
        "Braga",
        "Vitoria",
        "Guimaraes"
    ],
    "Eredivisie": [
        "Ajax",
        "PSV",
        "Feyenoord",
        "AZ Alkmaar",
        "Utrecht",
        "Twente"
    ],
    "Liga Profesional": [
        "Boca Juniors",
        "River Plate",
        "Racing Club",
        "Independiente",
        "San Lorenzo",
        "Velez Sarsfield"
    ],
    "Brasileirão": [
        "Flamengo",
        "Palmeiras",
        "Santos",
        "São Paulo",
        "Corinthians",
        "Internacional"
    ],
    "Pro League": [
        "Club Brugge",
        "Anderlecht",
        "Standard Liege",
        "Gent",
        "Genk",
        "Antwerp"
    ]
}

# List to store bought players
my_players = []

def create_account():
    """Create a new user account."""
    print("\n--- Create Account ---")
    username = input("Enter a username: ").strip()
    
    if username in accounts:
        print("Error: Username already exists. Try again.")
        return

    password = maskpass.advpass("Enter a password: ")
    confirm_password = maskpass.advpass("Confirm your password: ")
    
    if password != confirm_password:
        print("Error: Passwords do not match. Try again.")
        return

    accounts[username] = password
    print("Account created successfully!")

def login():
    os.system('cls')
    """Log in Menu"""
    username = input("Enter your username: ").strip()
    password = maskpass.advpass("Enter your password: ")

    while True:
        if len(username)==0 and len(password)==0:
            print("Error: Username and password cannot be empty.")
            break
        elif username in accounts and accounts[username] == password and accounts[username] == "admin":
            os.system('cls')
            print(f"Welcome, {username}! You are logged in as an admin.")
            menu()
        elif username in accounts and accounts[username] == password and accounts[username] != "admin":
            os.system('cls')
            print(f"Welcome, {username}! You are logged in as a user.")
            user_menu()
        else:
            print("Error: Invalid username or password.")
            break

# Function to display Menu
def display_menu():
    print("\n--- Player Management System ---")
    print("1. Read Player")
    print("2. Create Player")
    print("3. Update Player")
    print("4. Delete Player")
    print("5. Exit")

def read_menu():
    print("1. Display Player")
    print("2. Search Player")
    print("3. Back")

def user_display_menu():
    print("\n--- User Menu ---")
    print("1. View My Players")
    print("2. Buy Player")
    print("3. Exit")

# Function to read/get a player by ID
def get_player(player_id):
    for player in players:
        if player["id"] == player_id:
            return player
    return None

def display_options(field, header):
    """Displays a numbered list of options with a header."""
    print(f"\nAvailable {header}:")
    field_list = []
    for i, fld in enumerate(field):
        number = str(i + 1)
        field_list.append([number, fld])
    print(tabulate(field_list, headers=["No.", header], tablefmt="pretty"))

def get_choice(i, opt, custom=False, txt="Enter custom value: "):
    while True:
        try:
            choice = int(input(i))
            if 1 <= choice <= len(opt):
                return opt[choice - 1]
            elif custom and choice == len(opt) + 1:
                custom_value = input(f"{txt}: ").strip()
                if len(custom_value) > 0 and all(c.isalnum() or c.isspace() for c in custom_value):
                    return custom_value
                else:
                    print("Invalid Input : Please enter a valid value (cannot be empty and must be alphanumeric).")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")

def get_numeric_input(i, min=None, max=None):
    while True:
        try:
            val = int(input(i))
            if (min is None or val >= min) and (max is None or val <= max):
                return val
            print(f"Value must be between {min} and {max}.")
        except ValueError:
            print("Please enter a valid number.")

# Function to display all players in a table format
def display_players():
        if players:
            print("\n--- All Players ---")
            print(tabulate(players, headers="keys", tablefmt="fancy_grid"))
        else:
            print("No Data Avalaible\n")

# Function to search players by id/name
def search_player():
    if players:
        try : 
            player_id = int(input("Enter player ID: "))
            player = get_player(player_id)
            if player is None:  # Check if player was not found
                print("ID is not found / Invalid")
            else:
                print(tabulate([player.values()], headers=player.keys(), tablefmt="fancy_grid"))
        except ValueError:
            print("You must enter an integer for the player ID.")
    else : 
        print("No Data Available\n")
    
# Function to display bought players
def display_my_players():
    print("\n--- My Players ---")
    if my_players:
        simplified_my_players = [{"name": player["name"],"position" : player["position"] ,"rating": player["rating"], "nation":player["nation"],  "team":player["team"], "league":player["league"]} for player in my_players]
        print(tabulate(simplified_my_players, headers="keys", tablefmt="fancy_grid"))
    else:
        print("You have not bought any players yet.")

# Function to create players
def add_data():
    while True:
        player_id = get_numeric_input("Enter player ID: ")
        if any(player["id"] == player_id for player in players):
            print(f"ID {player_id} already exists.")
            break
        
        while True:
            name = input("Enter player name: ").strip()
            if name and all(c.isalnum() or c.isspace() for c in name):
                break
            print("Name cannot be empty.")
             

        display_options(POSITIONS, "Positions")
        position = get_choice("Choose Position number: ", POSITIONS)

        rating = get_numeric_input("Enter player rating (1-99): ", 1, 99)
        price = get_numeric_input("Enter player price: ", 1)
        stock = get_numeric_input("Enter stock: ", 1)

        display_options(NATIONS + ["Custom"], "Nations")
        nation = get_choice("Choose nation number: ", NATIONS, custom=True)

        display_options(LEAGUES + ["Custom"], "Leagues")
        league = get_choice("Choose League number: ", LEAGUES, custom=True)

        if league in CLUBS:
            display_options(CLUBS[league] + ["Custom"], "Clubs")
            team = get_choice("Choose club number: ", CLUBS[league], custom=True)
        else:
            while True : 
                team = input("Enter custom club: ").strip()
                if len(team.strip()) > 0 and all(t.isalnum() or t.isspace() for t in team):
                    break
                print("Invalid Input : Please enter a valid value (cannot be empty and must be alphanumeric).")


        player_data = {
            "id": player_id,
            "name": name,
            "position": position,
            "rating": rating,
            "price": price,
            "stock": stock,
            "nation": nation,
            "team": team,
            "league": league
        }

        save_choice = input("Do you want to save the data? (yes/no): ").strip().lower()
        if save_choice == 'yes':
            players.append(player_data)
            print(f"\nPlayer {name} added successfully.")
        else:
            print("Data was not saved.")
        break

# Function for updating players    
def update_player():
    while True:
        player_id = get_numeric_input("Enter player ID to update: ")
        player = get_player(player_id)
        if not player:
            print("The data you are looking for does not exist.")
            continue

        print("\nCurrent data for the player:")
        print(tabulate([player.values()], headers=player.keys(), tablefmt="fancy_grid"))

        if input("Do you want to continue with the update? (yes/no): ").strip().lower() != 'yes':
            break

        field = input("Enter the name of the field you want to update: ").strip().lower()
        if field not in player:
            print("Invalid field name. Please try again.")
            continue

        if field in ["rating", "price", "stock"]:
            new_value = get_numeric_input(f"Enter new value for {field}: ", 1, 99 if field == "rating" else None)

        elif field == "position":
            display_options(POSITIONS, "Positions")
            new_value = get_choice("Choose Position number: ", POSITIONS)

        elif field == "nation":
            display_options(NATIONS + ["Custom"], "Nations")
            new_value = get_choice("Choose nation number: ", NATIONS, custom=True)
       
        elif field == "league":
            display_options(LEAGUES + ["Custom"], "Leagues")
            new_value = get_choice("Choose League number: ", LEAGUES, custom=True)
            if new_value in CLUBS:
                display_options(CLUBS[new_value] + ["Custom"], "Clubs")
                player['team'] = get_choice("Choose club number: ", CLUBS[new_value], custom=True)
            else:
                while True:
                    player['team'] = input("Enter custom club: ").strip()
                    if len(player["team"].strip()) > 0 and all(p.isalnum() or p.isspace() for p in player["team"]):
                        break
                    print("Invalid Input : Please enter a valid value (cannot be empty and must be alphanumeric).")

        elif field == "team":
            if player["league"] in CLUBS:
                display_options(CLUBS[player["league"]] + ["Custom"], "Clubs")
                new_value = get_choice("Choose new club number: ", CLUBS[player["league"]], custom=True)
            else:
                new_value = input("Enter new team: ").strip()
                while True :
                    if len(new_value.strip()) > 0 and all(n.isalnum() or n.isspace() for n in new_value):
                        break
                    print("Invalid Input : Please enter a valid value (cannot be empty and must be alphanumeric).")
        elif field == "name":
            while True:
                new_value = input("Enter player name: ").strip()
                if new_value and all(n.isalnum() or n.isspace() for n in new_value):
                    break
                print("Invalid Input : Please enter a valid value (cannot be empty and must be alphanumeric).")
        else:
            print("Invalid field name.")
            continue

        # Confirm update
        if input("Do you want to save this update? (yes/no): ").strip().lower() == 'yes':
            player[field] = new_value
            print("Data successfully updated.")
        else:
            print("Update canceled.")
        break


# Function to delete a player by ID
def delete_player():
    while True:
        try:
            print("\n--- Delete Player Data ---")
            display_players()  
            
            player_id = int(input("\nEnter player ID to delete: "))
            player = get_player(player_id)
            if player is None:
                print("The data you are looking for does not exist")
                break
            print("\nSelected player to delete:")
            print(tabulate([player.values()], headers=player.keys(), tablefmt="fancy_grid"))
            confirm = input("\nAre you sure you want to delete this player? (yes/no): ").lower()
            
            if confirm == 'yes':
                global players
                new_players = []
                for p in players:
                    if p['id'] != player_id:
                        new_players.append(p)
                players = new_players
                print("Data successfully deleted")
                break
            else:
                break
                
        except ValueError:
            print("You must enter an integer for the player ID.")

# Function to see myplayer stats
def stats():
    if my_players:
        max_stats = my_players[0]['rating']  
        min_stats = my_players[0]['rating'] 
        max_player_name = my_players[0]['name']  
        min_player_name = my_players[0]['name']  
        player_count = 0
        print("\n--- My Players Stats ---")
        
        for player in my_players:
            player_count += 1
            if player['rating'] > max_stats:
                max_stats = player['rating']
                max_player_name = player['name']
            if player['rating'] < min_stats:
                min_stats = player['rating']
                min_player_name = player['name']

        print(f"Max Rating: {max_stats} is {max_player_name}")
        print(f"Min Rating: {min_stats} is {min_player_name}")
        print(f"Player Count: {player_count}")
        print(f"Average Rating: {round(sum(player['rating'] for player in my_players) / player_count)}")
    else:
        print("You have not bought any players yet.")

# make chemistry from each player 
def chemistry() :
    # if nation & team  are same then chemistry is 4
    # if nation & league are same then chemistry is 3
    # if nation/team is same then chemistry is 2
    # if league are same then chemistry is 1
    #  else chemistry is 1
    chem = 0
    for player in my_players:
        for other_player in my_players:
            if player  == other_player:
                continue
            if player['nation'] == other_player['nation'] and player['team'] == other_player['team']  :
                chem += 4
            elif player['nation'] == other_player['nation'] and player['league'] == other_player['league'] and player['team'] !=  other_player['team']:
                chem += 3
            elif player['nation'] == other_player['nation'] and player['team'] != other_player['team'] :
                chem += 2
            elif player['nation'] != other_player['nation'] and player['team'] == other_player['team'] :
                chem += 2
            elif player['league'] == other_player['league'] and  player['team'] != other_player['team'] and  player['nation'] != other_player['nation']:
                chem += 1
            else :
                chem += 0
    print(f"Total Team Chemistry: {chem}\n")
    return chem

# Function for buying players
def buy_player():
    while True:
        display_players()
        
        try:
            player_id = int(input("Enter player ID to buy: "))
        except ValueError:
            print("Invalid input. Player ID must be an integer. Please try again.")
            break
        
        player = get_player(player_id)
        
        if player and player["stock"] > 0:
            try:
                amount = int(input(f"How many units of {player['name']} do you want to buy? "))
                if amount <= 0:
                    print("Amount must be a positive integer. Please try again.")
                    continue
                elif amount > player["stock"]:
                    print("Not enough stock to buy")
                    continue
            except ValueError:
                print("Invalid input. Amount must be an integer. Please try again.")
                continue
            
            try:
                total_payment = player['price'] * amount
                print(f"Total Payment: {total_payment}")
                coins = int(input("Enter your available coins: "))
            except ValueError:
                print("Invalid input. Coins must be an integer. Please try again.")
                continue
            
            if coins >= total_payment:
                if amount <= player["stock"]:
                    player["stock"] -= amount
                    for i in range(amount):
                        my_players.append({
                            "name": player["name"], 
                            "position": player["position"], 
                            "rating": player["rating"], 
                            "nation": player["nation"],  
                            "team": player["team"], 
                            "league": player["league"]
                        })
                    print(f"You have bought {amount} units of {player['name']} for {total_payment} coins.")
                    print(f"You have {coins - total_payment} coins left.")
                    yn = input("Do you want to buy another player? (yes/no): ")
                    if yn.lower() != "yes":
                        break  
                else:
                    print("Not enough stock for the requested amount.")
            else:
                print("You don't have enough coins to buy this player.")
        else:
            print("Player is out of stock or not found.")

#admin menu
def menu():
    while True:
        display_menu()
        choice = input("\nChoose an option: \n")
        os.system('cls')
    
        if choice == "1":
            while True:
                read_menu()
                choice = input("\nChoose an option: ")
                os.system('cls')
                if choice == "1":
                    display_players()
                    print("\n")
                elif choice == "2":
                    search_player()
                elif choice == "3":
                    os.system('cls')
                    break
                else:
                    print("Invalid option. Please try again.")

        elif choice == "2":
            while True :
                print("1. Add Player")
                print("2. Back")
                choice = input("Choose an option: ")
                if choice == "1":
                    add_data()
                elif  choice == "2":
                    break
                
        elif choice == "3":
            while True :
                print("1. Update Player")
                print("2. Back")
                choice = input("Choose an option: ")
                if choice == "1":
                    update_player()
                elif  choice == "2":
                    break
        
        elif choice == "4":
            while True :
                print("1. Delete Player")
                print("2. Back")
                choice = input("Choose an option: ")
                if choice == "1":
                    delete_player()
                elif  choice == "2":
                    break

        elif choice == "5":
            print("Exiting system.")
            main_menu()
            break
        else:
            print("Invalid option. Please try again.")

#user menu
def user_menu():
    while True:
        user_display_menu()
        choice = input("select an option: ").strip()
        os.system('cls')
        if choice == "1":
            if my_players:
                display_my_players()
                yn = input("Do you want to expand to see the stats?  (yes/no): ")
                if yn.lower() == "yes":
                    stats()
                    chemistry()
                else:
                    continue
            else:
                print("You have no players in your squad.")
        elif choice == "2":
            buy_player()
        elif choice == "3":
            print("Exiting system")
            main_menu()
            break
        else:
            print("Invalid choice. Please try again.")

#main menu
def main_menu():
    while True:
        print("\n--- Login Menu ---")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Select an option: ").strip()
        
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Exiting System")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")
            
main_menu()

