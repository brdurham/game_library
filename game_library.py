#!usr/bin/python3
#Brady Durham
#1/27/20

def print_all_games():
    print("running print_all_games() ")
    
def search_by_title():
    print("running search_by_title() ")

def add_game():
    print("running add_game() ")

        
def edit_game():
    print("running edit_game() ")
        
def delete_game():
   print("deleting game")
   
def save_database():
    print("saving database")
   
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
        

