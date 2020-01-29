#!usr/bin/python3
#Brady Durham
#1/27/20

import pickle

#dictionary
games = { 1: ['FPS', 'Halo3', 'Bungie', 'Microsoft', 'Xbox360', '2007',
              '10', 'either', '$30.00', 'yes', '1/15/2008', 'This game blows chunks!'],
              2: ['FPS', 'Doom', 'id Software', 'Bethesda Softworks', 'XboxOne', '2016',
              '10', 'either', '$10.00', 'yes', '4/8/2018', 'Heavy metal music intensifies'] }
              
def print_all_games():
    #print("running print_all_games() ")
    key_list = games.keys()
    
        
    for key in key_list:
        print("Genre: ", games[key][0])
        print("Title: ", games[key][1])
        print("Developer: ", games[key][2])
        print("Publisher: ", games[key][3])
        print("Platform: ", games[key][4])
        print("Year Released: ", games[key][5])
        print("Personal Rating: ", games[key][6])
        print("Single or Multiplayer: ", games[key][7])
        print("Price: ", games[key][8])
        print("Beaten it: ", games[key][9])
        print("Date Bought: ", games[key][10])
        print("Notes: ", games[key][11])
        print("------------------------------")
      
def search_by_title():
    #print("running search_by_title() ") 
    found_one = False
    name = input("What is the title of the game you are looking for?")
    for key in games.keys():
        if name == games[key][1]:
            found_one = True
            print()
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])
            print("Platform: ", games[key][4])
            print("Year Released: ", games[key][5])
            print("Personal Rating: ", games[key][6])
            print("Single or Multiplayer: ", games[key][7])
            print("Price: ", games[key][8])
            print("Beaten it: ", games[key][9])
            print("Date Bought: ", games[key][10])
            print("Notes: ", games[key][11])            
            print("----------------------")
            
    if not found_one:
        print("*** NO MATCHES FOUND!***\n")    

def add_game():
    print("running add_game() ")

        
def edit_game():
    print("running edit_game() ")
        
def delete_game():
   print("deleting game")
   
def save_database():
    print("saving database")
    data_file = open("game_lib.pickle", "wb")
    pickle.dump(games, data_file)
    data_file.close()    
   
def quit():
    print("Qutting Now")
    


keep_going = True


while keep_going:
    print("""
    Welcome to Game Library!
    ---------------------------
    
    MAIN MENU
    1) Print All Games
    2) Add Game
    3) Lookup By Title
    
    4) Remove A Game
    5) Save Database
    6) Edit Game
    
    Q) Quit
    
    """)
    
    choice = input("What would you like to do? ")
    if choice == "1":
        print_all_games()
    elif choice == "2":
        add_game()
    elif choice == "3":
        search_by_title()
    elif choice == "4":
        delete_game()
    elif choice == "5":
        save_database()
    elif choice == "6":
        edit_game()
    elif choice == "Q" or choice == "q":
        quit()
        keep_going = False
    else:
        print("*** NOT A VALID CHOICE ***\n")
        
print("Goodbye.")
        

