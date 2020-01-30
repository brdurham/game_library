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
      
def search():
    keep_going = True
    
    
    while keep_going:
        print("""
        Welcome to Search Menu!
        ---------------------------
        
        Search Menu
        1)Search by genre
        2)Search by developer
        3)Search by publisher
        
        4)Search by platform 
        5)Search by release year 
        6)Search by rating
        
        7)Search by mode
        8)Search by price
        9)Search by completion
        10)Search by purchase date
        
        Q) Quit
        
       
         
        """)
        
        choice = input("What would you like to do? ")        
        if choice == "1":
            search_by_genre()
        elif choice == "2":
            search_by_developer()
        elif choice == "3":
            search_by_publisher()
        elif choice == "4":
            search_by_platform()
        elif choice == "5":
            search_by_year()
        elif choice == "6":
            search_by_rating()
        elif choice == "7":
            search_by_mode()
        elif choice == "8":
            search_by_price()
        elif choice == "9":
            search_by_completion()
        elif choice == "10":
            search_by_purchase_date()
        elif choice == "Q" or choice == "q":
            quit()
        else:
            print("*** NOT A VALID CHOICE ***\n")

      
def search_by_title():
    #print("running search_by_title() ") 
    found_one = False
    name = input("What is the title of the game you are looking for?")
    for key in games.keys():
        if name == games[key][1]:
            found_one = True
            print()
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
            print("----------------------")
            
    if not found_one:
        print("*** NO MATCHES FOUND!***\n")
        
def search_by_genre():
    found_one = False
    name = input("What is the genre you are looking for?")
    for key in games.keys():
        if name == games[key][0]:
            found_one = True
            print()
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
            print("----------------------")
            
    if not found_one:
        print("*** NO MATCHES FOUND!***\n")
        
def search_by_developer():
    found_one = False
    name = input("What is the developer you are looking for?")
    for key in games.keys():
        if name == games[key][2]:
            found_one = True
            print()
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
            print("----------------------")
            
    if not found_one:
        print("*** NO MATCHES FOUND!***\n")
            
def search_by_publisher():
    found_one = False
    name = input("What is the publisher you are looking for?")
    for key in games.keys():
        if name == games[key][3]:
            found_one = True
            print()
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
            print("----------------------")
            
    if not found_one:
        print("*** NO MATCHES FOUND!***\n")
                
def search_by_platform():
    found_one = False
    name = input("What is the platform you are looking for?")
    for key in games.keys():
        if name == games[key][4]:
            found_one = True
            print()
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
            print("----------------------")
            
    if not found_one:
        print("*** NO MATCHES FOUND!***\n")
                    
def search_by_year():
    found_one = False
    name = input("What is the release year you are looking for?")
    for key in games.keys():
        if name == games[key][5]:
            found_one = True
            print()
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
            print("----------------------")
            
    if not found_one:
        print("*** NO MATCHES FOUND!***\n")
                        
def search_by_rating():
    found_one = False
    name = input("What is the rating you are looking for?")
    for key in games.keys():
        if name == games[key][6]:
            found_one = True
            print()
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
            print("----------------------")
            
    if not found_one:
        print("*** NO MATCHES FOUND!***\n")
                            
def search_by_mode():
    found_one = False
    name = input("What is the player mode you are looking for?")
    for key in games.keys():
        if name == games[key][7]:
            found_one = True
            print()
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
            print("----------------------")
            
    if not found_one:
        print("*** NO MATCHES FOUND!***\n")
                                
def search_by_price():
    found_one = False
    name = input("What is the pricing you are looking for?")
    for key in games.keys():
        if name == games[key][8]:
            found_one = True
            print()
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
            print("----------------------")
            
    if not found_one:
        print("*** NO MATCHES FOUND!***\n")
                                    
def search_by_completion():
    found_one = False
    name = input("Have you beaten what you are looking for?")
    for key in games.keys():
        if name == games[key][9]:
            found_one = True
            print()
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
            print("----------------------")
            
    if not found_one:
        print("*** NO MATCHES FOUND!***\n") 
                                        
def search_by_purchase_date():
    found_one = False
    name = input("What is the purchase date you are looking for?")
    for key in games.keys():
        if name == games[key][10]:
            found_one = True
            print()
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
            print("----------------------")
            
    if not found_one:
        print("*** NO MATCHES FOUND!***\n")


def add_game():
    #print("running add_game() ")
    new_key = len(games) + 1
    new_entry = []
    valid = False
    while not valid:
        genre = input("What is the genre?")
        new_entry.append(genre)
        title = input("What is the title?")
        new_entry.append(title)
        developer = input("What is the developer?")
        new_entry.append(developer)
        publisher = input("What is the publisher?")
        new_entry.append(publisher)
        platform = input("What is the platform?")
        new_entry.append(platform)
        year = input("What is the release year?")
        new_entry.append(year)
        rating = input("What is the rating?")
        new_entry.append(rating)
        mode = input("Is it single or multiplayer?")
        new_entry.append(mode)
        price = input("What is the price?")
        new_entry.append(price)
        completion = input("Have you beaten it?")
        new_entry.append(completion)
        date = input("What is the purchase date?")
        new_entry.append(date)
        notes = input(" ")
        new_entry.append(notes)
        
        
        
        answer = input("Is this correct?")
        if answer.lower() in ("yes, y"):
            valid = True
        games[new_key] = new_entry
    
        
def edit_game():
    #print("running edit_game() ")
    print("Here is the library: ")
    for key in games.keys():
        print(key, "-", games[key][1])
        edit_key = input("Which game would you like to edit?")
        edit_entry = games[edit_key]
        genre = input("What is the genre?")
        print("Current Genre: ", edit_entry[0])
        edit_entry[0] = input("New Genre: ")
        title = input("What is the title?")
        print("Current Title: ", edit_entry[1])
        edit_entry[1] = input("New Title: ")
        developer = input("What is the developer?")
        print("Current Developer: ", edit_entry[2])
        edit_entry[2] = input("New Developer: ")
        publisher = input("What is the publisher?")
        print("Current Publisher: ", edit_entry[3])
        edit_entry[3] = input("New Publisher: ")
        platform = input("What is the platform?")
        print("Current Platform: ", edit_entry[4])
        edit_entry[4] = input("New Platform: ")
        year = input("What is the release year?")
        print("Current Release Year: ", edit_entry[5])
        edit_entry[5] = input("New Release Year: ")
        rating = input("What is the rating?")
        print("Current Rating: ", edit_entry[6])
        edit_entry[6] = input("Rating: ")
        mode = input("Is it single or multiplayer?")
        print("Current Mode: ", edit_entry[7])
        edit_entry[7] = input("New Mode: ")
        price = input("What is the price?")
        print("Current Price: ", edit_entry[8])
        edit_entry[8] = input("New Price: ")
        completion = input("Have you beaten it?")
        print("Current Completion: ", edit_entry[9])
        edit_entry[9] = input("New Completion: ")
        date = input("What is the purchase date?")
        print("Current Purchase Date: ", edit_entry[10])
        edit_entry[10] = input("New Purchase Date: ")
        notes = input(" ")
        print("Current Notes: ", edit_entry[11])
        edit_entry[11] = input("New Notes: ")
    
    
        
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
    3) Edit Game
    
    4)Search Database
    5) Remove A Game
    6) Save Database
    
    Q) Quit
    
   
     
    """)
    
    choice = input("What would you like to do? ")
    if choice == "1":
        print_all_games()
    elif choice == "2":
        add_game()
    elif choice == "3":
        edit_game()
    elif choice == "4":
        search()
    elif choice == "5":
        delete_game()
    elif choice == "6":
        save_database()      
    elif choice == "Q" or choice == "q":
        quit()
        keep_going = False
    else:
        print("*** NOT A VALID CHOICE ***\n")
        
print("Goodbye.")
        

